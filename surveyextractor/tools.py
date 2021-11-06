from os.path import exists
import requests
from requests.auth import HTTPBasicAuth
from surveyextractor import xmltodict
from pprint import pprint as pp
import time
from typing import List, Dict, Any
from requests.exceptions import HTTPError

import argparse


def p(object):
    """Nice prettyprint"""
    pp(object, sort_dicts=False)


def fix_keyname(old_name: str) -> str:
    """Change characters for usefull names"""
    return old_name.replace("/", "_")


def get_api_data(
    url: str, survey_id: int, survey_user: str, survey_password: str, cache: bool = True
) -> Dict:
    """Get data from the API"""
    cache_file = f"test_{survey_id}.xml"
    use_cache = True if cache and exists(cache_file) else False

    if not use_cache:
        try:
            response = requests.get(
                url, auth=HTTPBasicAuth(survey_user, survey_password)
            )

            if response.status_code == 403:
                raise HTTPError(
                    f"User {survey_user} is not allowed to access survey {survey_id}, HTTP code 403"
                )

            with open(cache_file, "wb") as fp:
                content = response.content
                fp.write(response.content)
            # time.sleep(1)
        except Exception as e:
            print("Internal error", e)
            exit(f"{e} wrong survey id")
    else:
        with open(cache_file, "rb") as fp:
            content = fp.read()

    api_data = xmltodict.parse(
        content,
        attr_prefix="attr_",
        force_list=(
            "respondent",
            "varChoice",
            "choice",
        ),
    )

    output = {}

    api_data = api_data["dataset"]
    if (
        isinstance(api_data["respondents"], dict)
        and "respondent" in api_data["respondents"]
    ):
        output.update(api_data["respondents"])

    if "variable" in api_data["variables"]:
        output.update(api_data["variables"])

    return output


def is_digit(text: str) -> bool:
    """Function to test if string is a number, including decimal numbers"""
    return text.replace("-", "", 1).isdigit()


def convert_variable(variable_list):
    variable = []
    for var in variable_list:
        key_name = fix_keyname(var["attr_name"])
        formatted_variable = {
            "name": key_name,
            "text": var["text"]["#text"],
            "type": var["attr_type"],
        }
        if not "varChoice" in var:
            variable.append(formatted_variable)
            continue
        for answer in var["varChoice"]:
            formatted_variable = {
                **formatted_variable,
                "attr_id": int(answer["attr_id"]),
                "value": int(answer["attr_value"]),
                "text": answer["text"]["#text"],
            }
            variable.append(formatted_variable)

    return variable

    var["attr_name"]
    return variable


def text(input):
    if isinstance(input, int):
        return str(input)
    else:
        return f"'{input}'"


def convert_respondents(respondents):
    answers = []
    # omskriv xmltodict, så keys bliver name

    for answer in respondents:
        new = {"respondent_externkey": answer["attr_externkey"]}
        for key, value in answer.items():
            if isinstance(value, list):
                for it in value:
                    key_name = fix_keyname(it["attr_name"])
                    if "#text" in it:
                        new[key_name] = (
                            int(it["#text"]) if is_digit(it["#text"]) else it["#text"]
                        )

                    if "choice" in it:
                        choices = (
                            int(it["choice"][0]["attr_id"])
                            if len(it["choice"]) == 1
                            else [int(att["attr_id"]) for att in it["choice"]]
                        )
                        if key == "valueMultiple":
                            choices = [int(att["attr_id"]) for att in it["choice"]]
                            # print(it['choice'])
                        new[key_name] = choices
        else:
            answers.append(new)
    return answers


def answers_schema(
    variables: List[Dict], answers_table: str, unique_columns: tuple
) -> str:
    """Define table schema for Labels by types in variables"""

    types = {
        "multiple": "INT[]",
        "string": "TEXT",
        "single": "INT",
        "double": "numeric",
        "dateTime": "timestamptz",
    }
    out = {"answer_id": "SERIAL PRIMARY KEY"}

    for var in variables:
        out[var["name"]] = types.get(var["type"], "TEXT")
        # print(var["type"])
    else:
        string = f"CREATE TABLE {answers_table} (\n"
        string += " respondent_externkey varchar(24) \n,"
        string += " , \n ".join(key + " " + value for key, value in out.items())
        string += f", UNIQUE({','.join(unique_columns)})"
        string += ");"
        # string += f"CREATE UNIQUE INDEX ON {answers_table} (respondent_externkey, respondent_modified)"
    return string


def sql_insert(table_name: str, element: dict, unique_columns: List[str] = None) -> str:
    columns = list(element.keys())
    column = ", ".join(columns)
    placeholder_values = ", ".join("%s" for value in columns)
    values_updating = tuple(
        str(v).replace("[", "{").replace("]", "}") if isinstance(v, list) else v
        for v in element.values()
    )

    if unique_columns is None:
        conflict = " ON CONFLICT DO NOTHING;"
    else:
        conflict = f" ON CONFLICT ({','.join(unique_columns)}) DO UPDATE SET ({column}) = {values_updating};"

    sql = f"INSERT INTO {table_name} ({column}) VALUES ({placeholder_values}) {conflict};".replace("'Null'", "Null")
    return sql


def parse_args(description="Hvad gør dette program?"):
    """Arguments for CLI program:
    eg.
    $ python create_tables_api.py -i survey_id

    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-i", "--survey_id", type=int, help="Survey ID"
    )

    args = parser.parse_args()
    parser.parse_args()

    if not args.survey_id:
        parser.error("Missing survey id")

    # Få det som en dictionary
    return vars(args)

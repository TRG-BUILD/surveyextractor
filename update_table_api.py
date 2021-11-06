import requests
from requests.auth import HTTPBasicAuth
from decouple import config, Csv
from surveyextractor.tools import *
from pprint import pprint as pp
from os.path import exists
from sqlalchemy import create_engine
from typing import List, Dict

if __name__ == "__main__":
    """TODO: Create CLI with survey id parameter"""
    key = parse_args("Hent besvarelser!")

    unique_columns = config('unique_columns', default=None, cast=Csv(str))
    survey_user = config("survey_user", default="empty", cast=str)
    survey_password = config("survey_password", cast=str)

    survey_id = key["survey_id"]

    conn_string = config("connection_string", default=None, cast=str)
    engine = create_engine(conn_string, echo=False)
    con = engine.connect()

    answers_table = f"answers_{survey_id}"
    table_exists = engine.dialect.has_table(con, answers_table)
    last_modified_arg = ""

    if table_exists:
        sql_lastmodified = f"SELECT to_char(respondent_modified, 'yyyyMMdd_HH24MIss') as formated_date FROM {answers_table} order by respondent_modified DESC limit 1;"
        result = con.execute(sql_lastmodified)
        if result.rowcount == 1:
            last_modified_arg = f"&modifiedSince={result.first()[0]}"
        print(last_modified_arg)

    url = f"https://rest.survey-xact.dk/rest/surveys/{survey_id}/export/dataset?format=XML{last_modified_arg}"  # &modifiedSince=20211029_081010"
    print(url)
    api_data = get_api_data(url, survey_id, survey_user, survey_password, cache=False)

    variable_tag = api_data["variable"]
    variables = convert_variable(variable_tag)
    answer_schema = answers_schema(variables, answers_table, unique_columns)

    respondents = api_data["respondent"] if "respondent" in api_data else {}
    answers = convert_respondents(respondents)
    print(f"Answers since last time: {len(answers)}")
    if not table_exists:
        print(f"Creating table: {answers_table}")
        rs = con.execute(answer_schema)

    for idx, item in enumerate(answers):
        if not isinstance(item, dict):
            # print(item)
            continue
        list_of_values = list(item.values())
        sql = sql_insert(answers_table, item, unique_columns)
        rs = con.execute(sql, list_of_values)
    else:
        print(f"Succesfully imported {idx+1} answers from survey {survey_id} to db.")

    con.close()

import requests
from requests.auth import HTTPBasicAuth
from decouple import config
from surveyextractor.tools import *
from os.path import exists
from sqlalchemy import create_engine
from typing import List, Dict


if __name__ == "__main__":
    """TODO: Create CLI with survey id parameter"""
    key = parse_args()

    survey_user = config("survey_user", default="empty", cast=str)
    survey_password = config("survey_password", cast=str)

    survey_id = key["survey_id"]

    url = f"https://rest.survey-xact.dk/rest/surveys/{survey_id}/export/dataset?format=XML"

    api_data = get_api_data(url, survey_id, survey_user, survey_password)


    variable_tag = api_data["variable"]
    variables = convert_variable(variable_tag)

    # INSERT VARIABLES TO TABLE
    labels_table = f"labels_{survey_id}"

    label_schema = f"""CREATE TABLE {labels_table} (
        id serial,
        name varchar(255),
        text text,
        type varchar(255),
        attr_id int,
        value int,
        UNIQUE(name, attr_id, value)
        );
        CREATE UNIQUE INDEX i_null_{labels_table} ON {labels_table} (name, (attr_id IS NULL), (value IS NULL))
                        WHERE attr_id IS NULL;
        """

    conn_string = config("connection_string", default=None, cast=str)
    engine = create_engine(conn_string, echo=False)
    with engine.connect() as con:
        if not engine.dialect.has_table(con, labels_table):
            rs = con.execute(label_schema)

        for item in variables:
            if not isinstance(item, dict):
                continue

            sql = sql_insert(labels_table, item)
            rs = con.execute(sql, list(item.values()))
        else:
            print(f"Succesfully import variables from survey_id {survey_id}")

'''

Description: Easy Truncate survey answers_tabel.

'''

from surveyextractor.tools import *
from sqlalchemy import create_engine
from decouple import config, Csv


if __name__ == "__main__":

    #key = parse_args("Tilføj mailsystem felter til survey tabel")
    survey_id = key["survey_id"]
    conn_string = config("connection_string", default=None, cast=str)

    engine = create_engine(conn_string, echo=False)
    con = engine.connect()

    answers_table = f"answers_{survey_id}"
    table_exists = engine.dialect.has_table(con, answers_table)

    if not table_exists:
        exit(f"opret tabellen {answers_table} først.")

    sql = f"""TRUNCATE TABLE {answers_table};"""
    #result = con.execute(sql)

    print(sql)
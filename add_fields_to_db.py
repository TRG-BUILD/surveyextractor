'''

Description: Add fields to survey answers tabel, for the mailer system.

'''

from surveyextractor.tools import *
from sqlalchemy import create_engine
from decouple import config, Csv


if __name__ == "__main__":

    #key = parse_args("Tilføj mailsystem felter til survey tabel")
    survey_id = 1293732 #key["survey_id"]
    conn_string = config("connection_string", default=None, cast=str)

    engine = create_engine(conn_string, echo=False)
    con = engine.connect()

    answers_table = f"answers_{survey_id}"
    table_exists = engine.dialect.has_table(con, answers_table)

    if not table_exists:
        exit(f"opret tabellen {answers_table} først.")

    sql = f"""ALTER TABLE {answers_table}
       ADD COLUMN  strategi_mail_send_first timestamptz,
       ADD COLUMN  strategi_mail_send_first_failed timestamptz,
       ADD COLUMN  strategi_mail_send_second timestamptz,
       ADD COLUMN  strategi_mail_send_second_failed timestamptz;"""
    result = con.execute(sql)

    print(result)
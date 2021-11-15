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

    sql = f"""drop view if exists strategi_mailings;
    CREATE VIEW strategi_mailings as
    SELECT * FROM (SELECT
    answer_id as respondentid,
    respondent_externkey as respondent_externkey,
    EXTRACT(EPOCH FROM now()-respondent_closetime)/60/60/24 as days_since_done,
    respondent_closetime as closetime,
    now() as today,
    l1.text as situation1_text,
    l2.text as strategi1_text,
    l3.text as situation2_text,
    l4.text as strategi2_text,
    l5.text as situation3_text,
    l6.text as strategi3_text,
    questionnaire_strategi_tekstfelt,
    l7.value as strategimail,
    l8.value as strategireminder,
    questionnaire_email_strategi as email_strategi,
    questionnaire_del1b_kommentar,
    background_id, background_gr,
    background_s,
    strategi_mail_send_first,
    strategi_mail_send_first_failed,
    strategi_mail_send_second,
    strategi_mail_send_second_failed
    FROM public.answers_{survey_id}
    LEFT JOIN labels_{survey_id} l1	ON (questionnaire_situation1 = l1.attr_id)
    LEFT JOIN labels_{survey_id} l2	ON (questionnaire_strategi1 = l2.attr_id)
    LEFT JOIN labels_{survey_id} l3	ON (questionnaire_situation2 = l3.attr_id)
    LEFT JOIN labels_{survey_id} l4	ON (questionnaire_strategi2 = l4.attr_id)
    LEFT JOIN labels_{survey_id} l5	ON (questionnaire_situation3 = l5.attr_id)
    LEFT JOIN labels_{survey_id} l6	ON (questionnaire_strategi3 = l6.attr_id)
        LEFT JOIN labels_{survey_id} l7	ON (questionnaire_strategimail = l7.attr_id)
        LEFT JOIN labels_{survey_id} l8	ON (questionnaire_strategireminder = l8.attr_id)
    ) foo
    where
    strategimail = 1 AND
    strategireminder = 1 AND
    (strategi_mail_send_first is null OR strategi_mail_send_second is null)
    and email_strategi is not null;"""

    conn_string = config("connection_string", default=None, cast=str)
    engine = create_engine(conn_string, echo=False)
    with engine.connect() as con:
        rs = con.execute(sql)

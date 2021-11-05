import pandas as pd

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from surveyextractor.orm.models import Survey, Label, Answer3


def start_session(engine):
    """Start session to access or read data from engine"""
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    return Session()


def create_survey(id, name, session):
    """Create survey in database"""
    ns = Survey(id=id, name=name)
    session.add(ns)
    session.commit()


def load_dataset(filename="csv/dataset_utf-8.csv", session=None):
    df = pd.read_csv(filename, delimiter=";")
    df.to_sql("answers3", engine, if_exists="append", index_label="answer_id")


if __name__ == "__main__":
    # engine = create_engine('sqlite:///main.sqlite3', echo=True)
    conn_string = "postgresql+psycopg2://postgres:changeme@localhost/vttt"
    engine = create_engine(conn_string, echo=True)

    session = start_session(engine)

    create_survey(1293732, "EASE - del 1b", session)

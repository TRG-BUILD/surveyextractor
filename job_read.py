"""
job_read.py is running a cronjob each hour.


"""


from abc import ABC, abstractmethod

from sqlalchemy import create_engine

from surveyextractor.factories import *

if __name__ == "__main__":
    what_in = "CSV"
    what_out = "CSV"

    # Initialize database
    conn_string = 'postgresql+psycopg2://postgres:changeme@localhost/vttt'
    #conn_string = "sqlite:///main.sqlite3"
    engine = create_engine(conn_string, echo=True)

    # Initialise Reader and Writer:
    reader = get_factory(factories_import, what_in)
    write = get_factory(factories_export, what_out)

    # Read dataset
    read = reader(1293732, "EASE - del 1b", "csv/dataset.csv",  encoding="ISO8859-1")
    dataset = read.read()

    # Ugly hack, convert decimalnumber to correct with . as separator

    #for row in dataset.answers:
    #    row['difftime'] = row['difftime'].replace(',', '.')

    # Write Dataset
    #dst = write(filename="test.csv")
    #dst.writer(dataset)
    #l  = dataset.answers[3]

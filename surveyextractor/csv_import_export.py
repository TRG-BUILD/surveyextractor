""" Create reader

Implement two different readers, one for CSV files and one for interacting with the surveyxact webservice.

"""


from abc import ABC, abstractmethod
import csv

import requests
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree

from typing import List, Dict
from surveyextractor.datamodel import Survey, Answer1b

from sqlalchemy import create_engine

from surveyextractor.abstracts import DataImporter, DataExporter
from dataclasses import asdict, fields


class CSVReader(DataImporter):
    """Reading csv file into"""

    def __init__(
        self, survey_id, survey_name, filename, delimiter=";", encoding="UTF-8"
    ):
        self.filename: str = filename
        self.delimiter: str = delimiter
        self.encoding: str = encoding
        self.survey: Survey = Survey(survey_id=survey_id, name=survey_name)

    def read(self, **kwargs) -> List[Dict]:
        with open(self.filename, "r", encoding=self.encoding) as csvfile:
            reader = csv.DictReader(csvfile, delimiter=self.delimiter)
            for row in reader:
                self.survey.answers.append(Answer1b(**row))
            return self.survey


class APIReader(DataImporter):
    """Reading survey data from SurveyXacts API"""

    def __init__(self, url, username, password):
        pass

    def read(self) -> List[Dict]:
        pass


""" Writers for Survey """
class CSVWriter(DataExporter):
    """Write CSV file from Survey object"""

    def __init__(self, filename, delimiter=";", encoding="UTF-8"):
        self.filename: str = filename
        self.delimiter: str = delimiter
        self.encoding: str = encoding

    def writer(self, dataset: Survey):
        with open(self.filename, "w", encoding=self.encoding) as csvfile:
            fieldnames = [field.name for field in fields(Answer1b)]
            csv_writer = csv.DictWriter(
                csvfile, fieldnames=fieldnames, delimiter=self.delimiter
            )

            csv_writer.writeheader()
            csv_writer.writerows([asdict(row) for row in dataset.answers])



class SQLiteWriter(DataExporter):
    """Write CSV file from Survey object"""

    def __init__(self, engine):
        self.engine: str = engine

    def writer(self, dataset: Survey):
        with self.engine.connect() as con:
            for item in dataset.answers:
                #clean for missing info
                item = asdict(item)
                column = ", ".join(item.keys())
                values = ", ".join("'" + value + "'" for value in item.values())
                sql = f"INSERT INTO answers3 ({column}) VALUES ({values})".replace("'Null'", "Null")
                rs = con.execute(sql)


if __name__ == "__main__":

    # Test read
    csv_read = CSVReader(1293732, "EASE - del 1b", "../csv/dataset_utf-8.csv")

    dataset = csv_read.read()
    print(dataset)

    # Working:

    engine = create_engine('sqlite:///main.sqlite3', echo=True)
    writer = SQLiteWriter(engine)
    writer.writer(dataset)

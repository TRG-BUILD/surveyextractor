
from abc import ABC, abstractmethod
from typing import List, Dict

class DataImporter(ABC):
    """Abstract factory for reading data to list of surveyresult"""

    @abstractmethod
    def read(self):
        """Reader method for filetype"""


class DataExporter(ABC):
    """Abstract factory for Writint datamodels"""

    @abstractmethod
    def writer(self, dataset: List[Dict]):
        """Write dataset object"""


class ImporterFactory(ABC):
    """
    Factory that represents an importer and exporter codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_importer(self) -> DataImporter:
        """Returns a new file importer belonging to this factory."""


class ExporterFactory(ABC):
    """
    Factory that represents an exporter codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_exporter(self) -> DataExporter:
        """Returns a new exporter belonging to this factory."""

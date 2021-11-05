from .csv_import_export import CSVWriter, CSVReader, DataImporter, DataExporter, APIReader, SQLiteWriter
from .abstracts import ImporterFactory, DataImporter, DataExporter
from .datamodel import Survey



class CSV2CSVFactory(ImporterFactory):
    """ Converting from CSV file 2 CSV file"""
    def get_importer(self) -> DataImporter:
        return CSVWriter()

    def get_exporter(self) -> DataExporter:
        return CSVReader()



class CSV2CSVFactory(ImporterFactory):
    """ Converting from CSV file 2 CSV file"""
    def get_importer(self) -> DataImporter:
        return CSVWriter()

    def get_exporter(self) -> DataExporter:
        return CSVReader()

factories_import = {
        "CSV": CSVReader,
        "API": APIReader
    }

factories_export = {
        "CSV": CSVWriter,
        "SQL": SQLiteWriter,
    }

def get_factory(factory_name, what) -> Survey:

    try:
        return factory_name[what]
    except Exception:
        exit(f"Missing factory: {what}")


if __name__ == "__main__":
    # What reader is wanted:

    what_in = "CSV"
    what_out = "CSV"

    # Initialise Reader and Writer:
    reader = get_factory(factories_import, what_in)
    write = get_factory(factories_export, what_out)


    # Read dataset
    read = reader(1293732, "EASE - del 1b", "../csv/dataset_utf-8.csv")
    dataset = read.read()


    # Write Dataset
    dst = write(filename="csv/dataset_utf-8_dddd121221.csv")
    dst.writer(dataset)
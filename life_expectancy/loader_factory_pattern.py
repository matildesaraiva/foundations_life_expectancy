from abc import ABC, abstractmethod
import pandas as pd
import zipfile
import json

class LoaderFactory(ABC):
    """
    Abstract base class (LoaderFactory) that represents a combination of:
        - unzip files method
        - abstract method to loading several file formats (to be implemented in each sub-class)
    """
    def __init__(self, file_path: str):
        self.file_path = file_path

    def unzip_file(self) -> str:
        # Returns the file as it's found.
        return self.file_path

    @abstractmethod
    def load_data(self) -> pd.DataFrame:
        # It's passed to be implemented in other sub-classes
        pass


class CSVLoader(LoaderFactory):
    # loads data from a .csv file
    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.unzip_file())

class TSVLoader(LoaderFactory):
    # loads data from a .tsv file
    def load_data(self) -> pd.DataFrame:
        return pd.read_csv(self.unzip_file(), sep="\t")

class XLSXLoader(LoaderFactory):
    # loads data from a .xlsx file
    def load_data(self) -> pd.DataFrame:
        return pd.read_excel(self.unzip_file(), engine="openpyxl")

class XLSLoader(LoaderFactory):
    # loads data from a .xls file
    def load_data(self) -> pd.DataFrame:
        return pd.read_excel(self.unzip_file(), engine="xlrd")

class JSONLoader(LoaderFactory):
    # loads data from a .json file
    def load_data(self) -> pd.DataFrame:
        with open(self.unzip_file(), "r") as f:
            data = json.load(f)
        return pd.DataFrame(data)

class ParquetLoader(LoaderFactory):
    # loads data from a .parquet file
    def load_data(self) -> pd.DataFrame:
        return pd.read_parquet(self.unzip_file())

class ZippedFileLoader(LoaderFactory):
    # Unzips, detects file format and loads it into the correct loader.
    def unzip_file(self) -> str:
        # Unzips the archive
        with zipfile.ZipFile(self.file_path, 'r') as zip_ref:
            inner_file = zip_ref.namelist()[0]
            zip_ref.extract(inner_file, '/tmp')
            return f"/tmp/{inner_file}"

    def load_data(self) -> pd.DataFrame:
        # Loads the unzipped file into the appropriate loader.
        unzipped_path = self.unzip_file()
        inner_loader = get_loader(unzipped_path)
        return inner_loader.load_data()

def get_loader(file_path: str) -> LoaderFactory:
    if file_path.endswith('.csv'):
        return CSVLoader(file_path)
    elif file_path.endswith('.tsv'):
        return TSVLoader(file_path)
    elif file_path.endswith('.xlsx'):
        return XLSXLoader(file_path)
    elif file_path.endswith('.xls'):
        return XLSLoader(file_path)
    elif file_path.endswith('.json'):
        return JSONLoader(file_path)
    elif file_path.endswith('.parquet'):
        return ParquetLoader(file_path)
    elif file_path.endswith('.zip'):
        return ZippedFileLoader(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path}")
    
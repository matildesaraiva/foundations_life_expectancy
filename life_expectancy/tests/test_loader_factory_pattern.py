import pandas as pd
from life_expectancy.loader_factory_pattern import (
    get_loader,
    CSVLoader,
    TSVLoader,
    XLSXLoader,
    XLSLoader,
    JSONLoader,
    ParquetLoader,
    ZippedFileLoader
)

def test_get_loader_returns_correct_class():
    """
    Tests if get_loader returns an instance of the correct loader for its extension
    """
    assert isinstance(get_loader("file.csv"), CSVLoader)
    assert isinstance(get_loader("file.tsv"), TSVLoader)
    assert isinstance(get_loader("file.xlsx"), XLSXLoader)
    assert isinstance(get_loader("file.xls"), XLSLoader)
    assert isinstance(get_loader("file.json"), JSONLoader)
    assert isinstance(get_loader("file.parquet"), ParquetLoader)
    assert isinstance(get_loader("file.zip"), ZippedFileLoader)

def test_zipped_file_loader_unzip_file(monkeypatch):
    """
    tests if the unzip_file method extracts the inner file correctly and returns its path.
    """
    loader = ZippedFileLoader("dummy.zip")
    class DummyZip:
        def __enter__(self):
            return self
        def __exit__(self, exc_type, exc_val, exc_tb):
            pass
        def namelist(self):
            return ["innerfile.csv"]
        def extract(self, name, path):
            pass
    
    monkeypatch.setattr("zipfile.ZipFile", lambda file, mode: DummyZip())
    
    path = loader.unzip_file()
    assert path == "/tmp/innerfile.csv"
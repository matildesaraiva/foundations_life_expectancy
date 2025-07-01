"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR
from life_expectancy.loading_data import load_data

@pytest.fixture(scope="session")
def eu_life_expectancy_raw() -> pd.DataFrame:
    """Fixture to load input sample to test cleaning."""
    return load_data(use_fixture=True)

@pytest.fixture(scope="session")
def eu_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load expected output of cleaning sample."""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    """Fixture to load the expected output of the cleaning script"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")

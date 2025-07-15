"""Testing 'preprocessing_data' module"""

import pandas as pd

from life_expectancy.region import Region
from life_expectancy.preprocessing_data import clean_data

def _exclude_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only actual countries.
    """
    keep = {m.value for m in Region.country_members()}
    return df[df["region"].isin(keep)].reset_index(drop=True)

def test_clean_data(
        eu_life_expectancy_raw,
        eu_life_expectancy_expected):
    """
    Testing if 'clean_data' function transforms the raw fixture dataframe
    into the expected cleaned cleaned dataframe.
    """
    df = clean_data(eu_life_expectancy_raw)

    pd.testing.assert_frame_equal(
        df.reset_index(drop=True),
        _exclude_groups(eu_life_expectancy_expected),
    )

def test_clean_data_flag(eu_life_expectancy_expected):
    """
    Testing if clean_data(use_fixture=True) loads the raw fixture
    and produces the same explected cleaned dataframe.
    """
    df = clean_data(use_fixture=True)
    pd.testing.assert_frame_equal(
        df.reset_index(drop=True),
        _exclude_groups(eu_life_expectancy_expected),
    )
    
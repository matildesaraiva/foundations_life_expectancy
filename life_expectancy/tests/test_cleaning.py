"""Tests for the cleaning module"""
import pandas as pd

from life_expectancy.cleaning import clean_data, load_data

def test_clean_data(pt_life_expectancy_expected):
    """Run the `clean_data` function and compare the output to the expected output"""
    country_code = 'PT'
    raw_data = load_data()
    cleaned_data = clean_data(raw_data, country_code=country_code)

    pd.testing.assert_frame_equal(
        cleaned_data.reset_index(drop=True),
        pt_life_expectancy_expected.reset_index(drop=True)
    )

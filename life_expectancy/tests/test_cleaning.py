"""Testing 'cleaning' module"""
import sys
import pandas as pd

from life_expectancy import cleaning
from . import FIXTURES_DIR

from life_expectancy.cleaning import main
import life_expectancy.loading_data as load_data

def test_main(eu_life_expectancy_raw, eu_life_expectancy_expected):
    cleaned = main(raw_data=eu_life_expectancy_raw)

    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True),
        eu_life_expectancy_expected.reset_index(drop=True)
    )
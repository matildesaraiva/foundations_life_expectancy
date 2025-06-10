"""Testing 'loading_data' module"""

import pandas as pd

from . import FIXTURES_DIR
from life_expectancy.loading_data import load_data

def test_load_data(eu_life_expectancy_raw):
    """
    Testing if 'load_data' function reads the raw file
    in the same way as fixture 'eu_life_expectancy_raw'.
    """
    df = load_data(use_fixture=True)

    pd.testing.assert_frame_equal(df, eu_life_expectancy_raw)
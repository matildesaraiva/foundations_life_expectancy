"""Testing 'cleaning' module"""
import sys
import pandas as pd

from life_expectancy.region import Region
from life_expectancy.cleaning import main

def _exclude_groups(df: pd.DataFrame) -> pd.DataFrame:
    """
    Keep only actual countries.
    """
    keep = {m.value for m in Region.country_members()}
    return df[df["region"].isin(keep)].reset_index(drop=True)

def test_main(eu_life_expectancy_raw, eu_life_expectancy_expected):
    """
    Testing if it returns the entire dataset
    """
    cleaned = main(raw_data=eu_life_expectancy_raw)

    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True),
        _exclude_groups(eu_life_expectancy_expected),
    )

def test_main_flag_all(monkeypatch, eu_life_expectancy_expected):
    """
    Testing if --fixture with --all returns the same as
    eu_life_expectancy_expected's fixture.
    """
    monkeypatch.setattr(sys, 'argv', [
        'cleaning.py', '--fixture', '--all'
    ])
    cleaned = main()
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True),
        _exclude_groups(eu_life_expectancy_expected),
    )

def test_main_flag_country(pt_life_expectancy_expected, monkeypatch):
    """
    Testing if --country PT returns the same as
    pt_life_expectancy_expected's fixture.
    """
    monkeypatch.setattr(sys, 'argv', [
        'cleaning.py', '--country', 'PT'
    ])
    cleaned = main()
    pd.testing.assert_frame_equal(
        cleaned.reset_index(drop=True),
        pt_life_expectancy_expected.reset_index(drop=True)
    )

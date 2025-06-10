"""
This module cleans the raw life expectancy dataset and converts it into a dataset
for Portugal by default. You can also specify a different country for the dataset.
"""

import argparse
import pandas as pd

from life_expectancy.loading_data import load_data
from life_expectancy.preprocessing_data import clean_data
from life_expectancy.saving_data import save_data

def main(raw_data=None):
    """
    Main function for cleaning life expectancy data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', default='PT', help='Country code')
    parser.add_argument('--all', action='store_true', help='All countries')
    args = parser.parse_args()

    if raw_data is None:
        raw_data = load_data()

    if args.all:
        cleaned_data = clean_data(raw_data, country_code=None)
        save_data(cleaned_data, country_code='ALL')
    else:
        cleaned_data = clean_data(raw_data, country_code=args.country)
        save_data(cleaned_data, country_code=args.country)

    return cleaned_data

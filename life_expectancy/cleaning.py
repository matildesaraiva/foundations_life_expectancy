"""
This module cleans the raw life expectancy dataset and converts it into a dataset
for Portugal by default. You can also specify a different country for the dataset.
"""

from typing import Optional
import argparse
import pandas as pd

from life_expectancy.loading_data import load_data
from life_expectancy.preprocessing_data import clean_data
from life_expectancy.saving_data import save_data

def main(raw_data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
    """
    Main function for cleaning life expectancy data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', default='PT', help='Country code')
    parser.add_argument('--all', action='store_true', help='All countries')
    parser.add_argument(
        '--fixture',
        action='store_true',
        help='Uses fixture as input',
    )
    args = parser.parse_args()
    
    # If raw_data was passed, consider --all countries run
    if raw_data is not None:
        args.all = True

    # load if needed
    if raw_data is None:    
        raw_data = load_data(use_fixture=args.fixture)

    # clean
    if args.all:
        cleaned_data = clean_data(
            raw_data,
            country_code=None,
            use_fixture=args.fixture,
        )
    else:
        cleaned_data = clean_data(
            raw_data,
            country_code=args.country,
            use_fixture=args.fixture,
        )
    
    # If no data is found
    if cleaned_data.empty:
        target = 'ALL' if args.all else args.country.upper()
        raise ValueError(f"No data found for '{target}'.")
    
    # save and report
    if args.all:
        save_path = save_data(
            cleaned_data,
            country_code='ALL',
            use_fixture=args.fixture,
        )
    else:
        save_path = save_data(
            cleaned_data,
            country_code=args.country,
            use_fixture=args.fixture,
        )
    print(f"Location of the file: {save_path}")

    return cleaned_data

if __name__ == "__main__":
    main()

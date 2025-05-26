"""
This module cleans the raw life expectancy dataset and converts it into a dataset 
for Portugal by default. You can also specify a different country for the dataset.
"""

import os
import argparse
import pandas as pd

def load_data():
    """
    Loads the raw life expectancy data from the .tsv file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    
file_path = os.path.join(
    project_dir,
    'life_expectancy',
    'data',
    'eu_life_expectancy_raw.tsv')

life_expectancy_df = pd.read_csv(file_path, sep='\t')
return life_expectancy_df


def clean_data(life_expectancy_df: pd.DataFrame, country_code: str = 'PT') -> pd.DataFrame:
    """
    Cleans and processes the raw life expectancy data.
    """
    life_expectancy_df.columns = life_expectancy_df.columns.str.replace(' ', '')

    life_expectancy_df[['unit', 'sex', 'age', 'region']] = (
        life_expectancy_df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    )
    life_expectancy_df = life_expectancy_df.drop('unit,sex,age,geo\\time', axis=1)
    life_expectancy_df = life_expectancy_df[life_expectancy_df['region'] == country_code]

    life_expectancy_df_melted = pd.melt(
        life_expectancy_df,
        id_vars=['unit', 'sex', 'age', 'region'],
        var_name='year',
        value_name='value'
    ).query('value != ": "')

    life_expectancy_df_melted['value'] = pd.to_numeric(
        life_expectancy_df_melted['value'].str.replace(r'[^0-9.^0-9]', '', regex=True),
        errors='coerce'
    )
    life_expectancy_df_melted['year'] = life_expectancy_df_melted['year'].astype(int)

    return life_expectancy_df_melted


def save_data(life_expectancy_df: pd.DataFrame, country_code: str = 'PT'):
    """
    Saves the cleaned data to a CSV file.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)
    output_file_path = os.path.join(
        project_dir,
        'life_expectancy',
        'data',
        f'{country_code}_life_expectancy.csv'
    )
    life_expectancy_df.to_csv(output_file_path, index=False)


def main():
    """
    Main function for cleaning life expectancy data.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--country', default='PT')
    args = parser.parse_args()

    raw_data = load_data()
    cleaned_data = clean_data(raw_data, country_code=args.country)
    save_data(cleaned_data, country_code=args.country)


if __name__ == '__main__':  # pragma: no cover
    main()

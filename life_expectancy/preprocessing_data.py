import pandas as pd
from typing import Optional

from life_expectancy.loading_data import load_data

def clean_data(
    life_expectancy_df: Optional[pd.DataFrame] = None,
    *,
    country_code: Optional[str] = None,
    use_fixture: bool = False,
) -> pd.DataFrame:
    """
    Cleans and processes the raw life-expectancy data.
    If life_expectancy_df is None, loads it via load_data().
    """
    # get data if it wasn't provided
    if life_expectancy_df is None:
        life_expectancy_df = load_data(use_fixture=use_fixture)
    else:
        life_expectancy_df=life_expectancy_df.copy()

    # unpivot variable to long format
    life_expectancy_df.columns = life_expectancy_df.columns.str.replace(' ', '', regex=False)
    life_expectancy_df[['unit', 'sex', 'age', 'region']] = (
        life_expectancy_df['unit,sex,age,geo\\time'].str.split(',', expand=True)
    )
    life_expectancy_df = life_expectancy_df.drop('unit,sex,age,geo\\time', axis=1)
    
    # filter by country if country_code exists
    if country_code is not None:
        country_code = country_code.upper()
        life_expectancy_df = life_expectancy_df[
            life_expectancy_df['region'] == country_code
            ]
    
    # create year and value variables
    life_expectancy_df = (
        life_expectancy_df
        .melt(
            id_vars=['unit', 'sex', 'age', 'region'],
            var_name='year',
            value_name='value',
        )
        .loc[lambda df_: df_['value'].str.strip() != ':']
    )
    
    # assure value is a float
    life_expectancy_df['value'] = pd.to_numeric(
        life_expectancy_df['value'].str.replace(r'[^0-9.]', '', regex=True),
        errors='coerce',
    )

    # assure year is an integer
    life_expectancy_df['year'] = life_expectancy_df['year'].astype(int)
    return life_expectancy_df
import pandas as pd
from typing import Optional, Union

from life_expectancy.loading_data import load_data
from life_expectancy.region import Region

# Saving all country members if necessary
_ALL_COUNTRY_CODES = {m.value for m in Region.country_members()}

def clean_data(
    life_expectancy_df: Optional[pd.DataFrame] = None,
    *,
    country_code: Optional[Union[str, Region]] = None,
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
        if isinstance(country_code, Region):
            country_code = country_code.value
        country_code = country_code.upper()

        if country_code not in _ALL_COUNTRY_CODES:
            raise ValueError(f"'{country_code}' is not a valid country code.")
        
        life_expectancy_df = life_expectancy_df[
            life_expectancy_df['region'] == country_code
            ]
    else:
        life_expectancy_df = life_expectancy_df[
            life_expectancy_df['region'].isin(_ALL_COUNTRY_CODES)
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
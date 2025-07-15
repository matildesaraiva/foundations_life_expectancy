import os
import pandas as pd
from typing import Optional, Union

from life_expectancy.region import Region

def save_data(
    life_expectancy_df: pd.DataFrame,
    *,
    country_code: Union[str, Region] = 'PT',
    base_dir: Optional[str] = None,
    use_fixture: bool = False,
) -> str:
    """
    Save life_expectancy_df to CSV.
    """

    if isinstance(country_code, Region):
        country_code_str = country_code.value
    else:
        country_code_str = None if country_code is None else str(country_code).upper()
    

    script_dir  = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    if base_dir is None:
        base_dir = (
            os.path.join(
                project_dir,
                'life_expectancy',
                'tests',
                'fixtures'
                )
            if use_fixture
            else os.path.join(
                project_dir,
                'life_expectancy',
                'data'
                )
        )
    os.makedirs(base_dir, exist_ok=True)

    filename = (
        'eu_life_expectancy_expected.csv'
        if country_code_str in (None, 'ALL')
        else f'{country_code_str}_life_expectancy.csv'
    )

    output_path = os.path.join(base_dir, filename)
    life_expectancy_df.to_csv(output_path, index=False)
    return output_path

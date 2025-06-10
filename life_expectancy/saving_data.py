import os
import pandas as pd
from typing import Optional

def save_data(
    life_expectancy_df: pd.DataFrame,
    *,
    country_code: str = "PT",
    base_dir: Optional[str] = None,
) -> str:
    """
    Save life_expectancy_df to CSV.
    """
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    if base_dir is None:
        base_dir = os.path.join(project_dir, "life_expectancy", "data")
    os.makedirs(base_dir, exist_ok=True)

    if country_code in (None, "ALL"):
        filename = "eu_life_expectancy_expected.csv"
    else:
        filename = f"{country_code}_life_expectancy.csv"

    output_path = os.path.join(base_dir, filename)
    life_expectancy_df.to_csv(output_path, index=False)
    return output_path

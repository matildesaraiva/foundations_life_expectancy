"""Testing 'saving_data' module"""

from unittest.mock import patch
import pandas as pd

from life_expectancy.saving_data import save_data
from life_expectancy.region import Region

def test_save_data_calls_to_csv(eu_life_expectancy_raw, tmp_path):
    """
    Testing if 'save_data' function calls dataframe.to_csv when saving.
    """
    df = eu_life_expectancy_raw
    with patch.object(pd.DataFrame, "to_csv") as mock_to_csv:
        save_data(
            df,
            country_code=Region.PT,
            base_dir=str(tmp_path),
            use_fixture=False,
        )
        
        # Checking if the method was called
        mock_to_csv.assert_called_once()

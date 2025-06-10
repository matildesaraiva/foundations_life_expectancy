"""Testing 'saving_data' module"""

from unittest.mock import patch
import pandas as pd

from life_expectancy.saving_data import save_data

def test_save_data_calls_to_csv(eu_life_expectancy_raw, tmp_path):
    """
    Testing if 'save_data' function makes a 'to_csv' call.
    """
    # patch DataFrame.to_csv to assure no file is written
    with patch.object(pd.DataFrame, "to_csv") as mock_to_csv:
        save_data(eu_life_expectancy_raw, country_code="PT", base_dir=tmp_path)
        
        # Checking if the method was called
        mock_to_csv.assert_called_once()

import os
import pandas as pd

def load_data(base_dir=None, use_fixture: bool = False) -> pd.DataFrame:
    """
    Loads the raw life expectancy data from the .tsv file.
    If use_fixture is True, loads the test fixture version.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    if base_dir is None:
        base_dir = 'life_expectancy/tests/fixtures' if use_fixture else 'life_expectancy/data'

    file_path = os.path.join(project_dir, base_dir, 'eu_life_expectancy_raw.tsv')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")

    return pd.read_csv(file_path, sep='\t')

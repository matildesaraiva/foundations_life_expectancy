import os
import pandas as pd

from life_expectancy.loader_factory_pattern import get_loader

def load_data(base_dir=None, use_fixture: bool = False) -> pd.DataFrame:
    """
    Loads the raw life expectancy data from a data file.
    If use_fixture is True, loads the test fixture version.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_dir = os.path.dirname(script_dir)

    if base_dir is None:
        base_dir = (
            'life_expectancy/tests/fixtures'
            if use_fixture
            else 'life_expectancy/data'
        )

    file_path = os.path.join(project_dir, base_dir, 'eurostat_life_expect.zip')

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found at: {file_path}")

    return get_loader(file_path).load_data()

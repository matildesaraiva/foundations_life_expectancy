import pandas as pd
from life_expectancy.cleaning import clean_data

# Loading the original "eu_life_expectancy_raw" dataset
eu_life_expectancy_df = pd.read_csv(
    "data/eu_life_expectancy_raw.tsv",
    sep="\t"
    )

# Extracting country codes from variable 'unit,sex,age,geo\time'
eu_life_expectancy_df['country'] = eu_life_expectancy_df['unit,sex,age,geo\\time'].apply(lambda x: x.split(',')[-1])

# Filtering unique rows by variable 'country'
fixture_input = eu_life_expectancy_df.drop_duplicates(subset=['country']).reset_index(drop=True)

# Removing variable 'country'
fixture_input = fixture_input.drop(columns=['country'])

# Saving sample eu_life_expectancy_raw dataset into fixtures folder
fixture_input.to_csv(
    "tests/fixtures/eu_life_expectancy_raw.tsv", 
    sep="\t",
    index=False
    )

# Creating the fixture for the expected result
df_expected = clean_data(fixture_input)

# Saving the eu_life_expectancy_expected dataset into fixtures folder
df_expected.to_csv("tests/fixtures/eu_life_expectancy_expected.csv", index=False)
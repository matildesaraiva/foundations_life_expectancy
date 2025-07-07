from life_expectancy.region import Region

def test_country_members():
    """
    Testing if grouped regions are leaked into 'country_members'.
    """
    grouped_members = {
        "DE_TOT", "EA18", "EA19", "EEA30_2007", "EEA31",
        "EFTA", "EU27_2007", "EU27_2020", "EU28",
    }
    codes = {m.value for m in Region.country_members()}
    assert codes.isdisjoint(grouped_members), "Grouped regions found in country list"

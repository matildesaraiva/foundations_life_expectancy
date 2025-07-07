"""
1) Extracts a list of regions that appear in the life-expectancy dataset.
2) Creates a Enum with the Region codes.
2) Class method that returns the enums of all the actual countries 

Note: It can be ran as a script to print the region codes.
"""

import sys
from enum import Enum
from typing import List

from life_expectancy.loading_data import load_data

def get_enum_regions(
    use_fixture: bool = False,
    col: str = "unit,sex,age,geo\\time",
    split_index: int = 3,
) -> List[str]:
    """
    1) Loads the entire dataset;
    2) Splits "unit,sex,age,geo\\time";
    3) Returns a list of unique regions.
    """
    df = load_data(use_fixture=use_fixture)
    return (
        df[col]
          .str.split(",", expand=True)[split_index]
          .unique()
          .tolist()
    )

if __name__ == "__main__":
    regions = get_enum_regions(use_fixture="--fixture" in sys.argv)
    print("\n".join(regions))


class Region(Enum):
    """
    All region codes observed in the dataset.
    """
    AL = 'AL';
    AM = 'AM';
    AT = 'AT';
    AZ = 'AZ';
    BE = 'BE';
    BG = 'BG';
    BY = 'BY';
    CH = 'CH';
    CY = 'CY';
    CZ = 'CZ';
    DE = 'DE';
    DE_TOT ='DE_TOT';
    DK = 'DK';
    EA18 = 'EA18';
    EA19 = 'EA19';
    EE = 'EE';
    EEA30_2007 = 'EEA30_2007';
    EEA31 = 'EEA31';
    EFTA = 'EFTA';
    EL = 'EL';
    ES = 'ES';
    EU27_2007 = 'EU27_2007';
    EU27_2020 = 'EU27_2020';
    EU28 = 'EU28';
    FI = 'FI';
    FR = 'FR';
    FX = 'FX';
    GE = 'GE';
    HR = 'HR';
    HU = 'HU';
    IE = 'IE';
    IS = 'IS';
    IT = 'IT';
    LI = 'LI';
    LT = 'LT';
    LU = 'LU';
    LV = 'LV';
    MD = 'MD';
    ME = 'ME';
    MK = 'MK';
    MT = 'MT';
    NL = 'NL';
    NO = 'NO';
    PL = 'PL';
    PT = 'PT';
    RO = 'RO';
    RS = 'RS';
    RU = 'RU';
    SE = 'SE';
    SI = 'SI';
    SK = 'SK';
    SM = 'SM';
    TR = 'TR';
    UA = 'UA';
    UK = 'UK';
    XK = 'XK'



    @classmethod
    def country_members(cls) -> list["Region"]:
        """
        Returns valid country code enums that represent single countries
        """
        return [m for m in cls if m.name not in _GROUPED_REGIONS]
        
_GROUPED_REGIONS: set[str] = {
    "DE_TOT",
    "EA18",
    "EA19",
    "EEA30_2007",
    "EEA31",
    "EFTA",
    "EU27_2007",
    "EU27_2020",
    "EU28",
}
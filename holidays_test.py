from czech_holidays import Holidays
# Inspection data - http://kalendar.beda.cz

PATTERN_EASTER = ["2016-03-25", "2017-04-14",
                  "2018-03-30", "2019-04-19",
                  "2020-04-10", "2021-04-02",
                  "2022-04-15", "2023-04-07",
                  "2024-03-29", "2025-04-18",
                  "2026-04-03", "2027-03-26",
                  "2028-04-14", "2029-03-30"]

# Range of years, for example
FIRST_YEAR = 2016
LAST_YEAR = 2030


def test():
    index = 0
    for year in range(FIRST_YEAR, LAST_YEAR):
        holidays = Holidays(year)
#  first holiday is always 1 January
        assert str(holidays[0]) == str(year) + "-01-01"
#  Good Friday tests (controlling movable holidays)
        assert str(holidays[3]) == PATTERN_EASTER[index]
        index += 1
    




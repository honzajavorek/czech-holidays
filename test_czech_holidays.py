import re
from datetime import date

import pytest

from czech_holidays import czech_christmas, czech_easter, czech_holidays


@pytest.mark.parametrize('year, easter_date', [
    (2021, date(2021, 4, 5)),
    (2022, date(2022, 4, 18)),
    (2023, date(2023, 4, 10)),
    (2027, date(2027, 3, 29)),
])
def test_easter(year, easter_date):
    assert czech_easter(year).date == easter_date


def test_christmas():
    assert czech_christmas(2022).date == date(2022, 12, 24)


def test_czech_holidays_wont_work_for_historical_dates():
    with pytest.raises(NotImplementedError):
        czech_holidays(2015)

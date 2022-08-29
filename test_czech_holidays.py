import re
from datetime import date

import pytest

from czech_holidays import holidays, Holidays, Holiday


@pytest.mark.parametrize('easter_date', [
    date(2021, 4, 5),
    date(2022, 4, 18),
    date(2023, 4, 10),
    date(2024, 3, 31),
])
def test_easter(easter_date):
    holiday = Holidays(easter_date.year).easter
    assert (holiday.year, holiday.month, holiday.day) == (easter_date.year, easter_date.month, easter_date.day)


def test_christmas():
    holiday = Holidays(2022).christmas
    assert (holiday.year, holiday.month, holiday.day) == (2022, 12, 24)

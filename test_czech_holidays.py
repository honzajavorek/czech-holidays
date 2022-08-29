import re
from datetime import date

import requests
import pytest

from czech_holidays import holidays, Holidays, Holiday


WIKIPEDIA_RE = re.compile(r'Rok\s\d{4}</th>\s<td>(?P<date>\w+)')

WIKIPEDIA_DATE_RE = re.compile(r'(?P<day>\d+)\.\s+(?P<month>\w+)\s+(?P<year>\d{4})')


def fetch_easter_dates():
    response = requests.get('https://cs.wikipedia.org/wiki/Velikono%C4%8Dn%C3%AD_pond%C4%9Bl%C3%AD')
    response.raise_for_status()
    return [parse_wikipedia_date(match.group('date'))
            for match in WIKIPEDIA_RE.finditer(response.text)]


def parse_wikipedia_date(date_text):
    match = WIKIPEDIA_DATE_RE.search(date_text)
    groups = match.groupdict()
    return date(int(groups['year']),
                3 if 'bře' in groups['month'] else 4,
                int(groups['day']))


@pytest.mark.parametrize('date_text, expected', [
    ('5. dubna 2021', date(2021, 4, 5)),
    ('18. dubna 2022', date(2022, 4, 18)),
    ('10. dubna 2023', date(2023, 4, 10)),
    ('31. března 2024', date(2024, 3, 31)),
])
def test_parse_wikipedia_date(date_text, expected):
    assert parse_wikipedia_date(date_text) == expected


@pytest.mark.parametrize('easter_date', fetch_easter_dates())
def test_easter(easter_date):
    holiday = Holidays(easter_date.year).easter
    assert (holiday.year, holiday.month, holiday.day) == (easter_date.year, easter_date.month, easter_date.day)


def test_christmas():
    holiday = Holidays(2022).christmas
    assert (holiday.year, holiday.month, holiday.day) == (2022, 12, 24)

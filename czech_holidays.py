from collections import namedtuple

from datetime import date, timedelta
from dateutil.easter import easter as calculate_easter


__all__ = ('Holiday', 'czech_holidays', 'czech_easter', 'czech_christmas')


LAST_LEGISLATIVE_CHANGE = 2016


Holiday = namedtuple('Holiday', 'date, name, name_en')


def czech_easter(year):
    return Holiday(
        calculate_easter(year) + timedelta(days=1),
        "Velikonoční pondělí",
        "Easter Monday",
    )


def czech_christmas(year):
    return Holiday(
        date(year, 12, 24),
        "Štědrý den",
        "Christmas Eve",
    )


def czech_holidays(year):
    if year < LAST_LEGISLATIVE_CHANGE:
        raise NotImplementedError(f"Unable to generate data for years prior to {LAST_LEGISLATIVE_CHANGE} (last legislative change to the list of Czech public holidays)")

    easter = czech_easter(year)
    christmas = czech_christmas(year)

    return [
        Holiday(
            date(year, 1, 1),
            "Nový rok",
            "New Year's Day",
        ),
        Holiday(
            date(year, 1, 1),
            "Den obnovy samostatného českého státu",
            "Restoration Day of the Independent Czech State",
        ),
        easter,
        Holiday(
            easter.date - timedelta(days=3),
            "Velký pátek",
            "Good Friday",
        ),
        Holiday(
            date(year, 5, 1),
            "Svátek práce",
            "Labour Day",
        ),
        Holiday(
            date(year, 5, 8),
            "Den vítězství",
            "Liberation Day",
        ),
        Holiday(
            date(year, 7, 5),
            "Den slovanských věrozvěstů Cyrila a Metoděje",
            "Saints Cyril and Methodius Day",
        ),
        Holiday(
            date(year, 7, 6),
            "Den upálení mistra Jana Husa",
            "Jan Hus Day",
        ),
        Holiday(
            date(year, 9, 28),
            "Den české státnosti",
            "St. Wenceslas Day (Czech Statehood Day)",
        ),
        Holiday(
            date(year, 10, 28),
            "Den vzniku samostatného československého státu",
            "Independent Czechoslovak State Day",
        ),
        Holiday(
            date(year, 11, 17),
            "Den boje za svobodu a demokracii",
            "Struggle for Freedom and Democracy Day",
        ),
        christmas,
        Holiday(
            christmas.date + timedelta(days=1),
            "1. svátek vánoční",
            "Christmas Day",
        ),
        Holiday(
            christmas.date + timedelta(days=2),
            "2. svátek vánoční",
            "St. Stephen's Day (The Second Christmas Day)",
        ),
    ]

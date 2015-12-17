# -*- coding: utf-8 -*-


from __future__ import unicode_literals


__title__ = 'czech-holidays'
__version__ = '0.1.0'
__author__ = 'Honza Javorek'
__license__ = 'MIT'
__copyright__ = 'Copyright 2013 Honza Javorek'


from datetime import date, timedelta
from dateutil.easter import easter as calculate_easter


__all__ = ('Holiday', 'Holidays', 'holidays')


class Holiday(date):

    def __new__(cls, year, month, day, name, name_en):
        obj = date.__new__(cls, year, month, day)
        obj.name = name
        obj.name_en = name_en
        return obj


class Holidays(list):

    def __init__(self, year=None):
        year = year or date.today().year
        easter = calculate_easter(year) + timedelta(1)

        self.extend((
            Holiday(
                year, 1, 1,
                "Nový rok",
                "New Year's Day",
            ),
            Holiday(
                year, 1, 1,
                "Den obnovy samostatného českého státu",
                "Restoration Day of the Independent Czech State",
            ),
            Holiday(
                easter.year, easter.month, easter.day,
                "Velikonoční pondělí",
                "Easter Monday",
            ),
            Holiday(
                easter.year, easter.month, easter.day - 3,
                "Velký pátek",
                "Good Friday",
            ),
            Holiday(
                year, 5, 1,
                "Svátek práce",
                "Labour Day",
            ),
            Holiday(
                year, 5, 8,
                "Den vítězství",
                "Liberation Day",
            ),
            Holiday(
                year, 7, 5,
                "Den slovanských věrozvěstů Cyrila a Metoděje",
                "Saints Cyril and Methodius Day",
            ),
            Holiday(
                year, 7, 6,
                "Den upálení mistra Jana Husa",
                "Jan Hus Day",
            ),
            Holiday(
                year, 9, 28,
                "Den české státnosti",
                "St. Wenceslas Day (Czech Statehood Day)",
            ),
            Holiday(
                year, 10, 28,
                "Den vzniku samostatného československého státu",
                "Independent Czechoslovak State Day",
            ),
            Holiday(
                year, 11, 17,
                "Den boje za svobodu a demokracii",
                "Struggle for Freedom and Democracy Day",
            ),
            Holiday(
                year, 12, 24,
                "Štědrý den",
                "Christmas Eve",
            ),
            Holiday(
                year, 12, 25,
                "1. svátek vánoční",
                "Christmas Day",
            ),
            Holiday(
                year, 12, 26,
                "2. svátek vánoční",
                "St. Stephen's Day (The Second Christmas Day)",
            ),
        ))

        self.easter = self[2]
        self.christmas = self[10]


holidays = Holidays()

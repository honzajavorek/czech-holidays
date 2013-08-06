# -*- coding: utf-8 -*-


__title__ = 'czech-holidays'
__version__ = '0.0.2'
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
                u"Nový rok",
                u"New Year's Day",
            ),
            Holiday(
                year, 1, 1,
                u"Den obnovy samostatného českého státu",
                u"Restoration Day of the Independent Czech State",
            ),
            Holiday(
                easter.year, easter.month, easter.day,
                u"Velikonoční pondělí",
                u"Easter Monday",
            ),
            Holiday(
                year, 5, 1,
                u"Svátek práce",
                u"Labour Day",
            ),
            Holiday(
                year, 5, 8,
                u"Den vítězství",
                u"Liberation Day",
            ),
            Holiday(
                year, 7, 5,
                u"Den slovanských věrozvěstů Cyrila a Metoděje",
                u"Saints Cyril and Methodius Day",
            ),
            Holiday(
                year, 7, 6,
                u"Den upálení mistra Jana Husa",
                u"Jan Hus Day",
            ),
            Holiday(
                year, 9, 28,
                u"Den české státnosti",
                u"St. Wenceslas Day (Czech Statehood Day)",
            ),
            Holiday(
                year, 10, 28,
                u"Den vzniku samostatného československého státu",
                u"Independent Czechoslovak State Day",
            ),
            Holiday(
                year, 11, 17,
                u"Den boje za svobodu a demokracii",
                u"Struggle for Freedom and Democracy Day",
            ),
            Holiday(
                year, 12, 24,
                u"Štědrý den",
                u"Christmas Eve",
            ),
            Holiday(
                year, 12, 25,
                u"1. svátek vánoční",
                u"Christmas Day",
            ),
            Holiday(
                year, 12, 26,
                u"2. svátek vánoční",
                u"St. Stephen's Day (The Second Christmas Day)",
            ),
        ))

        self.easter = self[2]
        self.christmas = self[10]


holidays = Holidays()

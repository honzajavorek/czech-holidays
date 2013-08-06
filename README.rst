
Czech Holidays
==============

Python package with `Czech public holidays <https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic>`_.

Status: ACTIVE
--------------

Under active development and maintenance.

Installation
------------

The Cheese Shop::

    pip install czech-holidays

In case you have an adventurous mind, give a try to the source::

    pip install git+https://github.com/honzajavorek/czech-holidays.git#egg=czech-holidays

Examples
--------

Czech Holidays provide simple interface:

.. code:: python

    >>> from czech_holidays import holidays
    >>> holidays
    [Holiday(2013, 1, 1), Holiday(2013, 1, 1), Holiday(2013, 4, 1), Holiday(2013, 5, 1), Holiday(2013, 5, 8), Holiday(2013, 7, 5), Holiday(2013, 7, 6), Holiday(2013, 9, 28), Holiday(2013, 10, 28), Holiday(2013, 11, 17), Holiday(2013, 12, 24), Holiday(2013, 12, 25), Holiday(2013, 12, 26)]

Two shortcuts are available:

.. code:: python

    >>> holidays.easter
    Holiday(2013, 4, 1)
    >>> holidays.christmas
    Holiday(2013, 12, 24)

Otherwise ``holidays`` behaves as an ordinary ``list``. If you need holidays
for different year, you can make your own ``Holidays`` object:

.. code:: python

    >>> from czech_holidays import Holidays
    >>> holidays = Holidays(2020)
    >>> holidays.easter
    Holiday(2020, 4, 13)

``Holiday`` object behaves as an ordinary ``datetime.date`` object:

.. code:: python

    >>> from czech_holidays import holidays
    >>> holiday = holidays[5]  # arbitrary holiday
    >>> holiday.day
    5
    >>> holiday.year
    2013
    >>> from datetime import timedelta
    >>> holidays[5] + timedelta(days=4)
    datetime.date(2013, 7, 9)

It also has some extra properties:

.. code:: python

    >>> holiday.name
    u'Den slovansk\xfdch v\u011brozv\u011bst\u016f Cyrila a Metod\u011bje'
    >>> holiday.name_en
    u'Saints Cyril and Methodius Day'

Aim of this library is to simplify work with Czech public holidays in current
applications, thus **it does not provide any historical data**. For example,
*Restoration Day of the Independent Czech State* is celebrated since 2000,
but the library returns it also for, let's say, 1978.

License: MIT
------------

© 2013 Jan Javorek <jan.javorek@gmail.com>

This work is licensed under `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.


Czech Holidays
==============

Python package with `Czech public holidays <https://en.wikipedia.org/wiki/Public_holidays_in_the_Czech_Republic>`_.

Installation
------------

From PyPI::

    pip install czech-holidays

In case you have an adventurous mind, give a try to the source::

    pip install git+https://github.com/honzajavorek/czech-holidays.git#egg=czech-holidays

Examples
--------

Czech Holidays provides the following interface:

.. code:: python

    >>> from czech_holidays import czech_holidays
    >>> holidays = czech_holidays(2022)
    >>> holidays[:3]
    [Holiday(date=datetime.date(2022, 1, 1), name='Nový rok', name_en="New Year's Day"),
     Holiday(date=datetime.date(2022, 1, 1), name='Den obnovy samostatného českého státu', name_en='Restoration Day of the Independent Czech State'),
     Holiday(date=datetime.date(2022, 4, 18), name='Velikonoční pondělí', name_en='Easter Monday')]

The function accepts year as a single argument and returns a list of `named tuples <https://docs.python.org/3/library/collections.html#collections.namedtuple>`_:

.. code:: python

    >>> holidays[0].date
    datetime.date(2022, 1, 1)
    >>> holidays[0].name
    'Nový rok'
    >>> holidays[0].name_en
    "New Year's Day"

Albeit named, it's still just a tuple:

.. code:: python

    >>> holidays[0][0]
    datetime.date(2022, 1, 1)
    >>> holidays[0][1]
    'Nový rok'
    >>> holidays[0][2]
    "New Year's Day"
    >>> tuple(holidays[0])
    (datetime.date(2022, 1, 1), 'Nový rok', "New Year's Day")
    >>> holidays[0] < holidays[5]
    True

Two shortcuts are available:

.. code:: python

    >>> from czech_holidays import czech_easter, czech_christmas
    >>> czech_easter(2022)
    Holiday(date=datetime.date(2022, 4, 18), name='Velikonoční pondělí', name_en='Easter Monday')
    >>> czech_christmas(2022)
    Holiday(date=datetime.date(2022, 12, 24), name='Štědrý den', name_en='Christmas Eve')

The aim of this library is to simplify work with Czech public holidays in current
applications, thus **it does not provide any historical data**:

.. code:: python

    >>> czech_holidays(2013)
    Traceback (most recent call last):
    NotImplementedError: ...

Development
-----------

Install using `poetry <https://python-poetry.org/>`_::

    git clone git@github.com:honzajavorek/czech-holidays.git
    cd czech-holidays
    poetry install

Then run tests::

    pytest

License: MIT
------------

© 2022 Honza Javorek <mail@honzajavorek.cz>

This work is licensed under `MIT license <https://en.wikipedia.org/wiki/MIT_License>`_.

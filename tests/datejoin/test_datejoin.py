import DateTimeTools as dt


def test_datejoin():
    """
    join year month and day to date
    """

    date = dt.DateJoin(2001, 12, 1)

    assert date == 20011201

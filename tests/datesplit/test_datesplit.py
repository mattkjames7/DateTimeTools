import DateTimeTools as dt

def test_datesplit():
    """
    Test splitting date into year, month, day
    """

    year, month, day = dt.DateSplit(20010503)

    assert year == 2001
    assert month == 5
    assert day == 3

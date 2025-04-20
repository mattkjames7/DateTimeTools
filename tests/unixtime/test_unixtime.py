import DateTimeTools as dt


def test_datetounixtime():
    """
    convert date and time to unixtime
    """

    result = dt.UnixTime(20010405, 19.0)

    assert result == 986497200.0


def test_unixtimetodate():
    """
    convert unix time to date and time
    """

    date, ut = dt.UnixTimetoDate(986497200.0)

    assert date == 20010405
    assert ut == 19.0

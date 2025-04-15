import DateTimeTools as dt


def test_timedifference():
    """
    calculate the time difference between two date/times
    """

    result = dt.TimeDifference(20010324, 3.0, 20020324, 12.0)

    assert result == 365.375

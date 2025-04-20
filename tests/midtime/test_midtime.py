import DateTimeTools as dt


def test_midtime():
    """
    Calculate middle date and time between two date/times
    """

    date, ut = dt.MidTime(20010324, 3.0, 20020324, 12.0)

    assert date == 20010922
    assert ut == 19.5

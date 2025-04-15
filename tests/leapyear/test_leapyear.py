import DateTimeTools as dt


def test_leapyear():
    """
    test the leap year function
    """

    result = dt.LeapYear(2001)

    assert not result

    result = dt.LeapYear(2004)

    assert result

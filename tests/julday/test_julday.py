import DateTimeTools as dt


def test_datetojulday():
    """
    convert date to julian day
    """

    date, ut = dt.JulDaytoDate(2413370.0)

    assert date == 18950625
    assert ut == 12.0


def test_juldaytodate():
    """
    convert julian day to date
    """

    result = dt.JulDay(20041230, 12.0)

    assert result == 2453370.0

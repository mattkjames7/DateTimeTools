import DateTimeTools as dt


def test_datetocontut():
    """
    convert date + time in hours to number of hours since 1950
    """

    utc = dt.ContUT(19960923, 17.5)

    assert utc[0] == 409625.5


def test_contuttodate():
    """
    convert cont ut bck to date and time
    """

    date, ut = dt.ContUTtoDate(0.0)

    assert date[0] == 19500101
    assert ut[0] == 0.0

    date, ut = dt.ContUTtoDate(438288.0)

    assert date[0] == 20000101
    assert ut[0] == 0.0

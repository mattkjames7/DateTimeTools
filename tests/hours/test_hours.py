import DateTimeTools as dt


def test_hourstohhmm():
    """
    test converting hours to hhmm
    """

    hh, mm, ss, ms = dt.DectoHHMM(22.25)

    assert hh == 22
    assert mm == 15
    assert ss == 0
    assert ms == 0.0


def test_hhmmtohours():
    """
    reverse of the above
    """

    ut = dt.HHMMtoDec(22, 15, 0, 0)

    assert ut == 22.25

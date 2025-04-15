import DateTimeTools as dt


def test_plusday():
    """
    test subtracting a day from a date
    """
    result = dt.PlusDay(20040228)
    assert result == 20040229

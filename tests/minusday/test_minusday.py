import DateTimeTools as dt


def test_minusday():
    """
    test subtracting a day from a date
    """
    result = dt.MinusDay(20040301)
    assert result == 20040229

import DateTimeTools as dt


def test_datediff():
    """
    calculate the difference between two dates in days
    """

    diff = dt.DateDifference(19950101, 20220324)

    assert diff == 9944

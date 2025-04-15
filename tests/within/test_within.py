import DateTimeTools as dt


def test_within():
    """
    find indices of times within a range
    """

    inds = dt.WithinTimeRange(
        (
            [20010101, 20010101, 20010103, 20010104, 20010105],
            [12.0, 23.0, 15.0, 4.0, 12.0]
        ),
        (20010102, 12.0),
        (20010105, 6.0)
    )

    assert inds.tolist() == [2, 3]

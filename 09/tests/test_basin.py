import basin

data = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_basin():
    assert basin.basin(data, roots_only=True) == 15


def test_basin_sizes_only():
    assert basin.basin(data, sizes_only=True) == [3, 9, 9, 14]


def test_basin_sizes():
    assert basin.basin(data) == 1134

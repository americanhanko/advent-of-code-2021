import vents
from vents import Line

data = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_creating_horizontal_line_from_two_points():
    points = [(0, 9), (5, 9)]
    line = Line(points)

    assert line.points() == [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]


def test_creating_vertical_line_from_two_points():
    points = [(9, 0), (9, 5)]
    line = Line(points)

    assert line.points() == [(9, 0), (9, 1), (9, 2), (9, 3), (9, 4), (9, 5)]


def test_creating_decreasing_diagonal_line():
    points = [(1, 1), (3, 3)]
    line = Line(points)

    answer = [(1, 1), (2, 2), (3, 3)]

    assert line.points() == answer


def test_creating_increasing_diagonal_line():
    points = [(9, 7), (7, 9)]
    line = Line(points)

    answer = [(9, 7), (8, 8), (7, 9)]

    assert line.points() == answer


def test_number_of_danger_zones():
    assert vents.danger_zones(data) == 5


def test_number_of_danger_zones_with_diags():
    assert vents.danger_zones(data, diagonals=True) == 12

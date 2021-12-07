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


def test_number_of_danger_zones():
    assert vents.danger_zones(data) == 5

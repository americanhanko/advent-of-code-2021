from collections import Counter
from typing import List
from typing import Tuple


class Line:
    """Represents a two-dimensional line"""

    def __init__(self, coords: List[Tuple[int, ...]]):
        self.coords = coords
        self.flipped = list(zip(*coords))
        self.start = None
        self.end = None

    @property
    def is_vertical(self) -> bool:
        return self._check_direction(0)

    @property
    def is_horizontal(self) -> bool:
        return self._check_direction(1)

    @property
    def is_straight(self) -> bool:
        return self.is_vertical or self.is_horizontal

    @property
    def is_diagonal(self) -> bool:
        f = self.flipped
        x = f[0]
        y = f[1]
        x1 = x[0]
        x2 = x[1]
        y1 = y[0]
        y2 = y[1]
        xs = sum([x1, (x2 * -1)])
        ys = sum([y1, (y2 * -1)])
        return abs(xs) == abs(ys)

    def points(self) -> List[Tuple[int, int]]:
        if self.is_straight:
            i, j = (1, 0) if self.is_vertical else (0, 1)
            start, end = sorted(self.flipped[i])
            axis = set(self.flipped[j]).pop()
            return [(axis, p) if self.is_vertical else (p, axis) for p in range(start, end + 1)]
        if self.is_diagonal:
            x1, y1 = self.coords[0]
            x2, y2 = self.coords[1]
            x_step = -1 if sum([x1, x2 * -1]) > 1 else 1
            y_step = -1 if sum([y1, y2 * -1]) > 1 else 1
            return list(zip(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)))

    def _check_direction(self, i) -> bool:
        return len(set(self.flipped[i])) == 1


def all_coordinates(pairs, diagonals=False):
    coordinates = []
    for pair in pairs:
        line = Line(pair)
        if line.is_straight:
            coordinates += line.points()
        if diagonals and line.is_diagonal:
            coordinates += line.points()

    return coordinates


def danger_zones(data, diagonals=False):
    lines = data.strip().split("\n")
    pairs = [[tuple(int(i) for i in p.split(",")) for p in ln.split(" -> ")] for ln in lines]
    coordinates = all_coordinates(pairs, diagonals=diagonals)
    overlaps = Counter(coordinates).values()
    result = Counter(overlaps)
    result.pop(1)
    return sum(result.values())


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    pt_one = danger_zones(content)
    pt_two = danger_zones(content, diagonals=True)
    print(pt_one, pt_two)

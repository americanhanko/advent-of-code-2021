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

    def points(self) -> List[Tuple[int, int]]:
        i, j = (1, 0) if self.is_vertical else (0, 1)
        start, end = sorted(self.flipped[i])
        axis = set(self.flipped[j]).pop()
        return [(axis, p) if self.is_vertical else (p, axis) for p in range(start, end + 1)]

    def _check_direction(self, i) -> bool:
        return len(set(self.flipped[i])) == 1


def all_coordinates(pairs):
    coordinates = []
    for pair in pairs:
        line = Line(pair)
        if line.is_straight:
            coordinates += line.points()

    return coordinates


def danger_zones(data):
    lines = data.strip().split("\n")
    pairs = [[tuple(int(i) for i in p.split(",")) for p in ln.split(" -> ")] for ln in lines]
    coordinates = all_coordinates(pairs)
    overlaps = Counter(coordinates).values()
    result = Counter(overlaps)
    result.pop(1)
    return sum(result.values())


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    print(danger_zones(content))

import itertools
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

    def _check_direction(self, i) -> bool:
        return len(set(self.flipped[i])) == 1

    @property
    def is_straight(self) -> bool:
        return self.is_vertical or self.is_horizontal

    def points(self) -> List[Tuple[int, int]]:
        if self.is_vertical:
            i, j = 1, 0
        else:
            i, j = 0, 1

        start, end = sorted(self.flipped[i])
        axis = set(self.flipped[j]).pop()
        rng = range(start, end + 1)

        if self.is_vertical:
            return [(axis, i) for i in rng]
        else:
            return [(i, axis) for i in rng]


def danger_zones(data):
    lines = data.strip().split("\n")
    pairs = [[tuple(int(i) for i in p.split(",")) for p in ln.split(" -> ")] for ln in lines]

    coordinates = []

    for pair in pairs:
        line = Line(pair)
        if line.is_straight:
            coordinates.append(line.points())

    coordinates = list(itertools.chain.from_iterable(coordinates))

    overlaps = []

    for coord in coordinates:
        if coordinates.count(coord) > 1:
            overlaps.append(coord)

    print(overlaps)
    return len(set(overlaps))

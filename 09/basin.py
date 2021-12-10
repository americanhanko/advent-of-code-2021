import math
from collections import deque


def basin(grid: str, roots_only: bool = False, sizes_only=False):
    grid = [[int(i) for i in list(d)] for d in grid.strip().split("\n")]
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    basin_roots = []
    basin_root_values = []

    for x in range(len(grid)):
        for y in range(len(grid[0])):
            this_crd = (x, y)
            this_val = grid[x][y]
            valid = True
            for d in directions:
                xn = this_crd[0] + d[0]
                yn = this_crd[1] + d[1]

                if is_safe(xn, yn, grid):
                    nbr_val = grid[xn][yn]
                    if nbr_val > this_val:
                        continue
                    else:
                        valid = False

            if valid:
                basin_roots.append(this_crd)
                basin_root_values.append(this_val)
    if roots_only:
        return sum([grid[c[0]][c[1]] + 1 for c in basin_roots])

    basin_sizes = []
    for root in basin_roots:
        queue = deque([root])
        basin_size = 1
        seen = []
        while queue:
            iterations = len(queue)
            for _ in range(iterations):
                coord = queue.popleft()
                x = coord[0]
                y = coord[1]
                this_val = grid[x][y]
                for d in directions:
                    xn = coord[0] + d[0]
                    yn = coord[1] + d[1]
                    nbr_coord = (xn, yn)

                    if is_safe(xn, yn, grid):
                        nbr_val = grid[xn][yn]
                        if nbr_coord not in seen and this_val < nbr_val < 9:
                            queue.append(nbr_coord)
                            seen.append(nbr_coord)
                            basin_size += 1

        basin_sizes.append(basin_size)

    b = sorted(basin_sizes)
    if sizes_only:
        return b

    three_largest = b[-3:]
    return math.prod(three_largest)


def is_safe(x, y, grid):
    rows = len(grid)
    columns = len(grid[0])
    return rows > x >= 0 and columns > y >= 0


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    part_one = basin(content, roots_only=True)
    part_two = basin(content)
    print(part_one, part_two)

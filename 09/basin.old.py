from collections import deque
from typing import List


def basin(grid: str):
    grid = [[int(i) for i in list(d)] for d in grid.strip().split("\n")]

    # low_points = 0
    # queue = deque()
    # directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    #
    # queue.append([0, 0])

    # for x in range(len(grid)):
    #     for y in range(len(grid[0])):
    #         coord = [x, y]
    #         val = grid[x][y]
    #
    #         for d in directions:
    #             xn = coord[0] + d[0]
    #             yn = coord[1] + d[1]
    #
    #             n_coordinate = [xn, yn]
    #             n_val = grid[xn][yn]
    #
    #             if is_safe(xn, yn, grid) and n_val < val:
    #                 queue.append(n_coordinate)
    #                 queue.remove(val)

    # while queue:
    #     iterations = len(queue)
    #     for _ in range(iterations):
    #         coord = queue.popleft()
    #         x = coord[0]
    #         y = coord[1]
    #         val = grid[x][y]
    #
    #         candidates = deque()
    #
    #         for d in directions:
    #             xn = coord[0] + d[0]
    #             yn = coord[1] + d[1]
    #
    #             n_coordinate = [xn, yn]
    #             n_val = grid[xn][yn]
    #
    #             if is_safe(xn, yn, grid) and n_val < val:
    #                 candidates.append(n_coordinate)
    #
    #         for candidate in candidates:
    #             x = candidate[0]
    #             y = candidate[1]
    #
    #             if grid[x][y] > val:
    #                 continue
    #             else:
    #                 break

    return list(queue)


def is_safe(x, y, grid):
    rows = len(grid)
    columns = len(grid[0])
    return rows > x >= 0 and columns > y >= 0


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    more = """222
212
222"""

    print(basin(more))

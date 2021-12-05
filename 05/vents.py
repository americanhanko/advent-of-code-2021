import itertools


def danger_zones(data):
    lines = data.strip().split("\n")
    # coords = [[point.split(",") for point in line.split(" -> ")] for line in lines]

    points = [
        [tuple(int(i) for i in coord.split(",")) for coord in line.split(" -> ")]
        for line in lines
    ]

    all_coords = []

    for p in points:
        if is_straight(p):
            all_coords.append(get_points(p))

    all_coords = list(itertools.chain.from_iterable(all_coords))

    return all_coords
    # overlaps = []
    #
    # for coord in all_coords:
    #     # print(coord)
    #     if all_coords.count(coord) > 1:
    #         overlaps.append(coord)
    #
    # print(overlaps)
    # return len(set(overlaps))


def is_straight(coords):
    return is_vertical(coords) or is_horizontal(coords)


def is_vertical(coords):
    return coords[0][0] == coords[1][0]


def is_horizontal(coords):
    return coords[0][1] == coords[1][1]


def get_points(coords):
    if is_horizontal(coords):
        start = min(coords[0][0], coords[1][0])
        end = max(coords[0][0], coords[1][0])
        const = coords[0][1]
        # print(start, end, const)
        return [(i, const) for i in range(start, end + 1)]
    if is_vertical(coords):
        start = min(coords[0][1], coords[1][1])
        end = max(coords[0][1], coords[1][1])
        const = coords[0][0]
        print(start, end, const)
        return [(i, const) for i in range(start, end + 1)]


def print_board(all_coords):
    for x in range(0, 10):
        print("")
        for y in range(0, 10):
            if (x, y) in all_coords:
                print("1", end="")
            else:
                print(".", end="")

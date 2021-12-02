def position(data):
    horizontal = 0
    vertical = 0

    for d in data:
        if d[0] == "forward":
            horizontal += d[1]
        if d[0] == "down":
            vertical += d[1]
        if d[0] == "up":
            vertical -= d[1]

    return horizontal * vertical

from typing import List
from typing import Tuple


def position(data: List[Tuple[str, ...]], use_aim: bool) -> int:
    horizontal = 0
    depth = 0
    aim = 0

    for d in data:
        command = d[0]
        units = int(d[1])

        if use_aim:
            if command == "forward":
                horizontal += units
                depth += units * aim
            if command == "down":
                aim += units
            if command == "up":
                aim -= units
        else:
            if command == "forward":
                horizontal += units
            if command == "down":
                depth += units
            if command == "up":
                depth -= units

    return horizontal * depth


if __name__ == "__main__":
    with open("input") as fp:
        lines = fp.readlines()
        instructions = [tuple(line.split()) for line in lines]

    result = position(instructions, use_aim=True)
    print(result)

from typing import List


def windows(data: List[int]) -> List[int]:
    count = len(data)
    winds = []
    start = 0
    end = 3

    for i in range(count):
        window = sum(data[start:end])
        start += 1
        end += 1
        winds.append(window)
        if end > count:
            break

    return winds


def sweep(data: List[int]) -> int:
    count = len(data)
    increases = 0

    for i in range(1, count):
        increases += 1 if data[i] - data[i - 1] > 0 else 0

    return increases


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.readlines()
        measurements = [int(i) for i in content]

    windows = windows(measurements)
    result = sweep(windows)
    print(result)

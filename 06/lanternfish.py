from typing import List


def growth_rate(data: List[int], days=0) -> int:
    days = days
    fish = data

    print(days)
    while days > 0:
        fish = [f - 1 for f in fish]
        days -= 1

    return growth_rate(fish, days)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    init_fish = [int(i) for i in content.split(",")]
    result = growth_rate(init_fish)
    print(result)

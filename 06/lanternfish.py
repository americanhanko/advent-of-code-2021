from collections import Counter
from typing import List


def growth_rate(fish: List[int], days) -> int:
    fish = Counter(fish)
    for i in range(days):
        new_fish = fish[0]
        for age in range(8):
            fish[age] = fish[age + 1]
        fish[6] += new_fish
        fish[8] = new_fish
    return sum(fish.values())


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    fish_data = [int(i) for i in content.split(",")]
    fewer_days = growth_rate(fish_data, days=80)
    many_days = growth_rate(fish_data, days=256)
    print(fewer_days, many_days)

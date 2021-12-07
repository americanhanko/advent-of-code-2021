from typing import List


def growth_rate(fish: List[int], days) -> int:
    if days > 0:
        next_gen = []
        for i in range(len(fish)):
            if fish[i] != 0:
                aged = fish[i] - 1
                next_gen.insert(i, aged)
            else:
                next_gen.append(8)
                next_gen.insert(i, 6)
        days -= 1
        return growth_rate(next_gen, days)
    else:
        return len(fish)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    fish_data = [int(i) for i in content.split(",")]
    result = growth_rate(fish_data, days=80)
    print(result)

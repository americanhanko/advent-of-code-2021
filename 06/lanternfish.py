def growth_rate(data, days=0) -> int:
    init_fish = data.split(",")

    days = days
    fish = init_fish

    while days:
        days -= 1

    return len(fish)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    result = growth_rate(content)
    print(result)

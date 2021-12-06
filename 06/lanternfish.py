def growth_rate(data) -> int:
    return 0


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip()

    result = growth_rate(content)
    print(result)

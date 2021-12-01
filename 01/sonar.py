def windows(data):
    count = len(data)
    windows = []
    start = 0
    end = 3

    for i in range(count):
        window = sum(data[start:end])
        start += 1
        end += 1
        windows.append(window)
        if end > count:
            break

    return windows


def sweep(data):
    count = len(data)
    increases = 0

    for i in range(1, count):
        increases += 1 if data[i] - data[i - 1] > 0 else 0

    return increases


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.readlines()
        data = [int(i) for i in content.strip()]

    windows = windows(data)
    result = sweep(windows)
    print(result)

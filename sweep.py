def sliding_windows(depths):
    depth_count = len(depths)
    sums = []
    start = 0
    end = 3

    for i in range(depth_count):
        slide = sum(depths[start:end])
        start += 1
        end += 1
        sums.append(slide)
        if end > depth_count:
            break

    return sums


def sonar_sweep(depths):
    depth_count = len(depths)
    increase_count = 0

    for i in range(depth_count):
        if i == 0:
            next
        else:
            previous_depth = int(depths[i - 1])
            this_depth = int(depths[i])
            difference = this_depth - previous_depth
            increase_count += 1 if difference > 0 else 0

    return increase_count


if __name__ == "__main__":
    with open("input") as fp:
        string_depths = fp.read().strip().split("\n")
        depths = [int(i) for i in string_depths]

    windows = sliding_windows(depths)
    result = sonar_sweep(windows)
    print(result)

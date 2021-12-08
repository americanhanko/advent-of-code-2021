def segment(data):
    second_part = [line.split('|')[1] for line in data.strip().split('\n')]
    digit_occurrences = 0
    for part in second_part:
        digits = part.split()
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                digit_occurrences += 1

    return digit_occurrences


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    print(segment(content))

from collections import Counter

MASTER_KEY = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def segment(data):
    second_part = [line.split("|")[1] for line in data.strip().split("\n")]

    digit_occurrences = 0
    for part in second_part:
        digits = part.split()
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                digit_occurrences += 1

    return digit_occurrences


def create_mapping(display):
    letters_in = dict()
    digits = display.split()
    c = Counter(list(display))
    m = dict()

    for digit in digits:
        if len(digit) == 2:
            letters_in["1"] = digit
        if len(digit) == 3:
            letters_in["7"] = digit  # 'acf'
        if len(digit) == 4:
            letters_in["4"] = digit
        if len(digit) == 7:
            letters_in["8"] = digit

    ac = letters_in["1"] + letters_in["7"]
    count = Counter(ac)
    m["a"] = count.most_common()[-1][0]

    for letter in list("abcdefg"):
        if c[letter] == 8 and letter != m["a"]:
            m["c"] = letter
        if c[letter] == 4:
            m["e"] = letter
        if c[letter] == 9:
            m["f"] = letter
        if c[letter] == 6:
            m["b"] = letter
        if c[letter] == 7:
            pass

    for letter in letters_in["4"]:
        if letter not in m.values():
            m["d"] = letter

    for letter in list("abcdefg"):
        if letter not in m.values():
            m["g"] = letter

    return m


def mapping(data):
    displays = [line.split("|") for line in data.strip().split("\n")]

    all_displays = []

    for display in displays:
        first_part = display[0]
        second = display[1]
        mapping = create_mapping(first_part)
        all_displays.append(get_digits(mapping, second))

    return sum(all_displays)


def get_digits(mapping, second):
    translated = []
    reversed = {v: k for k, v in mapping.items()}
    for letter in list(second):
        try:
            translated.append(reversed[letter])
        except KeyError:
            translated.append(" ")
    translated = "".join(translated).split()
    l_digits = [MASTER_KEY["".join(sorted(word))] for word in translated]
    return int("".join(l_digits))


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    print(segment(content), mapping(content))

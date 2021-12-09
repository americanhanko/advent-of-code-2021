from collections import Counter
from typing import Dict

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


def segment(data: str) -> int:
    second_part = [line.split("|")[1] for line in data.strip().split("\n")]

    digit_occurrences = 0
    for part in second_part:
        digits = part.split()
        for digit in digits:
            if len(digit) in [2, 4, 3, 7]:
                digit_occurrences += 1

    return digit_occurrences


def create_mapping(display: str) -> Dict:
    digit_map = dict()
    digits = display.split()
    digit_count = Counter(list(display))
    wire_map = dict()

    alpha = list("abcdefg")

    for digit in digits:
        if len(digit) == 2:
            digit_map["1"] = digit
        if len(digit) == 3:
            digit_map["7"] = digit
        if len(digit) == 4:
            digit_map["4"] = digit

    one_seven_count = Counter(digit_map["1"] + digit_map["7"])

    for letter in one_seven_count.most_common():
        if letter[1] == 1:
            wire_map["a"] = letter[0]

    for letter in alpha:
        if digit_count[letter] == 8 and letter != wire_map["a"]:
            wire_map["c"] = letter
        if digit_count[letter] == 4:
            wire_map["e"] = letter
        if digit_count[letter] == 9:
            wire_map["f"] = letter
        if digit_count[letter] == 6:
            wire_map["b"] = letter

    remaining = "".join([letter if letter not in wire_map.values() else "" for letter in alpha])

    for letter in remaining:
        if letter in digit_map["4"]:
            wire_map["d"] = letter
        else:
            wire_map["g"] = letter

    return wire_map


def display_sets_sum(data: str) -> int:
    displays = [line.split("|") for line in data.strip().split("\n")]

    display_sets = []
    for display in displays:
        wiring = display[0]
        digits = display[1]
        mapping = create_mapping(wiring)
        result = decode(mapping, digits)
        display_sets.append(result)

    return sum(display_sets)


def decode(wire_map: Dict, digit_data: str) -> int:
    translated = []
    reversed = {v: k for k, v in wire_map.items()}
    for letter in list(digit_data):
        try:
            translation = reversed[letter]
            translated.append(translation)
        except KeyError:
            translated.append(" ")
    translated = "".join(translated).split()
    l_digits = [MASTER_KEY["".join(sorted(word))] for word in translated]
    return int("".join(l_digits))


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    print(segment(content), display_sets_sum(content))

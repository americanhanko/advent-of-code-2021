import dive

data = [
    ("forward", 5),
    ("down", 5),
    ("forward", 8),
    ("up", 3),
    ("down", 8),
    ("forward", 2),
]


def test_dive():
    assert dive.position(data) == 150

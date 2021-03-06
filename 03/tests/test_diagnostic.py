from diagnostic import BinaryDiagnostic

data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_power_consumption():
    diag = BinaryDiagnostic(data)
    assert diag.power_consumption == 198


def test_life_support_rating():
    diag = BinaryDiagnostic(data)
    assert diag.life_support_rating == 230

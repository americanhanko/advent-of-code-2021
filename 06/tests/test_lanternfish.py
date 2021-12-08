import lanternfish

f = [int(d) for d in "3,4,3,1,2".split(",")]


def test_lanternfish_interim_short():
    assert lanternfish.growth_rate(f, days=2) == 6


def test_lanternfish_interim_medium():
    assert lanternfish.growth_rate(f, days=18) == 26


def test_lanternfish():
    assert lanternfish.growth_rate(f, days=80) == 5934


def test_lanternfish_immortal():
    assert lanternfish.growth_rate(f, days=256) == 26984457539

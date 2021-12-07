import lanternfish

fish = "3,4,3,1,2"


def test_lanternfish_interim():
    assert lanternfish.growth_rate(fish, days=1)


def test_lanternfish():
    assert lanternfish.growth_rate(fish, days=80) == 5934

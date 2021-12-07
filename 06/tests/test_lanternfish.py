import lanternfish

fish = "3,4,3,1,2"


def test_lanternfish():
    assert lanternfish.growth_rate(fish) == 5934

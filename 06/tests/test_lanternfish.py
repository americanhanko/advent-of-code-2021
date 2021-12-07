import pytest

import lanternfish

fish = [int(d) for d in "3,4,3,1,2".split(",")]


def test_lanternfish_interim():
    assert lanternfish.growth_rate(fish, days=2)


@pytest.mark.skip
def test_lanternfish():
    assert lanternfish.growth_rate(fish, days=80) == 5934

import sweep


def test_sonar_sweep():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sweep.sonar_sweep(depths) == 7


def test_sliding_windows():
    depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    result = sweep.sliding_windows(depths)
    assert sweep.sonar_sweep(result) == 5

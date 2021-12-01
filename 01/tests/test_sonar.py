import sonar


def test_sonar_sweep():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    assert sonar.sweep(data) == 7


def test_sonar_windows():
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    windows = sonar.windows(data)
    assert sonar.sweep(windows) == 5

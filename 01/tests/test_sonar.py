import sonar

data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def test_sonar_sweep():
    assert sonar.sweep(data) == 7


def test_sonar_windows():
    windows = sonar.windows(data)
    assert sonar.sweep(windows) == 5

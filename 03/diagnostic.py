class BinaryDiagnostic:
    def __init__(self, data):
        self._data = data.strip().split("\n")
        self.gamma = self._common_bit_as_int(max)
        self.epsilon = self._common_bit_as_int(min)
        self.power_consumption = self.gamma * self.epsilon

    def _transpose(self):
        nums = [list(d) for d in self._data]
        return [list(col) for col in zip(*nums)]

    def _common_bit_as_int(self, func):
        as_bin = "".join([func(set(col), key=col.count) for col in self._transpose()])
        return int(as_bin, base=2)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    diag = BinaryDiagnostic(content)
    print(diag.power_consumption)

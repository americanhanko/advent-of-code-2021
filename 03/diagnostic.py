from typing import List


def to_int(bin_str: str) -> int:
    return int(bin_str, base=2)


def comm(func, col):
    if len(col) == 2:
        if func == max:
            return "1"
        else:
            return "0"
    return func(set(col), key=col.count)


class BinaryDiagnostic:
    def __init__(self, data: str):
        self._data = data
        self.bytes = self.refresh_bytes()
        self.cols = self._transposed()
        self.power_consumption = self.gamma() * self.epsilon()
        self.life_support_rating = self.oxygen() * self.scrubber()

    def _transposed(self, start_pos=0) -> List[List[str]]:
        return [list(col) for col in zip(*self.bytes)][start_pos:]

    def _commonality(self, func, data):
        return [comm(func, col) for col in data]

    def gamma(self) -> int:
        s = self._commonality(min, self.cols)
        return to_int("".join(s))

    def epsilon(self) -> int:
        s = self._commonality(max, self.cols)
        return to_int("".join(s))

    def refresh_bytes(self):
        return [list(d) for d in self._data.strip().split("\n")]

    def get_rating(self, func) -> int:
        pos = 0
        cols = self.cols
        self.bytes = self.refresh_bytes()

        while cols:
            common_bit = comm(func, cols[0])
            marked = []

            for i in range(len(self.bytes)):
                this_bit = self.bytes[i][pos]
                if this_bit != common_bit:
                    marked.append(self.bytes[i])

            [self.bytes.remove(mark) for mark in marked]

            if len(self.bytes) == 1:
                return to_int("".join(self.bytes[0]))

            pos += 1
            cols = self._transposed(pos)

        return to_int("".join(self.bytes[0]))

    def oxygen(self) -> int:
        return self.get_rating(max)

    def scrubber(self) -> int:
        return self.get_rating(min)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read()

    diag = BinaryDiagnostic(content)
    print(diag.power_consumption)
    print(diag.life_support_rating)

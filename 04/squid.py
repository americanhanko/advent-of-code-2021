from typing import List


def bingo(raw_data: str, last_winner: bool = False) -> int:
    content = raw_data.strip().split("\n\n")
    num_winners = 0
    numbers_called = [i for i in content[0].split(",")]
    board_data = [
        [row.split() for row in board]
        for board in [board.split("\n") for board in content[1:]]
    ]
    boards = [BingoBoard(data) for data in board_data]
    for number in numbers_called:
        for board in boards:
            board.play_round(number)
            if board.is_winner() and not board.already_won:
                board.already_won = True
                num_winners += 1
                if not last_winner:
                    return board.winning_result(number)
                if last_winner and (len(boards) - num_winners) == 0:
                    return board.winning_result(number)


class BingoBoard:
    def __init__(self, data: List[List[str]]):
        self.already_won = False
        self.rows = data
        self.cols = self._create_cols(data)

    def play_round(self, selection: str) -> None:
        self.rows = [self._rm_num(selection, row) for row in self.rows]
        self.cols = [self._rm_num(selection, col) for col in self.cols]

    def is_winner(self) -> bool:
        return not all(self.rows) or not all(self.cols)

    @staticmethod
    def _rm_num(selection: str, line: List[str]) -> List[str]:
        try:
            line.remove(selection)
        except ValueError:
            pass
        return line

    @staticmethod
    def _create_cols(data: List[List[str]]) -> List[List[str]]:
        columns = []
        for x in range(len(data)):
            columns.append([])
            for y in range(len(data[0])):
                columns[x].append(data[y][x])
        return columns

    def winning_result(self, selection: str) -> int:
        row_sums = [sum([int(val) for val in values]) for values in self.rows]
        return sum(row_sums) * int(selection)


if __name__ == "__main__":
    with open("input") as fp:
        puzzle_input = fp.read()

    one_star = bingo(puzzle_input)
    two_stars = bingo(puzzle_input, last_winner=True)
    print(one_star, two_stars)

import typing
from typing import List


def bingo(selections, board_data, let_squid_win: bool):
    num_winners = 0
    boards = [BingoBoard(data) for data in board_data]
    for selection in selections:
        for board in boards:
            board.play_round(selection)
            if board.check_for_winner() and not board.i_won:
                board.i_won = True
                num_winners += 1
                if not let_squid_win:
                    return board.winning_result(selection)
                if let_squid_win and (len(boards) - num_winners) == 0:
                    return board.winning_result(selection)


class BingoBoard:
    def __init__(self, data):
        self.data = data
        self.i_won = False
        self.rows = data
        self.columns = self._create_columns(data)

    def play_round(self, selection):
        self.rows = [self.rm_selection(row, selection) for row in self.rows]
        self.columns = [self.rm_selection(column, selection) for column in self.columns]

    def check_for_winner(self):
        return not all(self.rows) or not all(self.columns)

    @staticmethod
    def rm_selection(line, selection):
        try:
            line.remove(selection)
        except ValueError:
            pass
        return line

    @staticmethod
    def _create_columns(data):
        columns = []
        for i in range(len(data)):
            columns.append([])
            for j in range(len(data[0])):
                columns[i].append(data[j][i])
        return columns

    def winning_result(self, selection):
        return sum([sum([int(i) for i in row]) for row in self.rows]) * int(selection)


if __name__ == "__main__":
    with open("input") as fp:
        content = fp.read().strip().split("\n\n")

    def selections():
        return [i for i in content[0].split(",")]

    def all_boards():
        board_data = content[1:]
        boards = [board.split("\n") for board in board_data]
        all_boards = []

        for board in boards:
            b = [row.split() for row in board]
            all_boards.append(b)

        return all_boards

    result = bingo(selections(), all_boards(), let_squid_win=True)
    print(result)

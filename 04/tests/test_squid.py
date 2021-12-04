import pytest

import squid

from squid import BingoBoard


@pytest.mark.skip()
def test_bingo_winner(selections, all_boards):
    assert squid.bingo(selections, all_boards) == 4512


def test_creating_bingo_board(all_boards):
    first = all_boards[0]
    b = BingoBoard(first)
    assert b.columns == [
        ["22", "8", "21", "6", "1"],
        ["13", "2", "9", "10", "12"],
        ["17", "23", "14", "3", "20"],
        ["11", "4", "16", "18", "15"],
        ["0", "24", "7", "5", "19"],
    ]

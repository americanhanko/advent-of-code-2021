import pytest

import squid

from squid import BingoBoard


def test_bingo_winner(selections, all_boards):
    assert squid.bingo(selections, all_boards, let_squid_win=False) == 4512


def test_squid_bingo_winner(selections, all_boards):
    assert squid.bingo(selections, all_boards, let_squid_win=True) == 1924


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


def test_checking_marking_selection(all_boards):
    first = all_boards[0]
    b = BingoBoard(first)
    b.play_round("22")

    assert b.rows == [
        ["13", "17", "11", "0"],
        ["8", "2", "23", "4", "24"],
        ["21", "9", "14", "16", "7"],
        ["6", "10", "3", "18", "5"],
        ["1", "12", "20", "15", "19"],
    ]

    assert b.columns == [
        ["8", "21", "6", "1"],
        ["13", "2", "9", "10", "12"],
        ["17", "23", "14", "3", "20"],
        ["11", "4", "16", "18", "15"],
        ["0", "24", "7", "5", "19"],
    ]


def test_checking_winning_board(selections, all_boards):
    board = all_boards[2]
    b = BingoBoard(board)

    for selection in selections:
        b.play_round(selection)
        if b.check_for_winner():
            break

    assert b.rows == [
        [],
        ["10", "16", "15", "19"],
        ["18", "8", "26", "20"],
        ["22", "13", "6"],
        ["12", "3"],
    ]

    assert b.columns == [
        ["10", "18", "22"],
        ["16", "8"],
        ["15", "13", "12"],
        ["26", "6", "3"],
        ["19", "20"],
    ]

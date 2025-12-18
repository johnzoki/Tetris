import pytest

from tetris import Board
from tetris.logic import board_move_piece_down


def test_move_down():
    board = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]
    assert board_move_piece_down(board, 0) == True
    assert board == [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]

    assert board_move_piece_down(board, 2) == False
    assert board == [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]

    assert board_move_piece_down(board, 1) == True
    assert board == [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]

    assert board_move_piece_down(board, 1) == False
    assert board == [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
    ]

    assert board_move_piece_down(board, 2) == True
    assert board == [
        [1, 1, 0, 0],
        [0, 1, 1, 0],
        [2, 2, 0, 0],
        [2, 2, 0, 0],
        [0, 0, 0, 0],
    ]

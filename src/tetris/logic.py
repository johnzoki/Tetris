from enum import Enum

from result import Err, Ok, Result

from tetris import BOARDHEIGHT, BOARDWIDTH, Board


class LogicErrors(Enum):
    NotMoveable = 1


def board_move_piece_down(board: Board, p_id: int) -> bool:
    """
    Moves the specified piece down by one in the board.

    Args:
        board (Board): The board in which the board.
        p_id (int): The id of the piece to move down.

    Returns:
        True: if the operation succeeded or the p_id is zero.
        False: if the piece could not be moved.
    """
    if p_id == 0:
        return True
    if any(p_id == id for id in board[0]):
        return False
    piece_positions = [
        (x, y)
        for y in range(1, len(board))
        for x in range(len(board[0]))
        if board[y][x] == p_id
    ]
    if all(
        board[y - 1][x] == 0 or board[y - 1][x] == p_id for (x, y) in piece_positions
    ):
        for x, y in piece_positions:
            board[y][x] = 0
            board[y - 1][x] = p_id
        return True
    return False

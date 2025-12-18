from enum import Enum

Board = list[list[int]]
PieceMap = dict[int, PieceType]
NextQueue = list[PieceType]


class PieceType(Enum):
    Cube = 1
    T = 2
    I = 3
    S = 4
    Sm = 5
    L = 6
    Lm = 7


def main() -> None:
    print("Hello from tetris!")

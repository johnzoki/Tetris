from enum import Enum


class PieceType(Enum):
    Cube = 1
    T = 2
    I = 3
    S = 4
    Sm = 5
    L = 6
    Lm = 7


Board = list[list[int]]
PieceMap = dict[int, PieceType]
NextQueue = list[PieceType]


def main() -> None:
    print("Hello from tetris!")

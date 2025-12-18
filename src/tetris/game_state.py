from tetris import Board, NextQueue, PieceMap, PieceType


class Gamestate:
    def __init__(self, *args):
        self.board: Board = []
        self.piece_queue: NextQueue = []
        self.piece_map: PieceMap = []
        self.hold_piece: PieceType | None = None
        self.score: int = 0

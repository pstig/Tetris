from Piece import Piece


class TPiece(Piece):
    def __init__(self):
        self._positions = [
            [(0, 0), (0, -1), (0, 1), (-1, 0)],
            [(0, 0), (1, 0), (-1, 0), (0, 1)],
            [(0, 0), (0, -1), (0, 1), (1, 0)],
            [(0, 0), (1, 0), (-1, 0), (0, -1)],
        ]
        self._position_id = 0
        super().__init__()

    def rotate_left(self):
        self._position_id = (self._position_id - 1) % 4

    def rotate_right(self):
        self._position_id = (self._position_id + 1) % 4

    def get_locations(self):
        return self._positions[self._position_id]

    def get_character_name(self):
        return "T"

    def get_spawn_offset(self):
        return [1,1]

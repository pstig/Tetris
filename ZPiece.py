from Piece import Piece


class ZPiece(Piece):
    def __init__(self):
        self._is_flat = True
        super().__init__()

    def rotate_left(self):
        self._is_flat = not self._is_flat

    def rotate_right(self):
        self._is_flat = not self._is_flat

    def get_locations(self):
        return (
            [(0, 0), (-1, 0), (0, 1), (1, 1)]
            if self._is_flat
            else [(0, 0), (0, 1), (1, 0), (1, -1)]
        )

    def get_character_name(self):
        return "Z"

    def get_spawn_offset(self):
        return [0,1]

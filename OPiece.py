from Piece import Piece


class OPiece(Piece):
    def __init__(self):
        super().__init__()

    def rotate_left(self):
        pass

    def rotate_right(self):
        pass

    def get_locations(self):
        return [(0, 0), (0, 1), (1, 1), (1, 0)]

    def get_character_name(self):
        return "O"
    
    def get_spawn_offset(self):
        return [0,1]

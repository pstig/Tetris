class Piece:
    def get_locations(self):
        raise NotImplementedError("base class not implemented")

    def rotate_right(self):
        raise NotImplementedError("base class not implemented")

    def rotate_left(self):
        raise NotImplementedError("base class not implemented")

    def get_character_name(self):
        raise NotImplementedError("base class not implemented")

    def get_spawn_offset(self):
        raise NotImplementedError("base class not implemented")

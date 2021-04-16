

class Earring:

    def __init__(self):
        self.layer = 3
        self.trait_id = 24

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [14, 15, 6, 7],  # yellow
                [14, 15, 5, 6],
                [15, 16, 6, 7]  # black
            ]
        else:
            return [
                [14, 15, 5, 6],  # yellow
                [14, 15, 4, 5],
                [15, 16, 5, 6]  # black
            ]



class SkinEffect:

    def __init__(self):
        self.layer = 3

    def get_pos(self, facetype):
        return []


class Mole(SkinEffect):

    def __init__(self):
        super().__init__()
        self.trait_id = 48

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [16, 17, 9, 10]
            ]
        else:
            return [
                [16, 17, 8, 9]
            ]


class RosyCheeks(SkinEffect):

    def __init__(self):
        super().__init__()
        self.trait_id = 66

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [15, 16, 9, 11],
                [15, 16, 14, 16]
            ]
        else:
            return [
                [15, 16, 9, 11],
                [15, 16, 15, 16],
                [16, 17, 9, 10],
                [16, 17, 15, 16]
            ]


class Spots(SkinEffect):

    def __init__(self):
        super().__init__()
        self.trait_id = 72

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [9, 10, 14, 15],
                [10, 11, 11, 12],
                [13, 14, 7, 8],
                [14, 15, 14, 15],
                [16, 17, 9, 10],
                [17, 18, 15, 16],
                [20, 21, 12, 13]
            ]
        else:
            return [
                [8, 9, 10, 11],
                [8, 9, 14, 15],
                [13, 14, 7, 8],
                [14, 15, 14, 15],
                [16, 17, 9, 10],
                [17, 18, 15, 16],
                [20, 21, 8, 9],
                [20, 21, 12, 13]
            ]

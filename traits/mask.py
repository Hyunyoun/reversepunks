

class Mask:

    def __init__(self):
        self.layer = 3

    def get_pos(self, facetype):
        return []


class MedicalMask(Mask):

    def __init__(self):
        super().__init__()
        self.trait_id = 43

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [13, 14, 7, 8],
                [14, 15, 8, 9],
                [14, 15, 15, 16],
                [15, 16, 9, 12],
                [15, 16, 13, 15],
                [16, 17, 9, 15],
                [17, 18, 10, 14],
                [18, 19, 8, 16],
                [19, 20, 9, 15],
                [20, 21, 10, 14],  # white
                [15, 16, 12, 13],
                [17, 18, 9, 10],
                [17, 18, 14, 15]  # gray
            ]
        else:
            return [
                [12, 13, 6, 7],
                [13, 14, 7, 8],
                [14, 15, 8, 9],
                [14, 15, 15, 16],
                [15, 16, 9, 12],
                [15, 16, 13, 15],
                [16, 17, 9, 15],
                [17, 18, 10, 14],
                [18, 19, 7, 16],
                [19, 20, 9, 15],
                [20, 21, 10, 14],  # white
                [15, 16, 12, 13],
                [17, 18, 9, 10],
                [17, 18, 14, 15]  # gray
            ]
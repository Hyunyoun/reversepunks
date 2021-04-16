

class EyeShadow:

    def __init__(self):
        self.layer = 2

    def get_pos(self, facetype):
        return []


class ColoredEyeShadow(EyeShadow):

    def __init__(self):
        super().__init__()
        self.trait_id = 34  # Green
        # self.trait_id = 61  # Purple
        # self.trait_id = 8  # Blue

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [12, 13, 9, 11],
                [12, 13, 14, 16],  # green
                [13, 14, 9, 11],
                [13, 14, 14, 16]  # light green
            ]
        else:
            return [
                [11, 12, 9, 11],
                [11, 12, 14, 16],  # green
                [12, 13, 9, 11],
                [12, 13, 14, 16]  # light green
            ]


class ClownEyes(EyeShadow):

    def __init__(self):
        super().__init__()
        self.trait_id = 17  # Green
        # self.trait_id = 16  # Blue

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 9, 10],
                [11, 12, 14, 15],  # light green
                [12, 13, 9, 11],
                [12, 13, 14, 16],  # green
                [13, 14, 9, 11],
                [13, 14, 14, 16],  # dark green
                [14, 15, 9, 10],
                [14, 15, 14, 15]  # light green
            ]
        else:
            return [
                [10, 11, 9, 10],
                [10, 11, 14, 15],  # light green
                [11, 12, 9, 11],
                [11, 12, 14, 16],  # green
                [12, 13, 9, 11],
                [12, 13, 14, 16],  # dark green
                [13, 14, 9, 10],
                [13, 14, 14, 15]  # light green
            ]


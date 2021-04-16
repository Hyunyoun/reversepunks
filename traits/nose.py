

class Nose:
    def __init__(self):
        self.layer = 3

    def get_pos(self, facetype):
        if facetype == "Female":
            return [
                [16, 17, 12, 13]
            ]
        else:
            return [
                [15, 16, 12, 14]
            ]


class ClownNose(Nose):
    def __init__(self):
        super().__init__()
        self.trait_id = 19

    def get_pos(self, facetype):
        if facetype == "Female":
            return [
                [15, 16, 12, 14],
                [16, 17, 12, 14]
            ]
        else:
            return [
                [14, 15, 12, 14],
                [15, 16, 12, 14]
            ]

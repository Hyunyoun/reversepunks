

class Neck:

    def __init__(self):
        self.layer = 3

    def get_pos(self, facetype):
        return []


class Choker(Neck):

    def __init__(self):
        super().__init__()
        self.trait_id = 13

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [20, 21, 9, 10],
                [21, 22, 9, 11],
                [22, 23, 10, 12]
            ]
        else:
            return [
            ]


class GoldChain(Neck):

    def __init__(self):
        super().__init__()
        self.trait_id = 33

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [22, 23, 9, 12]
            ]
        else:
            return [
                [20, 21, 7, 8],
                [21, 22, 8, 9],
                [22, 23, 9, 10]
            ]


class SilverChain(Neck):

    def __init__(self):
        super().__init__()
        self.trait_id = 69

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [22, 23, 9, 12]
            ]
        else:
            return [
                [22, 23, 9, 12]
            ]


class Sample(Neck):

    def __init__(self):
        super().__init__()
        self.trait_id = 29

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
            ]

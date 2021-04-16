

class Beard:

    def __init__(self):
        self.layer = 4

    def get_pos(self, facetype):
        return []


class BigBeard(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 3

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [16, 17, 9, 16],
                [17, 18, 7, 17],
                [18, 19, 6, 11],
                [18, 19, 14, 17],
                [19, 20, 6, 17],
                [20, 21, 6, 17],
                [21, 22, 8, 17],
                [22, 23, 11, 16],  # brown
                [16, 17, 16, 17],
                [17, 18, 6, 7],
                [17, 18, 17, 18],
                [18, 19, 5, 6],
                [18, 19, 17, 18],
                [19, 20, 5, 6],
                [19, 20, 17, 18],
                [20, 21, 5, 6],
                [20, 21, 17, 18],
                [21, 22, 6, 8],
                [21, 22, 17, 18],
                [22, 23, 8, 11],
                [22, 23, 16, 17],
                [23, 24, 10, 16]  # black
            ]


class Chinstrap(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 12

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 7, 8],
                [16, 17, 7, 9],
                [16, 17, 15, 16],
                [17, 18, 7, 9],
                [17, 18, 15, 16],
                [18, 19, 8, 10],
                [18, 19, 15, 16],
                [19, 20, 8, 10],
                [19, 20, 15, 16],
                [20, 21, 9, 15],
                [21, 22, 11, 14],  # yellow
                [21, 22, 10, 11],
                [21, 22, 14, 15],
                [22, 23, 11, 14]  # black
            ]


class FrontBeard(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 28

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [17, 18, 10, 15],
                [18, 19, 10, 11],
                [18, 19, 14, 15],
                [19, 20, 10, 15],
                [20, 21, 11, 14],
                [21, 22, 11, 14],  # brown
                [22, 23, 11, 14]  # black contour

            ]


class FrontBeardDark(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 29

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [17, 18, 10, 15],
                [18, 19, 10, 11],
                [18, 19, 14, 15],
                [19, 20, 10, 15],
                [20, 21, 11, 14],
                [21, 22, 11, 14],  # brown
                [22, 23, 11, 14]  # black contour
            ]


class Goat(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 32

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [20, 21, 11, 14],
                [21, 22, 11, 14],
                [22, 23, 12, 13],  # brown
                [22, 23, 11, 12],
                [22, 23, 13, 14],
                [23, 24, 12, 13]  # black
            ]


class Handlebars(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 36

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [17, 18, 11, 14],
                [18, 19, 10, 11],
                [18, 19, 14, 15],
                [19, 20, 10, 11],
                [19, 20, 14, 15],  # yellow
                [17, 18, 10, 11],
                [17, 18, 14, 15]  # light yellow
            ]


class LuxuriousBeard(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 42

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 6, 8],
                [16, 17, 6, 10],
                [16, 17, 15, 17],
                [17, 18, 6, 17],
                [18, 19, 6, 11],
                [18, 19, 14, 17],
                [19, 20, 6, 17],
                [20, 21, 8, 16],
                [21, 22, 8, 16],
                [22, 23, 9, 15]  # black
            ]


class Mustache(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 49

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [17, 18, 10, 15]
            ]


class Muttonchops(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 50

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 7, 8],
                [16, 17, 7, 9],
                [16, 17, 15, 16],
                [17, 18, 7, 10],
                [17, 18, 15, 16],
                [18, 19, 8, 10],
                [18, 19, 15, 16]
            ]


class NormalBeard(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 52

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 7, 8],
                [16, 17, 7, 9],
                [16, 17, 15, 16],
                [17, 18, 7, 16],
                [18, 19, 7, 11],
                [18, 19, 14, 16],
                [19, 20, 8, 16],
                [20, 21, 9, 15]
            ]


class NormalBeardBlack(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 53

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 7, 8],
                [16, 17, 7, 9],
                [16, 17, 15, 16],
                [17, 18, 7, 16],
                [18, 19, 7, 11],
                [18, 19, 14, 16],
                [19, 20, 8, 16],
                [20, 21, 9, 15]
            ]


class ShadowBeard(Beard):

    def __init__(self):
        super().__init__()
        self.trait_id = 67
        self.beard_lip = True

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
            ]
        else:
            return [
                [15, 16, 7, 8],
                [16, 17, 7, 9],
                [16, 17, 15, 16],
                [17, 18, 7, 16],
                [18, 19, 7, 11],
                [18, 19, 14, 16],
                [19, 20, 8, 16],
                [20, 21, 9, 15] # dark brown
            ]


class Sample(Beard):

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


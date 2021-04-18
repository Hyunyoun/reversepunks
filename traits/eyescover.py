

class EyesCover:

    def __init__(self):
        self.layer = 3

    def get_pos(self, facetype):
        return []


class Eyes:

    def __init__(self):
        self.layer = 2

    def get_pos(self, facetype):
        return []


class EyeShadow:

    def __init__(self):
        self.layer = 1

    def get_pos(self, facetype):
        return []


class ThreeDGlasses(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 0

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 7, 17],
                [12, 13, 7, 9],
                [13, 14, 8, 9],
                [12, 14, 12, 13],
                [12, 14, 16, 17],
                [14, 15, 8, 17],  # white
                [12, 14, 9, 12],  # red
                [12, 14, 13, 16]  # blue
            ]
        else:
            return [
                [10, 11, 6, 17],
                [11, 12, 7, 9],
                [11, 12, 12, 13],
                [11, 12, 16, 17],
                [12, 13, 8, 9],
                [12, 13, 12, 13],
                [12, 13, 16, 17],
                [13, 14, 8, 17],  # white
                [11, 13, 9, 12],  # red
                [11, 13, 13, 16]  # blue
            ]


class BigShades(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 4

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 15, 7, 12],
                [15, 16, 8, 11],
                [11, 15, 13, 18],
                [15, 16, 14, 17],
                [12, 13, 12, 13],
                [13, 14, 6, 7],  # black
                [12, 13, 8, 11],
                [12, 13, 14, 17],  # dark red
                [13, 14, 8, 11],
                [13, 14, 14, 17],  # red
                [14, 15, 8, 11],
                [14, 15, 14, 17]  # light red
            ]
        else:
            return [
                [9, 13, 7, 12],
                [13, 14, 8, 11],
                [9, 13, 13, 18],
                [13, 14, 14, 17],
                [10, 11, 12, 13],
                [11, 12, 6, 7],  # black
                [10, 11, 8, 11],
                [10, 11, 14, 17],  # dark red
                [11, 12, 8, 11],
                [11, 12, 14, 17],  # red
                [12, 13, 8, 11],
                [12, 13, 14, 17]  # light red
           ]


class ClassicShades(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 15

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 7, 17],
                [12, 14, 8, 12],
                [12, 14, 13, 17],
                [14, 15, 9, 11],
                [14, 15, 14, 16],  # black
                [12, 13, 9, 11],
                [12, 13, 14, 16],  # dark red
                [13, 14, 9, 11],
                [13, 14, 14, 16]  # red
            ]
        else:
            return [
                [10, 11, 7, 17],
                [11, 13, 8, 12],
                [11, 13, 13, 17],
                [13, 14, 9, 11],
                [13, 14, 14, 16],  # black
                [11, 12, 9, 11],
                [11, 12, 14, 16],  # dark red
                [12, 13, 9, 11],
                [12, 13, 14, 16]  # red
           ]


class EyeMask(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 25

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 7, 17],
                [12, 13, 7, 9],
                [12, 13, 11, 14],
                [12, 13, 16, 17],
                [13, 14, 6, 9],
                [13, 14, 11, 14],
                [13, 14, 16, 17],
                [14, 15, 6, 17],  # black
                [13, 14, 9, 10],
                [13, 14, 14, 15]  # white
            ]
        else:
            return [
                [10, 11, 7, 17],
                [11, 12, 7, 9],
                [11, 12, 11, 14],
                [11, 12, 16, 17],
                [12, 13, 6, 9],
                [12, 13, 11, 14],
                [12, 13, 16, 17],
                [13, 14, 6, 17],  # black
                [12, 13, 9, 10],
                [12, 13, 14, 15]  # white
            ]


class EyePatch(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 26

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 7, 16],
                [12, 14, 8, 12],
                [14, 15, 9, 11]  # black
            ]
        else:
            return [
                [10, 11, 7, 16],
                [11, 13, 8, 12],
                [13, 14, 9, 11]  # black
            ]


class HornedRimGlasses(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 39

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 7, 17],
                [12, 13, 7, 8],
                [12, 13, 11, 13],
                [12, 13, 16, 17],  # black
                [12, 15, 8, 11],
                [12, 15, 13, 16]  # transparent white
            ]
        else:
            return [
                [10, 11, 7, 18],
                [11, 12, 7, 8],
                [11, 12, 11, 13],
                [11, 12, 17, 18],  # black
                [11, 14, 8, 11],
                [11, 14, 13, 16]  # transparent white
            ]


class NerdGlasses(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 51

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 14, 8, 12],
                [11, 14, 13, 17],
                [12, 13, 7, 8],
                [12, 13, 12, 13],
                [14, 15, 9, 11],
                [14, 15, 14, 16],  # black
                [12, 14, 9, 11],
                [12, 14, 14, 16]  # light blue
            ]
        else:
            return [
                [10, 14, 8, 12],
                [10, 14, 13, 17],
                [11, 12, 7, 8],
                [11, 12, 12, 13],  # black
                [11, 13, 9, 11],
                [11, 13, 14, 16]  # light blue
            ]


class RegularShades(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 65

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 6, 17],
                [12, 13, 8, 12],
                [12, 13, 13, 17],
                [13, 14, 9, 11],
                [13, 14, 14, 16]  # black
            ]
        else:
            return [
                [11, 12, 5, 18],
                [12, 13, 8, 12],
                [12, 13, 14, 18],
                [13, 14, 9, 11],
                [13, 14, 15, 17]  # black
            ]


class SmallShades(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 70

    def get_pos(self, facetype):
        if facetype == 'Female':
            return []
            # return [
            #     [12, 13, 7, 17],
            #     [13, 15, 9, 11],
            #     [13, 15, 14, 16]  # black
            # ]
        else:
            return [
                [11, 12, 7, 16],
                [12, 13, 6, 7],
                [12, 13, 9, 11],
                [12, 14, 9, 11],
                [12, 14, 14, 16]  # black
            ]


class VR(EyesCover):

    def __init__(self):
        super().__init__()
        self.trait_id = 80

    def get_pos(self, facetype):
        if facetype == 'Female':
            return [
                [11, 12, 8, 17],
                [12, 13, 7, 8],
                [12, 13, 17, 18],
                [13, 14, 6, 7],
                [13, 14, 9, 16],
                [13, 14, 17, 18],
                [14, 15, 6, 7],
                [14, 15, 9, 16],
                [14, 15, 17, 18],
                [15, 16, 7, 8],
                [15, 16, 17, 18],
                [16, 17, 8, 17],  # black
                [12, 13, 8, 9],
                [12, 13, 16, 17],
                [13, 15, 7, 8],
                [15, 16, 8, 9],
                [15, 16, 16, 17],  # gray
                [12, 13, 9, 16],
                [13, 15, 8, 9],
                [13, 15, 16, 17],
                [15, 16, 9, 16]  # light gray
            ]
        else:
            return [
                [9, 10, 8, 17],
                [10, 13, 7, 18],
                [11, 13, 6, 18],
                [13, 14, 7, 18],
                [14, 15, 8, 17],  # black
                [10, 11, 9, 16],
                [11, 13, 8, 9],
                [11, 13, 16, 17],
                [13, 14, 9, 16],  # light gray
                [10, 11, 8, 9],
                [10, 11, 16, 17],
                [11, 13, 7, 8],
                [13, 14, 8, 9],
                [13, 14, 16, 17],  # gray
                [11, 13, 9, 16]  # black
            ]

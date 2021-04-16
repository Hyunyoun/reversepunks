

class Lip:

    def __init__(self):
        self.layer = 1

    def get_pos(self, facetype):
        return [
            [18, 19, 11, 14]
        ]


class Lipstick(Lip):

    def __init__(self):
        super().__init__()
        self.trait_id = 40  # Hot
        # self.trait_id = 63  # Purple
        # self.trait_id = 5  # Black

    def get_pos(self, facetype):
        return [
            [18, 19, 11, 14]
        ]


class BuckTeeth(Lip):

    def __init__(self):
        super().__init__()
        self.trait_id = 9

    def get_pos(self, facetype):
        return [
            [18, 19, 11, 12],
            [18, 19, 13, 14],  # white
            [18, 19, 12, 13]  # black
        ]


class Frown(Lip):

    def __init__(self):
        super().__init__()
        self.trait_id = 30

    def get_pos(self, facetype):
        return [
            [18, 19, 11, 14],
            [19, 20, 10, 11]  # black
        ]


class Smile(Lip):

    def __init__(self):
        super().__init__()
        self.trait_id = 71

    def get_pos(self, facetype):
        return [
            [17, 18, 10, 11],
            [18, 19, 11, 14]  # black
        ]


class BeardLip(Lip):

    def __init__(self):
        super().__init__()

    def get_pos(self, facetype):
        return [
            [18, 19, 11, 14]
        ]

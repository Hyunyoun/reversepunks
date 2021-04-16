

class Cigar:

    def __init__(self):
        self.layer = 10

    def get_pos(self, facetype):
        return []


class Cigarette(Cigar):

    def __init__(self):
        super().__init__()
        self.trait_id = 14

    def get_pos(self, facetype):
        return [
            [17, 18, 14, 20],
            [18, 19, 13, 21],
            [19, 20, 14, 20],  # black
            [18, 19, 14, 19],  # white
            [18, 19, 19, 20],  # orange
            [10, 16, 19, 20]  # smoke white
        ]


class Pipe(Cigar):

    def __init__(self):
        super().__init__()
        self.trait_id = 59

    def get_pos(self, facetype):
        return [
            [18, 19, 14, 15],
            [19, 20, 13, 16],
            [19, 20, 18, 23],
            [20, 21, 14, 17],
            [20, 21, 18, 23],
            [21, 22, 15, 23],
            [22, 23, 16, 22],
            [23, 24, 17, 21],  # black
            [19, 20, 14, 15],
            [20, 21, 15, 16],
            [21, 22, 16, 17],
            [22, 23, 17, 21],
            [20, 22, 19, 22],  # yellow brown
            [21, 22, 19, 20],
            [21, 22, 21, 22],
            [22, 23, 20, 21],  # brown
            [11, 12, 20, 21],
            [12, 14, 19, 22],
            [15, 16, 20, 21],
            [17, 18, 20, 21]  # smoke white
        ]


class Vape(Cigar):

    def __init__(self):
        super().__init__()
        self.trait_id = 82

    def get_pos(self, facetype):
        return [
            [17, 20, 14, 21],
            [18, 19, 13, 14],  # black
            [18, 19, 14, 19],  # gray
            [18, 19, 19, 20]  # blue

        ]





from .face import Face


class Ape(Face):

    def __init__(self):
        super().__init__()
        self.face_type = "Ape"

    def get_contour_pos(self):
        return [
            [5, 6, 8, 15],
            [6, 7, 7, 8],
            [7, 12, 6, 7],
            [12, 15, 5, 6],
            [14, 24, 6, 7],
            [6, 7, 15, 16],
            [7, 20, 16, 17],
            [20, 21, 15, 16],
            [21, 22, 10, 15],
            [22, 24, 10, 11],
            [9, 10, 9, 15],
            [18, 20, 8, 9],
            [20, 21, 9, 10]
        ]

    def get_face_pos(self):
        return [
            [6, 7, 8, 15],
            [7, 12, 7, 16],
            [12, 14, 6, 16],
            [14, 20, 7, 16],
            [20, 21, 7, 15],
            [21, 24, 7, 10]
        ]

    def get_inside_face_pos(self):
        return [
            [10, 15, 8, 16],
            [15, 16, 9, 16],
            [16, 17, 10, 15],
            [17, 20, 9, 16],
            [20, 21, 10, 15]
        ]

    def get_eyebrow_pos(self):
        return [
            [11, 12, 9, 11],
            [11, 12, 14, 16],
        ]

    def get_eyeball_pos(self):
        return [
            [12, 13, 9, 11],
            [12, 13, 14, 16]
        ]

    def get_eye_pos(self):
        return [
            [12, 13, 9, 10],
            [12, 13, 14, 15]
        ]

    def get_nose_pos(self):
        return [
            [15, 16, 11, 12],
            [15, 16, 13, 14]
        ]

    def get_mouth_pos(self):
        return [
            [18, 19, 10, 15]
        ]



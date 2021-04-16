
from .face import Face


class Zombie(Face):

    def __init__(self):
        super().__init__()
        self.face_type = "Zombie"

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
            [22, 24, 10, 11]
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
            [7, 8, 9, 10],
            [8, 9, 8, 9]
        ]

    def get_eyebrow_pos(self):
        return [
            [11, 12, 9, 11],
            [13, 14, 9, 10],
            [11, 12, 14, 16],
            [13, 14, 14, 15]
        ]

    def get_eyeball_pos(self):
        return [
            [12, 13, 9, 11],
            [12, 13, 14, 16]
        ]

    def get_eye_pos(self):
        return [
            [12, 13, 10, 11],
            [12, 13, 15, 16]
        ]

    def get_nose_pos(self):
        return [
            [15, 16, 12, 14]
        ]

    def get_mouth_pos(self):
        return [
            [18, 19, 11, 14]
        ]


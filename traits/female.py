
from .face import Face


class Female(Face):

    def __init__(self):
        super().__init__()
        self.face_type = "Female"

    def get_contour_pos(self):
        return [
            [7, 8, 9, 15],
            [8, 9, 8, 9],
            [9, 12, 7, 8],
            [12, 15, 6, 7],
            [14, 19, 7, 8],
            [19, 24, 8, 9],
            [8, 9, 15, 16],
            [9, 19, 16, 17],
            [19, 20, 15, 16],
            [20, 21, 10, 11],
            [20, 21, 14, 15],
            [21, 22, 11, 14],
            [22, 24, 12, 13]
        ]

    def get_face_pos(self):
        return [
            [8, 9, 9, 15],
            [9, 12, 8, 16],
            [12, 14, 7, 16],
            [14, 19, 8, 16],
            [19, 20, 9, 15],
            [20, 21, 9, 14],
            [21, 24, 9, 12]
        ]

    def get_inside_face_pos(self):
        return [
            [9, 10, 9, 10]
        ]

    def get_eyebrow_pos(self):
        return [
            [12, 13, 9, 11],
            [12, 13, 14, 16],
        ]

    def get_eyeball_pos(self):
        return [
            [13, 14, 9, 11],
            [13, 14, 14, 16]
        ]

    def get_eye_pos(self):
        return [
            [13, 14, 9, 10],
            [13, 14, 14, 15]
        ]

    def get_nose_pos(self):
        return [
            [16, 17, 12, 13]
        ]

    def get_mouth_pos(self):
        return [
            [18, 19, 11, 14]
        ]



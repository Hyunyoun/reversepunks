from PIL import Image
import numpy as np


class Face:

    PIXEL_PER_DOT = 14
    DOT_WIDTH = 24
    DOT_HEIGHT = 24
    WIDTH = PIXEL_PER_DOT * DOT_WIDTH
    HEIGHT = PIXEL_PER_DOT * DOT_HEIGHT
    TRANSPARENT_COLOR = np.array([255, 255, 255, 0])

    def __init__(self):
        self.contour_color = np.array([0, 0, 0, 255])
        self.face_color = np.array([0, 0, 0, 255])
        self.face_type = ""
        self.layer = 1

    def set_face_color(self, img_array):
        self.face_color = img_array[23*self.PIXEL_PER_DOT, 9*self.PIXEL_PER_DOT].copy()

    def get_contour_pos(self):
        return []

    def get_face_pos(self):
        return []

    def get_inside_face_pos(self):
        return []

    def get_eyebrow_pos(self):
        return []

    def get_eyeball_pos(self):
        return []

    def get_eye_pos(self):
        return []

    def get_nose_pos(self):
        return []

    def get_mouth_pos(self):
        return []

    def set_color(self, img_array, new_img_array, pos):
        if not pos:
            return

        color = img_array[self.PIXEL_PER_DOT*pos[-1][1] - 1, self.PIXEL_PER_DOT*pos[-1][3] - 1].copy()
        for sub_pos in pos:
            new_img_array[sub_pos[0] * self.PIXEL_PER_DOT:sub_pos[1] * self.PIXEL_PER_DOT, sub_pos[2] * self.PIXEL_PER_DOT:sub_pos[3] * self.PIXEL_PER_DOT] = color

    def set_component_color(self, img_array, new_img_array, pos):
        if not pos:
            return

        color = img_array[self.PIXEL_PER_DOT*pos[0], self.PIXEL_PER_DOT*pos[2]].copy()
        new_img_array[pos[0] * self.PIXEL_PER_DOT:pos[1] * self.PIXEL_PER_DOT, pos[2] * self.PIXEL_PER_DOT:pos[3] * self.PIXEL_PER_DOT] = color

    def extract_face(self, img_array):
        self.set_face_color(img_array)

        new_img_array = np.tile(self.TRANSPARENT_COLOR, (self.WIDTH, self.HEIGHT, 1))

        self.set_color(img_array, new_img_array, self.get_face_pos())
        self.set_color(img_array, new_img_array, self.get_inside_face_pos())
        self.set_color(img_array, new_img_array, self.get_contour_pos())

        # for pos in self.get_inside_face_pos():
        #     self.set_color(img_array, new_img_array, pos)
        #
        # for pos in self.get_contour_pos():
        #     self.set_color(img_array, new_img_array, pos)

        return Image.fromarray(new_img_array.astype(np.uint8), 'RGBA')

    def extract_component(self, img_array, pos):
        new_img_array = np.tile(self.TRANSPARENT_COLOR, (self.WIDTH, self.HEIGHT, 1))

        for subpos in pos:
            self.set_component_color(img_array, new_img_array, subpos)

        return Image.fromarray(new_img_array.astype(np.uint8), 'RGBA')





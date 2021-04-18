import os
from PIL import Image

import numpy as np
import pandas as pd

from database import DBClient


class PngGenerator:

    ROOT_DIR = os.path.join(os.path.realpath(os.curdir), "image/trait")
    skin_color_map = {
        '0x713f1d': 'Brownie',
        '0xae8b61': 'Choco',
        '0xdbb180': 'Butter',
        '0xead9d9': 'Milk'
    }

    def __init__(self):
        self.db_client = DBClient()
        self.set_layers()
        self.load_data_from_db()

    def set_layers(self):
        self.layers = pd.DataFrame({
            "layer": [
                "Background", "Face", "Eyeballs", "SkinEffect", "EyeShadow",
                "Neck", "Eyes", "Mustache", "Smile", "Lip", "Beard",
                "Earring", "Nose", "Shades", "Hair",
                "Hat", "Mask", "EyesCover", "NoseAccessory", "Cigar"
            ],
            "mandatory": [
                True, True, True, False, True,
                False, True, False, False, True, False,
                False, True, False, False,
                False, False, False, False, False
            ]
        })
        self.layers["order"] = range(self.layers.shape[0])

    def load_data_from_db(self):
        self.load_assets_from_db()
        self.load_traits_from_db()
        self.load_trait_relations_from_db()

    def load_assets_from_db(self):
        query = """
            select token_id, face_type, skin_color, inner_skin_color, lip_color, background_color
            from ops_assets_dev
            order by 1
        """
        self.assets = self.db_client.select_from_db(query, output="pandas")

    def load_traits_from_db(self):
        query = """
            select 
                ot.trait_id, 
                ot.value,
                ot.trait_count,
                ot.display_type
                from ops_traits ot
                where ot.trait_type = 'accessory'
                order by 1
        """
        self.traits = self.db_client.select_from_db(query, output="pandas")
        self.traits["display_type"] = self.traits["display_type"].apply(lambda s: s.replace("\r", ""))
        self.traits.index = self.traits.trait_id

    def load_trait_relations_from_db(self):
        query = """
            select
                   oad.token_id,
                   rel.trait_id,
                   ot.value,
                   ot.trait_count,
                   ot.display_type
                from ops_assets_traits_rel rel
                left join ops_assets_dev oad on rel.asset_id = oad.id
                left join ops_traits ot on rel.trait_id = ot.trait_id
                where rel.trait_id <= 87
                order by 1, 2
        """
        self.trait_relations = self.db_client.select_from_db(query, output="pandas")
        self.trait_relations["display_type"] = self.trait_relations["display_type"].apply(lambda s: s.replace("\r", ""))
        self.trait_relations = self.trait_relations.merge(self.layers[["layer", "order"]], how="left", left_on="display_type", right_on="layer")

    @staticmethod
    def hex_to_array(hex_num):
        dec_num = int(hex_num, 16)
        z = dec_num % 256
        dec_num = int(dec_num/256)
        y = dec_num % 256
        dec_num = int(dec_num/256)
        x = dec_num
        return np.array([x, y, z, 255])

    @staticmethod
    def merge_layer(low_layer_image, high_layer_image):
        low_layer_image = low_layer_image.astype(float)
        high_layer_image = high_layer_image.astype(float)
        new_image = high_layer_image.copy()
        for n in range(3):
            new_image[:, :, n] = (high_layer_image[:, :, 3] / 255.) * high_layer_image[:, :, n] + (1. - high_layer_image[:, :, 3] / 255.) * low_layer_image[:, :, n]
        new_image[:, :, 3] = np.max([high_layer_image[:, :, 3], low_layer_image[:, :, 3]], axis=0)
        new_image = np.round(new_image, 0)
        new_image = new_image.astype(np.uint8)

        return new_image

    def generate_png(self, token_id):
        asset = self.assets.loc[token_id]
        face_type = asset["face_type"]
        if face_type in ("Female", "Male"):
            skin_color = self.skin_color_map[asset["skin_color"]]
            detail_face_type = f"{face_type}{skin_color}"
        else:
            detail_face_type = face_type
        DIR = os.path.join(self.ROOT_DIR, face_type)
        traits_included = self.trait_relations[self.trait_relations.token_id == token_id].copy()
        if "Luxurious Beard" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"LuxuriousBeardLip", 0, "Lip", "Lip", 12]
        elif "Normal Beard" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"NormalBeardLip", 0, "Lip", "Lip", 12]
        elif "Normal Beard Black" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"NormalBeardBlackLip", 0, "Lip", "Lip", 12]
        traits_included.sort_index(inplace=True)

        background_color = self.hex_to_array(asset["background_color"])
        new_image = np.tile(background_color, (336, 336, 1)) #face.WIDTH, face.HEIGHT, 1))
        for n in range(1, self.layers.shape[0]):
            layer_name = self.layers.loc[n, "layer"]
            is_mandatory = self.layers.loc[n, "mandatory"]
            item = np.where(traits_included.layer == layer_name)[0]
            if len(item) > 0:
                item_name = traits_included.iloc[item[0]]["value"]
                item_name = item_name.replace(" ", "")
            elif is_mandatory:
                item_name = layer_name
            else:
                item_name = ""
            if item_name != "":
                filename = f"{detail_face_type}{item_name}.png"
                if not os.path.exists(os.path.join(DIR, filename)):
                    filename = f"{face_type}{item_name}.png"
                filepath = os.path.join(DIR, filename)
                with Image.open(filepath) as img:
                    layer_image = np.array(img.convert("RGBA"))
                new_image = self.merge_layer(new_image, layer_image)
                # if layer_name == "Beard" and item_name in ("LuxuriousBeard", "NormalBeardBlack", "NormalBeard"):
                #     traits_included.loc[0] = [token_id, 100, f"{item_name}Lip", 0, "Lip", "Lip", 12]
                #     traits_included.sort_index(inplace=True)
                # elif layer_name == "Beard" and item_name in ("ShadowBeard",):
                #     traits_included.loc[100000] = [token_id, 100, f"{item_name}Lip", 0, "Lip", "Lip", 12]
                #     traits_included.sort_index(inplace=True)
        new_img = Image.fromarray(new_image, "RGBA")
        new_img.save(f"image/test/newcryptopunk{token_id}.png")
        return new_image

    @staticmethod
    def compare_image(original_image, new_image):
        return np.all(original_image == new_image)

    @staticmethod
    def compare_image_weakly(original_image, new_image):
        return np.abs(original_image.astype(float) - new_image.astype(float)).max() <= 1.

    @staticmethod
    def load_original_image(token_id):
        ORIGINAL_IMAGE_DIR = os.path.join(os.path.realpath(os.curdir), "image/original_image")
        original_filepath = os.path.join(ORIGINAL_IMAGE_DIR, f"cryptopunk{token_id}.png")
        with Image.open(original_filepath) as img:
            original_image = np.array(img.convert("RGBA"))
        return original_image


if __name__ == "__main__":
    client = PngGenerator()
    for token_id in range(10000):
        new_image = client.generate_png(token_id)
        original_image = client.load_original_image(token_id)
        if not client.compare_image_weakly(original_image, new_image):
            print(token_id)
        if (token_id + 1) % 100 == 0:
            print(f"Done until {token_id}")

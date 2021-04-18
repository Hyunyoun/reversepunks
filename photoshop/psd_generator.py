import os
from PIL import Image

import numpy as np
import pandas as pd
import pytoshop
from pytoshop.layers import ChannelImageData
from pytoshop.user import nested_layers

from database import DBClient
from .png_generator import PngGenerator


class PsdGenerator(PngGenerator):

    def __init__(self):
        super().__init__()
        self.images_in_array = {}

    def generate_psd(self, token_id):
        asset = self.assets.loc[token_id]
        face_type = asset["face_type"]
        skin_color = self.skin_color_map[asset["skin_color"]]

        if face_type in ("Female", "Male"):
            skin_color = self.skin_color_map[asset["skin_color"]]
            detail_face_type = f"{face_type}{skin_color}"
        else:
            detail_face_type = face_type

        traits_included = self.trait_relations[self.trait_relations.token_id == token_id].copy()
        if "Luxurious Beard" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"LuxuriousBeardLip", 0, "Lip", "Lip", 12]
        elif "Normal Beard" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"NormalBeardLip", 0, "Lip", "Lip", 12]
        elif "Normal Beard Black" in traits_included.value.values:
            traits_included.loc[0] = [token_id, 100, f"NormalBeardBlackLip", 0, "Lip", "Lip", 12]
        traits_included.sort_index(inplace=True)

        
        trait_ids = self.trait_relations[self.trait_relations.token_id == token_id].trait_id.tolist()
        self.traits.loc[trait_ids]

        DIR = os.path.join(self.ROOT_DIR, face_type)


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

    def load_image(self, face_type, file_name):
        filepath = os.path.join(
            os.path.join(self.ROOT_DIR, face_type),
            f"{file_name}.png"
        )
        with Image.open(filepath) as img:
            img_array = np.array(img.convert("RGBA"))
        return img_array

    def load_all_images(self):
        face_types = ["Alien", "Ape", "Female", "Male", "Zombie"]
        images = {}
        for face_type in face_types:
            DIR = os.path.join(self.ROOT_DIR, face_type)
            png_files = [f for f in os.listdir(DIR) if f.split(".")[-1] == "png"]
            images[face_type] = {}
            for png_file in png_files:
                item_name = png_file.split(".")[0]
                images[face_type][item_name] = self.load_image(face_type, png_file)

        self.images_in_array = images

    def convert_image_to_layer(self, item_name, image_array):
        channels = {
            0: ChannelImageData(image_array[:, :, 0]),
            1: ChannelImageData(image_array[:, :, 1]),
            2: ChannelImageData(image_array[:, :, 2]),
            -1: ChannelImageData(image_array[:, :, 3])
        }
        return nested_layers.Image(
            name=item_name,
            visible=True,
            opacity=255,
            channels=channels,
            color_mode=pytoshop.enums.ColorMode.rgb.value
        )

    def convert_all_images_to_layers(self):
        layers = {}
        for face_type, images in self.images_in_array.items():
            layers[face_type] = {}
            for item_name, image_array in images.items():
                layers[face_type][item_name] = self.convert_image_to_layer(item_name, image_array)

        self.layers = layers

    def nested_layers_to_psd_file(self, layers, filepath):
        psd = nested_layers.nested_layers_to_psd(
            layers,
            pytoshop.enums.ColorMode.rgb.value,
            compression=0  # raw file
        )
        with open(filepath, "wb") as fd:
            psd.write(fd)

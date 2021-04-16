import os
from PIL import Image

import numpy as np
import pandas as pd

from traits import *
from database import DBClient


db_client = DBClient()

query = """
    select token_id, face_type, skin_color, inner_skin_color, lip_color, background_color
    from ops_assets_dev
    order by 1
"""
assets = db_client.select_from_db(query, output="pandas")

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
trait_relations = db_client.select_from_db(query, output="pandas")
trait_relations["display_type"] = trait_relations["display_type"].apply(lambda s: s.replace("\r", ""))

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
traits = db_client.select_from_db(query, output="pandas")
traits["display_type"] = traits["display_type"].apply(lambda s: s.replace("\r", ""))

layers = pd.DataFrame({
    "layer": ["Background", "Face", "Eyeballs", "SkinEffect", "EyeShadow", "Beard", "Eyes", "Earring", "Nose", "Lip", "Neck", "Mask", "Hair", "Hat", "EyesCover", "Cigar"],
    "mandatory": [True, True, True, False, True, False, True, False, True, True, False, False, False, False, False, False]
})
layers["order"] = range(layers.shape[0])

trait_relations = trait_relations.merge(layers[["layer", "order"]], how="left", left_on="display_type", right_on="layer")


def hex_to_array(hex_num):
    dec_num = int(hex_num, 16)
    z = dec_num % 256
    dec_num = int(dec_num/256)
    y = dec_num % 256
    dec_num = int(dec_num/256)
    x = dec_num
    return np.array([x, y, z, 255])


def merge_layer(low_layer_image, high_layer_image):
    new_image = high_layer_image.copy()
    for n in range(3):
        new_image[:, :, n] = (high_layer_image[:, :, 3] / 255.) * high_layer_image[:, :, n] + (1. - high_layer_image[:, :, 3] / 255.) * low_layer_image[:, :, n]
    new_image[:, :, 3] = np.max([high_layer_image[:, :, 3], low_layer_image[:, :, 3]], axis=0)
    return new_image


skin_color_map = {
    '0x713f1d': 'Brownie',
    '0xae8b61': 'Choco',
    '0xdbb180': 'Butter',
    '0xead9d9': 'Milk'
}

ROOT_DIR = os.path.join(os.path.realpath(os.curdir), "image/trait")



def generate_png(token_id, asset, trait_relations):
    face_type = asset["face_type"]
    if face_type in ("Female", "Male"):
        skin_color = skin_color_map[asset["skin_color"]]
        detail_face_type = f"{face_type}{skin_color}"
    else:
        detail_face_type = face_type
    DIR = os.path.join(ROOT_DIR, face_type)
    traits_included = trait_relations[trait_relations.token_id == token_id].copy()
    background_color = hex_to_array(asset["background_color"])
    new_image = np.tile(background_color, (336, 336, 1)) #face.WIDTH, face.HEIGHT, 1))
    for n in range(1, layers.shape[0]):
        layer_name = layers.loc[n, "layer"]
        is_mandatory = layers.loc[n, "mandatory"]
        item = np.where(traits_included.layer == layer_name)[0]
        if len(item) > 0:
            item_name = traits_included.iloc[item[0]]["value"]
            item_name = item_name.replace(" ", "")
        elif is_mandatory:
            item_name = layer_name
        filename = f"{detail_face_type}{item_name}.png"
        if not os.path.exists(os.path.join(DIR, filename)):
            filename = f"{face_type}{item_name}.png"
        filepath = os.path.join(DIR, filename)
        with Image.open(filepath) as img:
            layer_image = np.array(img.convert("RGBA"))
        new_image = merge_layer(new_image, layer_image)
        if layer_name == "Beard" and item_name in ("LuxuriousBeard", "ShadowBeard"):
            traits_included.loc[100] = [token_id, 100, "Beard Lip", 0, "Lip", "Lip", 6]
        #     print(traits_included)
        # print(layer_name)
        # print(filename)
        # print(layer_image[176, 147])
        # print(new_image[176, 147])
    new_img = Image.fromarray(new_image, "RGBA")
    new_img.save(f"test/newcryptopunk{token_id}.png")
    return new_image


def compare_image(original_image, new_image):
    return np.all(original_image == new_image)


def load_original_image(token_id):
    ORIGINAL_IMAGE_DIR = os.path.join(os.path.realpath(os.curdir), "image/original_image")
    original_filepath = os.path.join(ORIGINAL_IMAGE_DIR, f"cryptopunk{token_id}.png")
    with Image.open(original_filepath) as img:
        original_image = np.array(img.convert("RGBA"))
    return original_image


# 8

for token_id in range(15, 20):
    asset = assets.loc[token_id]
    new_image = generate_png(token_id, asset, trait_relations)
    original_iamge = load_original_image(token_id)
    print(compare_image(original_iamge, new_image))



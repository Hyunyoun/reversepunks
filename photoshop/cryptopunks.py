import requests
from PIL import Image

import numpy as np


url = "https://www.larvalabs.com/cryptopunks/cryptopunk49.png"
url = "https://www.larvalabs.com/cryptopunks/cryptopunk340.png"

img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")

imga = np.array(img)

img_width, img_height, _ = imga.shape

bkg_color = imga[0, 0].copy()
trp_color = np.array([255, 255, 255, 0])

# extract background
imga_bkg = np.tile(bkg_color, (img_width, img_height, 1))

# extract entire face
imga_1 = imga.copy()
for x in range(img_width):
    for y in range(img_height):
        if np.all(imga_1[x, y] == bkg_color):
            imga_1[x, y] = trp_color

# extract face
imga_1 = imga.copy()
for x in range(img_width):
    for y in range(img_height):
        if np.all(imga_1[x, y] == bkg_color):
            imga_1[x, y] = trp_color

# extract hair
imga_1 = imga.copy()
for x in range(img_width):
    for y in range(img_height):
        if np.all(imga_1[x, y] == bkg_color):
            imga_1[x, y] = trp_color




Image.fromarray(imga_1, 'RGBA').save("cryptopunk49_face.png")
Image.fromarray(imga_bkg, 'RGBA').save("cryptopunk49_background.png")

query = """
select asset.token_id,
       asset.image_url
    from ops_assets_dev asset
    left join ops_assets_traits_rel rel
    on asset.id = rel.asset_id
    left join ops_traits tr
    on rel.trait_id = tr.trait_id
    where tr.trait_id = 90
    order by asset.token_id, tr.trait_type, tr.value
"""
tokens = dbclient.select_from_db(query)


from traits import *
image_dir = "image/original_image"

# Alien
url = 'https://lh3.googleusercontent.com/Ucp7lgM8wMYQxANGs7T1XkCSI-HMM3LaBbLT9KdylBYYgMgFVMFROp_00ud52jRwB_IVTgLtS7C4mcFiBe1IAFrb'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Alien()
img_face = face.extract_face(img_array)
img_face.save("image/trait/AlienFace.png")

# Ape
url = 'https://lh3.googleusercontent.com/qN_jN9N7tuFPacxyt_jBhrC5i2WpGmcpI2N6f1E5GwLbXsyD-qi-gBbJIj22QbQdnEX7McoGjDBa9mWxLmqBRPJA'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Ape()
img_face = face.extract_face(img_array)
img_face.save("image/trait/ApeFace.png")

# Female
url = 'https://lh3.googleusercontent.com/4-e48Wxk4DZ_9WNiIb6fF4zN3eI97AFG1JF-u1E6dJdMefbWSrx8OLwXO3lktmUknDt3cGwgrGlmHPsGd8Q1-17T5A8zcjujD6VuGA'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Female()
img_face = face.extract_face(img_array)
img_face.save("image/trait/FemaleDarkFace.png")

# Male
url = 'https://lh3.googleusercontent.com/7bRocEaoBrWYBX3vThkHj4kAV3b3mKG-Kem85xeT-D8oHpvQ19kcoiBd9mIFeNU0GrwZGvj6Oc5NAEGBSsGlrww'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Male()
img_face = face.extract_face(img_array)
img_face.save("male_face.png")

# Zombie
token_id = "1374"
filename = f"cryptopunk{token_id}.png"
filepath = os.path.join(image_dir, filename)
with Image.open(filepath) as img:
    img_array = np.array(img.convert("RGBA"))

face = Zombie()
img_face = face.extract_face(img_array)
img_face.save("image/trait/ZombieFace.png")

img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Alien()
# face = Ape()
# face = Female()
img_face = face.extract_face(img_array)
img_face.save("alien_face.png")
img_face.save("alien_face.png")


count = 0
for tokenid, url in tokens[8000:]:
    img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
    img.save(f"image/cryptopunk{tokenid}.png")
    count += 1
    if count % 20 == 0:
        print(tokenid)

traits_rel

PIXEL_PER_DOT = 14
DOT_WIDTH = 24
DOT_HEIGHT = 24


def find_array(img_array, x, y):
    pos = []
    color = img_array[x*PIXEL_PER_DOT, y*PIXEL_PER_DOT]
    for i in range(DOT_WIDTH):
        found = False
        for j in range(DOT_HEIGHT):
            if not found:
                if np.all(img_array[i*PIXEL_PER_DOT, j*PIXEL_PER_DOT] == color):
                    start = j
                    found = True
            else:  # found
                if not np.all(img_array[i*PIXEL_PER_DOT, j*PIXEL_PER_DOT] == color):
                    end = j
                    pos.append([i, i+1, start, end])
                    found = False
        if found:
            pos.append([i, i+1, start, DOT_HEIGHT])
    return pos


def find_new_color_pos(img_array):
    bkg_color = img_array[0, 0]
    for i in range(DOT_WIDTH):
        for j in range(DOT_HEIGHT):
            if not np.all(img_array[i*PIXEL_PER_DOT, j*PIXEL_PER_DOT] == bkg_color):
                return i, j
    return 0, 0







traits.loc[np.where(pd.isnull(traits.display_type))].loc[:86]

trait_id = 43
print(traits_rel[np.logical_and(traits_rel.trait_id == trait_id, traits_rel.token_type == "Female")].iloc[:20])
print(traits_rel[np.logical_and(traits_rel.trait_id == trait_id, traits_rel.token_type != "Female")].iloc[:20])
# print(traits_rel[traits_rel.trait_id == trait_id].iloc[:20])

token_id = 436
url = assets[assets.token_id == str(token_id)].iloc[0]["image_url"]
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
x, y = find_new_color_pos(img_array)
# pos = find_array(img_array, x, y)
pos = find_array(img_array, 23, 9)
for subpos in pos:
    print(subpos, ",")

traits.loc[trait_id, "display_type"] = "mask"


pd.isnull(traits.display_type).sum() - 5


traits_rel[traits_rel.token_id == '70']


import os
image_dir = "image/original_image"

face_types = ["Female", "Male", "Ape", "Alien", "Zombie"]
for face_type in face_types:

face_type = face_types[1]
hex_color_set = set()
sub_assets = assets[assets.face_type == face_type]
for idx in sub_assets.index:
    token_id = sub_assets.loc[idx, "token_id"]
    # print(token_id)
    filename = f"cryptopunk{token_id}.png"
    filepath = os.path.join(image_dir, filename)
    with Image.open(filepath) as img:
        img_array = np.array(img.convert("RGBA"))
        color = img_array[7*PIXEL_PER_DOT, 8*PIXEL_PER_DOT]
        hex_color = hex(color[0] * 256 * 256 + color[1] * 256 + color[2])
        # if color_hash != 1467042303:
        #     print(token_id)
        #     print(color)
        if hex_color not in hex_color_set:
            hex_color_set.add(hex_color)

assert(len(hex_color_set) == 1)
idxs = np.where(assets.face_type == face_type)[0]
assets.loc[idxs, "inner_skin_color"] = hex_color


for idx in assets.index:
    token_id = assets.loc[idx, "token_id"]
    # print(token_id)
    filename = f"cryptopunk{token_id}.png"
    filepath = os.path.join(image_dir, filename)
    with Image.open(filepath) as img:
        img_array = np.array(img.convert("RGBA"))
        color = img_array[20*PIXEL_PER_DOT, 12*PIXEL_PER_DOT]
        hex_color = hex(color[0] * 256 * 256 + color[1] * 256 + color[2])
        assets.loc[idx, "skin_color"] = hex_color
        color = img_array[0, 0]
        hex_color = hex(color[0] * 256 * 256 + color[1] * 256 + color[2])
        assets.loc[idx, "background_color"] = hex_color

face_type = "Male"
skin_colors = list(np.unique(assets[assets.face_type == face_type].skin_color))

skin_color = skin_colors[3]
print(skin_color)
assets[np.logical_and(assets.face_type == face_type, assets.skin_color == skin_color)].iloc[:30]

token_id = 8437
# print(token_id)
filename = f"cryptopunk{token_id}.png"
filepath = os.path.join(image_dir, filename)
with Image.open(filepath) as img:
    img_array = np.array(img.convert("RGBA"))
    color = img_array[18*PIXEL_PER_DOT, 12*PIXEL_PER_DOT]
    hex_color = hex(color[0] * 256 * 256 + color[1] * 256 + color[2])
    print(hex_color)


idxs = np.where(np.logical_and(assets.face_type == face_type, assets.skin_color == skin_color))[0]
len(idxs)
assets.loc[idxs, "lip_color"] = hex_color


token_id = 5633
traits_rel[traits_rel.token_id == str(token_id)]

count = {
    "0x281b09": 0,
    "0x0": 0,
    "0x692f08": 0,
    "0x86581e": 0,
    "0xc9c9c9": 0
}

for skin_color in skin_colors[:1]:
    token_ids = list(assets[np.logical_and(assets.face_type == face_type, assets.skin_color == skin_color)]["token_id"])
    hex_color_set = set()
    for token_id in token_ids:
        relations = traits_rel[traits_rel.token_id == str(token_id)]
        rels = []
        for rel in list(relations["trait_value"]):
            rels += rel.split(" ")
        if "Lipstick" in rels:
            continue
        # print(token_id)
        filename = f"cryptopunk{token_id}.png"
        filepath = os.path.join(image_dir, filename)
        with Image.open(filepath) as img:
            img_array = np.array(img.convert("RGBA"))
            color = img_array[18*PIXEL_PER_DOT, 12*PIXEL_PER_DOT]
            hex_color = hex(color[0] * 256 * 256 + color[1] * 256 + color[2])
            # print(hex_color)
            # if hex_color == "0xc9c9c9":
            #     print(token_id)
            hex_color_set.add(hex_color)
        count[hex_color] += 1

    print(skin_color)
    print(hex_color_set)

idxs = np.where(np.logical_and(assets.face_type == face_type, assets.skin_color == skin_color))[0]
len(idxs)
assets.loc[idxs, "lip_color"] = hex_color

hex_color = "0x0"
idxs = np.where(assets.lip_color == "")[0]
assets.loc[idxs, "lip_color"] = hex_color



def to_hex(color_array):
    return hex(color_array[0]*256*256 + color_array[1]*256 + color_array[2])

skin_colors = ['0x713f1d', '0xae8b61', '0xdbb180', '0xead9d9']
skin_color = "0xead9d9"
assets[assets.skin_color == skin_color]

inner_skin_color = "0xffffff"
token_ids = list(assets[np.logical_and(assets.skin_color == skin_color, assets.face_type == "Female")]["token_id"])
for token_id in token_ids:
    filename = f"cryptopunk{token_id}.png"
    filepath = os.path.join(image_dir, filename)
    with Image.open(filepath) as img:
        img_array = np.array(img.convert("RGBA"))
    if to_hex(img_array[23*PIXEL_PER_DOT, 9*PIXEL_PER_DOT]) == skin_color:
        if to_hex(img_array[9*PIXEL_PER_DOT, 9*PIXEL_PER_DOT]) == inner_skin_color:
            face = Female()
            img_face = face.extract_face(img_array)
            img_face.save("image/trait/FemaleWhiteFace.png")
            break

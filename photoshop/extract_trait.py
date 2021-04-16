import os
from PIL import Image

import numpy as np

from traits import *
from database import DBClient






def call_trait(value):
    if value == '3D Glasses':
        return ThreeDGlasses()
    elif value == 'Bandana':
        return Bandana()
    elif value == 'Beanie':
        return Beanie()
    elif value == 'Big Beard':
        return BigBeard()
    elif value == 'Big Shades':
        return BigShades()
    elif value == 'Black Lipstick':
        return Lipstick()
    elif value == 'Blonde Bob':
        return BlondeBob()
    elif value == 'Blonde Short':
        return BlondeShort()
    elif value == 'Blue Eye Shadow':
        return ColoredEyeShadow()
    elif value == 'Buck Teeth':
        return BuckTeeth()
    elif value == 'Cap':
        return Cap()
    elif value == 'Cap Forward':
        return CapForward()
    elif value == 'Chinstrap':
        return Chinstrap()
    elif value == 'Choker':
        return Choker()
    elif value == 'Cigarette':
        return Cigarette()
    elif value == 'Classic Shades':
        return ClassicShades()
    elif value == 'Clown Eyes Blue':
        return ClownEyes()
    elif value == 'Clown Eyes Green':
        return ClownEyes()
    elif value == 'Clown Hair Green':
        return ClownHair()
    elif value == 'Clown Nose':
        return ClownNose()
    elif value == 'Cowboy Hat':
        return CowboyHat()
    elif value == 'Crazy Hair':
        return CrazyHair()
    elif value == 'Dark Hair':
        return DarkHair()
    elif value == 'Do-rag':
        return DoRag()
    elif value == 'Earring':
        return Earring()
    elif value == 'Eye Mask':
        return EyeMask()
    elif value == 'Eye Patch':
        return EyePatch()
    elif value == 'Fedora':
        return Fedora()
    elif value == 'Front Beard':
        return FrontBeard()
    elif value == 'Front Beard Dark':
        return FrontBeardDark()
    elif value == 'Frown':
        return Frown()
    elif value == 'Frumpy Hair':
        return FrumpyHair()
    elif value == 'Goat':
        return Goat()
    elif value == 'Gold Chain':
        return GoldChain()
    elif value == 'Green Eye Shadow':
        return ColoredEyeShadow()
    elif value == 'Half Shaved':
        return HalfShaved()
    elif value == 'Handlebars':
        return Handlebars()
    elif value == 'Headband':
        return Headband()
    elif value == 'Hoodie':
        return Hoodie()
    elif value == 'Horned Rim Glasses':
        return HornedRimGlasses()
    elif value == 'Hot Lipstick':
        return Lipstick()
    elif value == 'Knitted Cap':
        return KnittedCap()
    elif value == 'Luxurious Beard':
        return LuxuriousBeard()
    elif value == 'Medical Mask':
        return MedicalMask()
    elif value == 'Messy Hair':
        return MessyHair()
    elif value == 'Mohawk':
        return Mohawk()
    elif value == 'Mohawk Dark':
        return MohawkDark()
    elif value == 'Mohawk Thin':
        return MohawkThin()
    elif value == 'Mole':
        return Mole()
    elif value == 'Mustache':
        return Mustache()
    elif value == 'Muttonchops':
        return Muttonchops()
    elif value == 'Nerd Glasses':
        return NerdGlasses()
    elif value == 'Normal Beard':
        return NormalBeard()
    elif value == 'Normal Beard Black':
        return NormalBeardBlack()
    elif value == 'Orange Side':
        return OrangeSide()
    elif value == 'Peak Spike':
        return PeakSpike()
    elif value == 'Pigtails':
        return Pigtails()
    elif value == 'Pilot Helmet':
        return PilotHelmet()
    elif value == 'Pink With Hat':
        return PinkWithHat()
    elif value == 'Pipe':
        return Pipe()
    elif value == 'Police Cap':
        return PoliceCap()
    elif value == 'Purple Eye Shadow':
        return ColoredEyeShadow()
    elif value == 'Purple Hair':
        return PurpleHair()
    elif value == 'Purple Lipstick':
        return Lipstick()
    elif value == 'Red Mohawk':
        return RedHohawk()
    elif value == 'Regular Shades':
        return RegularShades()
    elif value == 'Rosy Cheeks':
        return RosyCheeks()
    elif value == 'Shadow Beard':
        return ShadowBeard()
    elif value == 'Shaved Head':
        return ShavedHead()
    elif value == 'Silver Chain':
        return SilverChain()
    elif value == 'Small Shades':
        return SmallShades()
    elif value == 'Smile':
        return Smile()
    elif value == 'Spots':
        return Spots()
    elif value == 'Straight Hair':
        return StraightHair()
    elif value == 'Straight Hair Blonde':
        return StraightHairBlonde()
    elif value == 'Straight Hair Dark':
        return StraightHairDark()
    elif value == 'Stringy Hair':
        return StringyHair()
    elif value == 'Tassle Hat':
        return TassleHat()
    elif value == 'Tiara':
        return Tiara()
    elif value == 'Top Hat':
        return TopHat()
    elif value == 'VR':
        return VR()
    elif value == 'Vampire Hair':
        return VampireHair()
    elif value == 'Vape':
        return Vape()
    elif value == 'Welding Goggles':
        return WeldingGoggles()
    elif value == 'Wild Blonde':
        return WildBlonde()
    elif value == 'Wild Hair':
        return WildHair()
    elif value == 'Wild White Hair':
        return WildWhiteHair()



db_client = DBClient()

query = """
    select token_id, face_type, skin_color, inner_skin_color, lip_color
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


trait_ids = traits["trait_id"].tolist()

image_dir = "image/original_image"
save_dir = "image/trait/candidate"


# for trait_id in trait_ids[10:]:
for trait_id in [86]:
    value = traits[traits.trait_id == trait_id].iloc[0]["value"]
    value_r = value.replace(" ", "")
    tmp_save_dir = os.path.join(save_dir, value_r)
    os.mkdir(tmp_save_dir)
    trait = call_trait(value)
    token_ids = trait_relations.loc[np.where(trait_relations.trait_id == trait_id)[0]]["token_id"].tolist()
    for token_id in token_ids:
        face_type = assets.loc[token_id, "face_type"]
        if face_type == "Female":
            face = Female()
        elif face_type == "Male":
            face = Male()
        elif face_type == "Zombie":
            face = Zombie()
        elif face_type == "Ape":
            face = Ape()
        elif face_type == "Alien":
            face = Alien()
        pos = trait.get_pos(face.face_type)
        filename = f"cryptopunk{token_id}.png"
        filepath = os.path.join(image_dir, filename)
        with Image.open(filepath) as img:
            img_array = np.array(img.convert("RGBA"))
        # component_types = ["Eyes", "Eyeballs", "Eyebrows", "Nose", "Lip"]
        comp = face.extract_component(img_array, pos)
        savefilepath = os.path.join(tmp_save_dir, f"{face_type}{value.replace(' ', '')}{token_id}.png")
        comp.save(savefilepath)



curdir = os.path.realpath(os.curdir)
DIR = os.path.join(curdir, save_dir)

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR, f)) and f[-3:] == "png"]

for filename in onlyfiles:
    newfilename = ''.join([i for i in filename if not i.isdigit()])
    os.rename(os.path.join(DIR, filename), os.path.join(DIR, newfilename))


value = "Vape"
value_r = value.replace(" ", "")
trait = call_trait(value)
# tmp_save_dir = os.path.join(save_dir, value)

face_type = "Male"
token_id = 9836
filename = f"cryptopunk{token_id}.png"
filepath = os.path.join(image_dir, filename)
with Image.open(filepath) as img:
    img_array = np.array(img.convert("RGBA"))

poslist = trait.get_pos(face_type)
new_img_array = np.tile(face.TRANSPARENT_COLOR, (face.WIDTH, face.HEIGHT, 1))
# pos = poslist[0]
# color = img_array[pos[1] * 14 - 1, pos[3] * 14 - 1]
for pos in poslist[:-4]:
    color = img_array[pos[0] * 14, pos[2] * 14]
    new_img_array[pos[0] * face.PIXEL_PER_DOT:pos[1] * face.PIXEL_PER_DOT, pos[2] * face.PIXEL_PER_DOT:pos[3] * face.PIXEL_PER_DOT] = color


for pos in poslist[-4:]:
    color = np.array([185, 185, 185, 128])
    new_img_array[pos[0] * face.PIXEL_PER_DOT:pos[1] * face.PIXEL_PER_DOT, pos[2] * face.PIXEL_PER_DOT:pos[3] * face.PIXEL_PER_DOT] = color


savefilepath = os.path.join(save_dir, f"{face_type}{value_r}.png")
comp = Image.fromarray(new_img_array.astype(np.uint8), 'RGBA')
comp.save(savefilepath)


old = ["Brown", "Milk", "Pink", "Yellow"]
new = ["Brownie", "Butter", "Milk", "Choco"]
skin_colors = ['0x713f1d', '0xae8b61', '0xdbb180', '0xead9d9']


curdir = os.path.realpath(os.curdir)
DIR = os.path.join(curdir, "image/trait/Male")

from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(DIR) if isfile(join(DIR, f)) and f[-3:] == "png"]

for filename in onlyfiles:
    newfilename = filename
    for n in range(4):
        newfilename = newfilename.replace(old[n], new[n])
    if filename != newfilename:
        os.rename(os.path.join(DIR, filename), os.path.join(DIR, newfilename))


def to_hex(array):
    return hex(array[0]*256*256 + array[1]*256 + array[2])

colors = {}
for color in skin_colors:
    colors[color] = {}

trait_id = 15
value = "Cigarette"
value_r = value.replace(" ", "")
trait = call_trait(value)
token_ids = trait_relations.loc[np.where(trait_relations.trait_id == trait_id)[0]]["token_id"].tolist()
# tmp_save_dir = os.path.join(save_dir, value)

for token_id in token_ids:
    face_type = assets.loc[token_id, "face_type"]
    if face_type != "Male":
        continue
    skin_color = assets.loc[token_id, "skin_color"]
    filename = f"cryptopunk{token_id}.png"
    filepath = os.path.join(image_dir, filename)
    with Image.open(filepath) as img:
        img_array = np.array(img.convert("RGBA"))
    poslist = trait.get_pos(face_type)
    pos = poslist[-1]
    color = img_array[pos[0]*14, pos[2]*14]
    hex_color = to_hex(color)
    if hex_color in colors[skin_color]:
        colors[skin_color][hex_color].append(token_id)
    else:
        colors[skin_color][hex_color] = [token_id]

for k, v in colors.items():
    print(k)
    for vk, vv in v.items():
        print(vk, vv)


# color = img_array[pos[1] * 14 - 1, pos[3] * 14 - 1]
for pos in poslist:
    color = img_array[pos[1] * 14 - 1, pos[3] * 14 - 1]
    new_img_array[pos[0] * face.PIXEL_PER_DOT:pos[1] * face.PIXEL_PER_DOT, pos[2] * face.PIXEL_PER_DOT:pos[3] * face.PIXEL_PER_DOT] = color

savefilepath = os.path.join(save_dir, f"{face_type}{value_r}.png")
comp = Image.fromarray(new_img_array.astype(np.uint8), 'RGBA')
comp.save(savefilepath)

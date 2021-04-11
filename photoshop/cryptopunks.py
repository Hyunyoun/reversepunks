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

# Alien
url = 'https://lh3.googleusercontent.com/Ucp7lgM8wMYQxANGs7T1XkCSI-HMM3LaBbLT9KdylBYYgMgFVMFROp_00ud52jRwB_IVTgLtS7C4mcFiBe1IAFrb'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Alien()
img_face = face.extract_face(img_array)
img_face.save("alien_face.png")

# Ape
url = 'https://lh3.googleusercontent.com/qN_jN9N7tuFPacxyt_jBhrC5i2WpGmcpI2N6f1E5GwLbXsyD-qi-gBbJIj22QbQdnEX7McoGjDBa9mWxLmqBRPJA'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Ape()
img_face = face.extract_face(img_array)
img_face.save("ape_face.png")

# Female
url = 'https://lh3.googleusercontent.com/4-e48Wxk4DZ_9WNiIb6fF4zN3eI97AFG1JF-u1E6dJdMefbWSrx8OLwXO3lktmUknDt3cGwgrGlmHPsGd8Q1-17T5A8zcjujD6VuGA'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Female()
img_face = face.extract_face(img_array)
img_face.save("female_face.png")

# Male
url = 'https://lh3.googleusercontent.com/7bRocEaoBrWYBX3vThkHj4kAV3b3mKG-Kem85xeT-D8oHpvQ19kcoiBd9mIFeNU0GrwZGvj6Oc5NAEGBSsGlrww'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Male()
img_face = face.extract_face(img_array)
img_face.save("male_face.png")

# Zombie
url = 'https://lh3.googleusercontent.com/bJwri72563TNKZLcC3w1uZpfq9fI_yjdddhBrS4S7KksD8m4P4JxB3v49LDA4K7L3sHzjAd89lnQLSnUfgPCjaZVGw'
img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Zombie()
img_face = face.extract_face(img_array)
img_face.save("zombie_face.png")

img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
img_array = np.array(img)
face = Alien()
# face = Ape()
# face = Female()
img_face = face.extract_face(img_array)
img_face.save("alien_face.png")
img_face.save("alien_face.png")


count = 0
for tokenid, url in tokens[:100]:
    img = Image.open(requests.get(url, stream=True).raw).convert("RGBA")
    img.save(f"image/Female/cryptopunk{tokenid}.png")
    if (count+1) % 10 == 0:
        print(tokenid)

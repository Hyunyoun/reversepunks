
import time
import requests

import pandas as pd

from opensea import OpenseaClient


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

o_client = OpenseaClient()

contract_addresses = {
    "cryptopunks": "0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb"
}

t_0 = time.time()
assets = []
for n in range(0, 200):
    kwargs = {
        "asset_contract_address": contract_addresses.get("cryptopunks"),
        "token_ids": list(range(n*50, (n+1)*50)),
        "order_by": "token_id",
        "order_direction": "asc",
        "offset": "0",
        "limit": "50"
    }
    response = o_client.retrieve_assets(**kwargs)
    sub_assets = response.get("assets")
    assets += sub_assets
    print(f"{n+1} - {(time.time() - t_0):.2f} sec elapsed")


assets_frame = pd.DataFrame(assets)

int_columns = ["token_id"]
assets_frame["token_id"] = assets_frame["token_id"].astype(int)
assets_frame.sort_values("token_id", inplace=True)
assets_frame.reset_index(drop=True, inplace=True)

assets_frame["owner_address"] = assets_frame["owner"].apply(lambda dct: dct.get("address"))

traits = []
for n in assets_frame.index:
    asset_id = assets_frame.loc[n, "id"]
    for trait in assets_frame.loc[n, "traits"]:
        traits.append([asset_id, f'{trait.get("trait_type")}{trait.get("value")}'])


traits = []
trait_key = set()
for n in range(assets.shape[0]):
    for t in assets.loc[n, 'traits']:
        if t["value"] not in trait_key:
            trait_key.add(t["value"])
            traits.append(t)

print(len(traits))



traits_vk = {}
for n in range(traits.shape[0]):
    traits_vk[traits.loc[n, "value"]] = traits.loc[n, "trait_id"]

traits_rel = []
for n in range(assets.shape[0]):
    for t in assets.loc[n, 'traits']:
        traits_rel.append([
            assets.loc[n, "token_id"],
            t["value"],
            traits_vk[t["value"]],
            assets.loc[n, "image_url"]
        ])

for n in
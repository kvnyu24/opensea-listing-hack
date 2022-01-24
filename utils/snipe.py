import requests
import json
import csv
import os


ORDER_API = "https://ethereum-api.rarible.org/v0.1/order/orders/sell/byMakerAndByStatus?status=ACTIVE&maker="
OWNER_API = "https://api-mainnet.rarible.com/marketplace/api/v4/items/" 

collection_map = {
    "BAYC": {
            "address":"0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d",
            "owners": "./data/owners_BAYC.csv",
            "orders": ".//data/orders_BAYC.csv",
            "num": 10000
        },
    "Meebits": {
            "address":"0x7bd29408f11d2bfc23c34f18275bbf23bb716bc7",
            "owners": "./data/owners_meebits.csv",
            "orders": "./data/orders_meebits.csv",
            "num": 20000
        },
    "Azuki": {
        "address":"0xed5af388653567af2f388e6224dc7c4b3241c544",
        "owners": "./data/owners_azuki.csv",
        "orders": "../data/orders_azuki.csv",
        "num": 10000
        },
    "CryptoCoven": {
            "address":"0x5180db8f5c931aae63c74266b211f580155ecac8",
            "owners": "./data/owners_crypto_coven.csv",
            "orders": "./data/orders_crypto_coven.csv",
            "num": 9999
        },
    "WoW": {
            "address":"0xe785e82358879f061bc3dcac6f0444462d4b5330",
            "owners": "./data/owners_wow.csv",
            "orders": "./data/orders_wow.csv",
            "num": 10000
        },
    "Doodle": {
            "address":"0x8a90cab2b38dba80c64b7734e58ee1db38b8992e",
            "owners": "./data/owners_doodle.csv",
            "orders": "./data/orders_doodle.csv",
            "num": 10000
        },



}

def init_file(owner_file, order_file):
    if not os.path.exists(owner_file):
        with open(owner_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["owner"])
    if not os.path.exists(order_file):
        with open(order_file, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["owner", "id", "price"])

def scrape_owner(address, id, owner_file):
    API = OWNER_API + address + "%3A" + str(id) + "/ownerships"
    r = json.loads(requests.get(API).content)
    owner = list(r)[0]["owner"]
    with open(owner_file, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([owner])
        print("writing {}th owner: ".format(id) + owner)

    return owner

def scrape_order(owner, address, order_file):
    r = requests.get(ORDER_API + owner)
    orders = json.loads(r.content)["orders"]
    for order in orders:
        contract = order["make"]["assetType"]["contract"]
        token_id = order["make"]["assetType"]["tokenId"]
        if (contract == address):
            price = order["makePrice"]
            with open(order_file, "a", newline='') as f:
                writer = csv.writer(f)
                writer.writerow([owner, token_id, price])
                print("Order of id {} has price {}".format(token_id, price))
        else:
            pass

def pipeline(collection, start):
    collection_config = collection_map[collection]
    owner_file = collection_config["owners"]
    order_file = collection_config["orders"]
    address = collection_config["address"]
    init_file(owner_file, order_file)
    for i in range(start, collection_config["num"]):
        try:
            owner = scrape_owner(address, i, owner_file)
            scrape_order(owner, address, order_file)
        except Exception as e:
            pass

# if __name__ == "__main__":
    # pipeline("BAYC", 536)

from mapping_template import mapping_template_name as my_mapping_template
from get_image_url import add_image

class NewWszystkoplProduct:
    def init(self, access_token, allegro_product):
        self.id = allegro_product['id']
        self.is_draft = False
        self.category_id = self.__get_category_id(my_mapping_template, allegro_product['category']['id'])
        self.name = allegro_product['name']
        self.old_images_to_new = add_image(access_token, allegro_product['images'])
        self.images = [img for img in self.old_images_to_new.values()]
        self.description = self.__adjust_scheme_description(allegro_product["description"]['sections'])
        self.ean = self.__set_parameter(allegro_product, "EAN (GTIN)")
        self.sku = self.__set_parameter(allegro_product, "Kod producenta")
        self.externalReferences = [{ "id": self.id, "kind": "allegro" }]
        self.externalCategories = [{"source": "allegro", "breadcrumb": [{"id": allegro_product['category']['id']}]}]
        self.externalAttributes = self.add_allegro_params(allegro_product["productSet"][0]["product"]["parameters"])
        self.price = float(allegro_product["sellingMode"]["price"]["amount"])
        self.stock = int(allegro_product["stock"]["available"])
        self.status = allegro_product['publication']["status"]
        self.data = {
            "name": self.name,
            "description": self.description,
            "ean": self.ean,
            "sku": self.sku,
            "externalReferences": self.externalReferences,
            "externalCategories": self.externalCategories,
            "externalAttributes": self.externalAttributes,
            "images": self.images,
            "price": self.price,
            "stock": self.stock,
            "dispatchTime": {"period": 1},
            "weight": 50, 
            "deliveryPriceList": "SMART",
            "status": "active" if self.status.lower() == "active" else "inactive"
        }

def __set_parameter(self, product, name):
    parameters = product["productSet"][0]["product"]["parameters"]
    for param in parameters:
        if param.get("name") == name:
            return param["values"][0]
        

def add_allegro_params(self, parameters):
    data = []
    for param in parameters:
        if param["name"] in ["EAN (GTIN)"]:
            continue
        data.append({
            "source": "allegro",
            "id": param["id"],
            "name": param["name"],
            "type": "string",
            "values": param["values"],
        })
    data.append({
        "source": "allegro",
        "id": "11323",
        "name": "Stan",
        "type": "string",
        "values": ["Nowy"],
    })
    return data

def __adjust_scheme_description(self, description: list[dict]):
    # changes the name of content | url key to value and sets img urls to wszystkopl url
    new_description = []
    for items in description:
        new_items = []
        for item in items['items']:
            new_item = {}
            for the_key, value in item.items():
                if the_key != "type":
                    # create 'value' key with the value of content | url key
                    if the_key == "url":
                    # update allegro img with the new url
                        new_item["value"] = self.old_images_to_new[value]
                    else:
                        new_item["value"] = value
                else:
                    new_item[the_key] = value
            new_items.append(new_item)
        new_description.append({'items': new_items})
    return new_description

def __get_category_id(self, mapping_template:list[dict], allegro_category_id: str) -> int:
    for category in mapping_template:
        if category['id'] == allegro_category_id:
            return int(category['wszystko_id'])
    # if the category is not found set product as a draft and return default category which is 0
    self.__set_as_draft()
    return 0

def __set_as_draft(self) -> None:
    self.is_draft = True
        





        



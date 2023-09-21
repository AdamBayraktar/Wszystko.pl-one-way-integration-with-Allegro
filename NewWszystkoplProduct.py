from get_image_url import add_image
from variables.mapping_auto_template_finished_with_params import mapped_categories as my_mapping_template

# improve the performance of the image search function
# refactor the code

class NewWszystkoplProduct:
    def __init__(self, wszystkopl_access_token, allegro_product):
        self.allegro_product = allegro_product
        self.id = allegro_product['id']
        self.is_draft = False
        self.category_id = self.__get_category_id(my_mapping_template, allegro_product['category']['id'])
        self.name = allegro_product['name']
        self.old_images_to_new = add_image(wszystkopl_access_token, allegro_product['images'])
        # self.images = [img for img in self.old_images_to_new.values()]
        self.images = [list(img.values())[0] for img in self.old_images_to_new]
        self.description = self.__adjust_scheme_description(allegro_product["description"]['sections'])
        self.ean = self.__set_parameter("EAN (GTIN)")
        self.sku = str(self.__set_parameter("Kod producenta"))
        self.brand = self.__set_parameter("Marka")
        self.externalReferences = [{ "id": self.id, "kind": "allegro" }]
        self.externalCategories = [{"source": "allegro", "breadcrumb": [{"id": allegro_product['category']['id']}]}]
        self.externalAttributes = self.add_allegro_params(allegro_product["productSet"][0]["product"]["parameters"])
        self.price = float(allegro_product["sellingMode"]["price"]["amount"])
        self.stock = int(allegro_product["stock"]["available"]) if int(allegro_product["stock"]["available"]) > 0 else 1
        self.status = 'active' if allegro_product['publication']["status"].lower() == 'active' else 'ended' 
        if self.status != 'active':
            print(f"this should be inactive!!!\n{self.name}")
            self.__set_as_draft()
        # check categories required params
        self.parameters = self.__set_category_parameters(self.category)

    def __set_parameter(self, name, the_type='int'):
        parameters = self.allegro_product["productSet"][0]["product"]["parameters"]
        if name == 'SKU':
            return self.sku
        for param in parameters:
            if param.get("name").lower() == name.lower():
                return param["values"][0]
        match the_type:
            # some products might not have EAN
            case 'integer':
                return  10
            case 'float':
                return 100.11
            case 'string':
                return self.sku
            case _:
                return 5901801109167 # random EAN
            

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
                            for img_dict in self.old_images_to_new:
                                if img_dict.get(value):
                                    new_item["value"] = img_dict[value]
                        else:
                            new_item["value"] = value
                    else:
                        new_item[the_key] = value.lower()
                new_items.append(new_item)
            new_description.append({'items': new_items})
        return new_description

    def __get_category_id(self, mapping_template:list[dict], allegro_category_id: str) -> int:
        """Return the category ID and create category property that hold information about the category.
        If failed to find then set product as a draft and create category property as False

        Args:
            mapping_template (list[dict]): the list of mapped categories
            allegro_category_id (str): the allegro category ID

        Returns:
            int: wszystko_pl category id
            create: self.category
        """        
        for category in mapping_template:
            if category['id'] == allegro_category_id:
                self.category = category
                return int(category['wszystko_id'])
        # if the category is not found set product as a draft and return default category which is 0
        self.__set_as_draft()
        self.category = False
        return 0

    def __set_as_draft(self) -> None:
        self.is_draft = True
            
    
    def __set_category_parameters(self, category: list) -> list:
        # if category argument is False then return only default parameters
        parameters = [
            {
            "id": 2,
            "value": str(self.ean)
            },
            {
            "id": 3,
            "value": self.sku
            },
        ]
        if not category:
            return parameters
        # the only category that does not require this parameter
        if self.category_id != 1019:
            parameters.append({"id": 1,"value": 5}) 
        for the_parameter in category["parameters"]:
            # add parameters with ready values
            if the_parameter.get('ready_value', False):
                parameters.append({
                    "id": the_parameter['id'],
                    "value": the_parameter['ready_value']
                })
            # add value to parameters that do not have the value
            elif the_parameter.get('extra', False):
                parameters.append({
                    "id": the_parameter['id'],
                    "value": self.__set_parameter(the_parameter['extra'], the_type=the_parameter['type']) 
                })
        return parameters
#SKU Marka moc pojemnosc



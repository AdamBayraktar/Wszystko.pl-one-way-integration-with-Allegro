import requests
from get_access_token_allegro import get_token
from allegro_get_products_main_info import all_products_id

requests.packages.urllib3.disable_warnings()


def main():
    access_token = get_token()
    example = all_product_detail(access_token, [True, 4])
    print(example)


def get_product_details(access_token, productId):
    """Get detailed information about the product with product ID

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        productId (str): product ID

    Returns:
        dict: product_parameter:value
            schema example:
                {
                "name":"product name",
                "productSet":[
                    {
                        "product":{
                            "id":"str product id",
                            "publication":{
                            "status":"LISTED"
                            },
                            "parameters":[
                            {
                                "id":"225693",
                                "name":"EAN (GTIN)",
                                "values":[
                                    "8691190571030"
                                ],
                                "valuesIds":"None",
                                "rangeValue":"None"
                            },
                            {
                                "id":"224017",
                                "name":"Kod producenta",
                                "values":[
                                    "P-TSD-103"
                                ],
                                "valuesIds":"None",
                                "rangeValue":"None"
                            },
                            {
                                "id":"129369",
                                "name":"Marka",
                                "values":[
                                    "Golden Rose"
                                ],
                                "valuesIds":[
                                    "129369_207"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"129877",
                                "name":"Rodzaj",
                                "values":[
                                    "wypiekany"
                                ],
                                "valuesIds":[
                                    "129877_8"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"129434",
                                "name":"Typ skóry",
                                "values":[
                                    "Do wszystkich typów skóry"
                                ],
                                "valuesIds":[
                                    "129434_8"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"129876",
                                "name":"Właściwości",
                                "values":[
                                    "rozświetlający"
                                ],
                                "valuesIds":[
                                    "129876_2"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"129812",
                                "name":"Poziom krycia",
                                "values":[
                                    "średni"
                                ],
                                "valuesIds":[
                                    "129812_2"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"129767",
                                "name":"Produkt wodoodporny",
                                "values":[
                                    "nie"
                                ],
                                "valuesIds":[
                                    "129767_2"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"452",
                                "name":"SPF",
                                "values":[
                                    "brak"
                                ],
                                "valuesIds":[
                                    "452_7"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"202705",
                                "name":"Waga",
                                "values":[
                                    "9"
                                ],
                                "valuesIds":"None",
                                "rangeValue":"None"
                            },
                            {
                                "id":"129569",
                                "name":"Wielkość",
                                "values":[
                                    "Produkt pełnowymiarowy"
                                ],
                                "valuesIds":[
                                    "129569_1"
                                ],
                                "rangeValue":"None"
                            },
                            {
                                "id":"244589",
                                "name":"Nazwa koloru producenta",
                                "values":[
                                    "103"
                                ],
                                "valuesIds":"None",
                                "rangeValue":"None"
                            },
                            {
                                "id":"237214",
                                "name":"Linia",
                                "values":[
                                    "Terracotta Stardust "
                                ],
                                "valuesIds":"None",
                                "rangeValue":"None"
                            }
                            ]
                        },
                        "quantity":{
                            "value":1
                        }
                    }
                ],
                "parameters":[
                    {
                        "id":"11323",
                        "name":"Stan",
                        "values":[
                            "Nowy"
                        ],
                        "valuesIds":[
                            "11323_1"
                        ],
                        "rangeValue":"None"
                    }
                ],
                "images":[
                    "https://a.allegroimg.com/original/1127ef/",
                    "https://a.allegroimg.com/original/11b018/"
                ],
                "afterSalesServices":{
                    "impliedWarranty":{
                        "id":"warranty id"
                    },
                    "returnPolicy":{
                        "id":"return id"
                    },
                    "warranty":"None"
                },
                "payments":{
                    "invoice":"VAT"
                },
                "sellingMode":{
                    "format":"BUY_NOW",
                    "price":{
                        "amount":"35.89",
                        "currency":"PLN"
                    },
                    "startingPrice":"None",
                    "minimalPrice":"None"
                },
                "stock":{
                    "available":7,
                    "unit":"UNIT"
                },
                "location":{
                    "countryCode":"PL",
                    "province":"WIELKOPOLSKIE",
                    "city":"Utopia",
                    "postCode":"00-000"
                },
                "delivery":{
                    "shippingRates":{
                        "id":"shipping rates ID"
                    },
                    "handlingTime":"PT24H",
                    "additionalInfo":"None",
                    "shipmentDate":"None"
                },
                "description":{
                    "sections":[
                        {
                            "items":[
                            {
                                "type":"IMAGE",
                                "url":"https://a.allegroimg.com/original/url"
                            },
                            {
                                "type":"TEXT",
                                "content":"<h1>html text</h1>"
                            }
                            ]
                        },
                        {
                            "items":[
                            {
                                "type":"TEXT",
                                "content":"<h1>html text</h1>"
                            },
                            {
                                "type":"IMAGE",
                                "url":"https://a.allegroimg.com/url"
                            }
                            ]
                        },
                        }
                    ]
                },
                "external":{
                    "id":"P-TSD-103"
                },
                "category":{
                    "id":"45669"
                },
                "tax":"None",
                "taxSettings":"None",
                "sizeTable":"None",
                "discounts":{
                    "wholesalePriceList":"None"
                },
                "contact":"None",
                "fundraisingCampaign":"None",
                "messageToSellerSettings":"None",
                "attachments":[
                    
                ],
                "b2b":"None",
                "additionalServices":"None",
                "compatibilityList":"None",
                "additionalMarketplaces":{
                    "allegro-cz":{
                        "sellingMode":{
                            "price":{
                            "amount":"194.00",
                            "currency":"CZK"
                            }
                        },
                        "publication":{
                            "state":"APPROVED"
                        }
                    }
                },
                "id":"11842340076",
                "language":"pl-PL",
                "publication":{
                    "status":"ACTIVE",
                    "duration":"None",
                    "endedBy":"None",
                    "endingAt":"None",
                    "startingAt":"None",
                    "republish":false,
                    "marketplaces":{
                        "base":{
                            "id":"allegro-pl"
                        },
                        "additional":[
                            {
                            "id":"allegro-cz"
                            }
                        ]
                    }
                },
                "validation":{
                    "errors":[
                        
                    ],
                    "warnings":[
                        
                    ],
                    "validatedAt":"2023-03-14T00:53:32.560Z"
                },
                "createdAt":"2022-02-17T12:24:17.000Z",
                "updatedAt":"2023-08-24T14:41:00.076Z"
                }
    """    
    url = f"https://api.allegro.pl/sale/product-offers/{productId}"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()


def all_product_detail(access_token: str, get_fixed_number_product: list[bool, int]=[False, 0]) -> tuple[list[dict], list] :  
    """Gets lists of all your products detail and list of all product's ID.
    For testing purpose you can reduce number of requested products to fixed number.
    By default there is no limitation.

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        get_fixed_number_product (list[bool, int], optional): If you want to reduce requested products to fixed number then add list where first item is True and the second item is the fixed number of products. Defaults to [False, 0].

    Returns:
        tuple[list[dict], list]: ([product details], [product IDs])
    """       
    # get all users product id
    all_id = all_products_id(access_token)
    all_id = list(set(all_id))
    all_product_detail_list = []
    # get each product with product id
    if get_fixed_number_product[0]:
        all_id = all_id[:get_fixed_number_product[1]]
    for id in all_id:
        all_product_detail_list.append(get_product_details(access_token, id))
    return all_product_detail_list, all_id

if __name__ == "__main__":
    main()
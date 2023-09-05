import requests 
from get_access_token import get_access_token
from get_complaint_policy_id import get_complaint_policies_ids
from get_guarantee_ids import get_guarantee_policies_ids
from get_return_policy_ids import get_return_policies_ids
from get_shipping_tariff_id import get_shipping_tariff_ids
from NewWszystkoplProduct import NewWszystkoplProduct
from allegro_get_product_details import all_product_detail

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    complaint_police_id = get_complaint_policies_ids(access_token)[0]
    guarantee_police_id = get_guarantee_policies_ids(access_token)[0]
    return_police_id = get_return_policies_ids(access_token)[0]
    shipping_tariff_police_id = get_shipping_tariff_ids(access_token)[0]
    allegro_products = all_product_detail(access_token)
    for product in allegro_products:
        addProduct(access_token, complaint_police_id, guarantee_police_id, return_police_id, shipping_tariff_police_id, product)
    
def addProduct(access_token, complaint_police_id, guarantee_police_id, return_police_id, shipping_tariff_police_id, allegro_product: NewWszystkoplProduct):
    END_POINT = '/me/offers'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    request_body = {
        "title": allegro_product.name,
        "price": allegro_product.price,
        # get the wszystkopl equvilant category
        "categoryId": allegro_product.category_id,
        # get img url from wszystko pl
        "gallery": allegro_product.images,
        "vatRate": "23%",
        # check all required parameters
        # "parameters": [
        #     {
        #     "id": 0,
        #     "value": "string"
        #     }
        # ],
        # check the scheme and img urls
        "description": allegro_product.description,
        "guaranteeId": guarantee_police_id,
        "complaintPolicyId": complaint_police_id,
        "returnPolicyId": return_police_id,
        "shippingTariffId": shipping_tariff_police_id,
        "leadTime": "Natychmiast",
        "stockQuantityUnit": "sztuk",
        "status": "active",
        "userQuantityLimit": 100,
        "isDraft": True, # change to false when the function will be ready
        # "isDraft": allegro_product.is_draft
        "stockQuantity": 0,
        "showUnitPrice": False
        }
    r = requests.post(URL + END_POINT, headers=headers, json=request_body)
    if r.status_code == 200:
        print(f"{r}\n{r.text}")
    else:
        print(f"Something went wrong while adding the product. Check the message:\n{r}\n{r.text}")
    
# def addProduct(access_token, complaint_police_id, guarantee_police_id, return_police_id, shipping_tariff_police_id, allegro_product: NewWszystkoplProduct):
#     END_POINT = '/me/offers'
#     headers = {
#         'Authorization': f'Bearer {access_token}',
#         'Content-Type': 'application/json'
#     }
#     request_body = {
#         "title": "Demo title for tests1",
#         "price": 10,
#         # "categoryId": 0,
#         "gallery": [
#             "https://cdn.wszystko.pl/01891b43-b5df-41cb-b2ac-a383e649c269/{size}-018a1dac-7336-423f-938c-4492a853e683.JPG"
#         ],
#         "vatRate": "23%",
#         # "parameters": [
#         #     {
#         #     "id": 0,
#         #     "value": "string"
#         #     }
#         # ],
#         "description": [
#             {
#             "items": [
#                 {
#                 "type": "text",
#                 "value": "string"
#                 }
#             ]
#             }
#         ],
#         "guaranteeId": guarantee_police_id,
#         "complaintPolicyId": complaint_police_id,
#         "returnPolicyId": return_police_id,
#         "shippingTariffId": shipping_tariff_police_id,
#         "leadTime": "Natychmiast",
#         "stockQuantityUnit": "sztuk",
#         "status": "active",
#         "userQuantityLimit": 100,
#         "isDraft": True,
#         "stockQuantity": 0,
#         "showUnitPrice": False
#         }
#     r = requests.post(URL + END_POINT, headers=headers, json=request_body)
#     if r.status_code == 200:
#         print(f"{r}\n{r.text}")
#     else:
#         print(f"Something went wrong while adding the product. Check the message:\n{r}\n{r.text}")
  
    
if __name__ == "__main__":
    main()
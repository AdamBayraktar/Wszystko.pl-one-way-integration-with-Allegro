import requests 
import traceback
from get_access_token import get_access_token
from get_access_token_allegro import get_token
from get_complaint_policy_id import get_complaint_policies_ids
from get_guarantee_ids import get_guarantee_policies_ids
from get_return_policy_ids import get_return_policies_ids
from get_shipping_tariff_id import get_shipping_tariff_ids
from NewWszystkoplProduct import NewWszystkoplProduct
from allegro_get_product_details import all_product_detail

URL = "https://wszystko.pl/api"
created_products = []
failed_to_create_products = []

# Change file to add just one product like it's name states
def main():
    access_token = get_access_token()
    allegro_access_token = get_token()
    complaint_police_id = get_complaint_policies_ids(access_token)[0]
    guarantee_police_id = get_guarantee_policies_ids(access_token)[0]
    return_police_id = get_return_policies_ids(access_token)[0]
    shipping_tariff_police_id = get_shipping_tariff_ids(access_token)[0]
    # reduce to max [MAX_PRODUCT_NUMBER] products, you are doing it for testing purpose
    MAX_PRODUCT_NUMBER = 4
    allegro_products, all_id = all_product_detail(allegro_access_token, get_fixed_number_product=[True,MAX_PRODUCT_NUMBER])
    total_products_number = len(allegro_products)
    for actual_product_number, product in enumerate(allegro_products):
        actual_product_number += 1
        print(f"Progression: {actual_product_number}/{total_products_number}")
        try:
            new_product = NewWszystkoplProduct(access_token, product)
        except Exception:
            print("Failed to create a product to add")
            print(f"An exception occurred:\n{Exception}")
            traceback.print_exc()
            print(product)
        else:
            addProduct(access_token, complaint_police_id, guarantee_police_id, return_police_id, shipping_tariff_police_id, new_product)
    write_it_as_variable(created_products, 'variables/active_products.py', 'active_products')
    write_it_as_variable(failed_to_create_products, 'variables/failed_to_add_products.py', 'failed_to_add_products')
    
def addProduct(access_token, complaint_police_id, guarantee_police_id, return_police_id, shipping_tariff_police_id, allegro_product: NewWszystkoplProduct):
    END_POINT = '/me/offers'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    request_body = {
        "title": allegro_product.name,
        "price": allegro_product.price,
        "categoryId": allegro_product.category_id,
        "gallery": allegro_product.images,
        "vatRate": "23%",
        'parameters': allegro_product.parameters,
        "description": allegro_product.description,
        "guaranteeId": guarantee_police_id,
        "complaintPolicyId": complaint_police_id,
        "returnPolicyId": return_police_id,
        "shippingTariffId": shipping_tariff_police_id,
        "leadTime": "Natychmiast",
        "stockQuantityUnit": "sztuk",
        "status": allegro_product.status,
        "userQuantityLimit": 100,
        "isDraft": allegro_product.is_draft,
        "stockQuantity": allegro_product.stock,
        "showUnitPrice": False
        }
    send_parameters = (f"""The request body parameters
          ==========================================================================
          {request_body['parameters']}
          ==========================================================================""")
    r = requests.post(URL + END_POINT, headers=headers, json=request_body)
    if r.status_code == 200:
        # print(f"{r}\\{r.text}")
        print("Successfully added")
        created_products.append({'wszystko_product_id': r.json()['id'], 'allegro_id': allegro_product.id})
    else:
        print(send_parameters)
        print(f"Something went wrong while adding the product. Check the message:\n{r}\n{r.text}")
        failed_to_create_products.append(f"{len(failed_to_create_products)}. product failed to add, the message:\n{r}\n{r.text}\n\n\n")

 
def write_it_as_variable(file, file_name, variable_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f'{variable_name} = {file}')

    
if __name__ == "__main__":
    main()
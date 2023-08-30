import requests
from get_access_token_allegro import get_token
from allegro_get_products_main_info import all_products_id

requests.packages.urllib3.disable_warnings()

# main function that first request all products of user then uses IDs of products to get detailed information about product
def main():
    access_token = get_token()
    example = all_product_detail(access_token)
    print(example)


def get_product_details(access_token, productId):
    """_summary_

    Args:
        access_token (_type_): _description_
        productId (_type_): _description_

    Returns:
        _type_: _description_
    """    
    url = f"https://api.allegro.pl/sale/product-offers/{productId}"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()

def all_product_detail(access_token):
    """_summary_

    Args:
        access_token (_type_): _description_

    Returns:
        _type_: _description_
    """    
    # get all users product id
    all_id = all_products_id(access_token)
    all_id = list(set(all_id))
    all_product_detail_list = []
    # get each product with product id
    for id in all_id[:100]:
        all_product_detail_list.append(get_product_details(access_token, id))
    return all_product_detail_list, all_id

if __name__ == "__main__":
    main()
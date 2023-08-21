import requests
from get_access_token_allegro import get_token

requests.packages.urllib3.disable_warnings()

# get all user's products
def main():
    access_token = get_token()
    example = all_own_category_id(access_token)
    print(example)
    


def get_products_main_info(access_token, lower_price=0, upper_price=1000, limit=1000):
    """Get main information about your products. Maximum number of returned products is 1000. If you have more than 1000 products, you can send multiple requests, each with a different set of 'lower_price' and 'upper_price' arguments, in order to retrieve all of the products.

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        lower_price (int, optional): The minimum price of requested products. Defaults to 0.
        upper_price (int, optional): The maximum price of requested products. Defaults to 1000.
        limit (int, optional): The maximum number of returned products. Defaults to 1000.

    Returns:
        list: list of dictionaries that represents each product
    """    
    url = "https://api.allegro.pl/sale/offers"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        "limit": limit,
        'sellingMode.price.amount.gte': lower_price,
        'sellingMode.price.amount.lte': upper_price,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()["offers"]


# gets all user's products and return list of products id
def all_own_category_id(access_token):
    """Request main info for each product on Allegro. Takes the category ID from each product and returns list of unique category IDs.

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module

    Returns:
        list: list of unique category IDs that the seller has at least one product on it
    """    
    all_products = []
    # max limit products per request is 1000 therefore divide by price to several requests to get all products
    all_products.extend(get_products_main_info(access_token, upper_price=10))
    all_products.extend(get_products_main_info(access_token, lower_price=10.01, upper_price=18))
    all_products.extend(get_products_main_info(access_token, lower_price=18.01))
    all_category_ids = [int(product["category"]['id']) for product in all_products]
    return list(set(all_category_ids))
    

if __name__ == "__main__":
    main()
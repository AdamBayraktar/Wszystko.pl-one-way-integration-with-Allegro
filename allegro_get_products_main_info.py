import requests
from get_access_token_allegro import get_token

requests.packages.urllib3.disable_warnings()

# get all user's products
def main():
    access_token = get_token()
    example = all_products_id(access_token)
    print(example)
    

def get_products_main_info(access_token:str, lower_price:int=0, upper_price:int=1000, limit:int=1000) -> list[dict]:
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
def all_products_id(access_token:str, price_range:list[int]=[9, 14, 17, 20]) -> list:
    """Get all your shop's products ID. Per one request you can get up to 1000 products. If you have more than 1000, then use price_range argument to split the request in such manner to get all products.

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        price_range (list[int], optional): List of prices that for each range unique request is send. Defaults to [9, 14, 17, 20].

    Returns:
        list: list of product's ID
    """   
    all_products = []
    # max limit products per request is 1000 therefore to get all products send requests for different range of prices
    # for price in price_range
    for index,price in enumerate(price_range):
        if index == 0:
            all_products.extend(get_products_main_info(access_token, upper_price=price))
        elif index == (len(price_range) - 1):
            all_products.extend(get_products_main_info(access_token, lower_price=price))
        else:
            all_products.extend(get_products_main_info(access_token, lower_price=price_range[index - 1], upper_price=price))
    return [product["id"] for product in all_products]
    

if __name__ == "__main__":
    main()
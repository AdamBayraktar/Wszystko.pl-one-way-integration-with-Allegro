import requests
from get_access_token_allegro import get_token
from allegro_get_products_main_info import get_products_main_info

requests.packages.urllib3.disable_warnings()

# get all user's products
def main():
    access_token = get_token()
    example = all_own_category_id(access_token)
    print(example)
    

# gets all user's products and return list of products id
def all_own_category_id(access_token: str) -> list[str]:
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
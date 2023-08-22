import requests
from get_access_token_allegro import get_token
from allegro_get_own_products_category_id import all_own_category_id

requests.packages.urllib3.disable_warnings()


# get all user's products
def main():
    access_token = get_token()
    category_ids = all_own_category_id(access_token)
    for id in category_ids:
        print(get_category_by_id(access_token, id))
        break
    

def get_category_by_id(access_token:str, categoryId:str|int) -> dict:
    """Get category information

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        categoryId (str): The unique category ID.
        
    Returns:
        dict: category information
    """    
    
    URL = f"https://api.allegro.pl/sale/categories/{categoryId}"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(URL, headers=headers)
    return response.json()


if __name__ == "__main__":
    main()
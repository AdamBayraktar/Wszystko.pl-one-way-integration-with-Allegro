import requests
from get_access_token_allegro import get_token

requests.packages.urllib3.disable_warnings()


# get all user's products
def main():
    access_token = get_token()
    example = get_subcategories(access_token, '1429')
    print(example)
    

def get_subcategories(access_token:str, parent_id:str | int) -> dict:
    """Get subcategories of given ID category

    Args:
        access_token (str): allegro access token
        parent_id (str): The parent category id.
        
    Returns:
        dict: subcategories of the parent ID
    """    
    
    URL = "https://api.allegro.pl/sale/categories"
    headers = {
        'Accept': 'application/vnd.allegro.public.v1+json',
        'Authorization': f'Bearer {access_token}'
    }
    params = {
        "parent.id": parent_id,
    }
    response = requests.get(URL, headers=headers, params=params)
    return response.json()


if __name__ == "__main__":
    main()
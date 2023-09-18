import requests 
from get_access_token import get_access_token

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    get_category_params(access_token, 13889)


def get_category_params(access_token:str, category_id:int) -> list[dict]:
    """Get all category parameters

    Args:
        access_token (str): access token required for authorization
        category_id (int): the id of category

    Returns:
        list[dict]: [{parameter}]
    """    
    END_POINT = f"/categories/{category_id}/parameters"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(URL + END_POINT, headers=headers)
    if response.status_code == 200:
        return response.json()['fields']
    else:
        print('something went wrong')
        print(response)
        print(response.text)
    

if __name__ == "__main__":
    main()
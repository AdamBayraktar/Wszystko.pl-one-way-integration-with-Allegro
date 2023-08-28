import requests 
from get_access_token import get_access_token
from custom_exceptions import getCategoryError

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    get_category(access_token, 13842)


def get_category(access_token:str, categoryId: str | int) -> dict:
    """Get category information with category ID

    Args:
        access_token (str): access token required for authorization
        categoryId (str | int): the unique ID of requested category

    Returns:
        dict: dictionary with parameter name as key and value as parameter value
            example:
                {
                "adultOnly": false,
                "unitPrice": {
                "enabled": false
                },
                "title": "Cyfry i litery na drzwi",
                "id": 21,
                "name": "Cyfry i litery na drzwi",
                "parentId": 20,
                "hasSubcategories": false
                }
    """
    END_POINT = f"/categories/{categoryId}"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(URL + END_POINT, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        error_msg = f'Something went wrong while obtaining the category. Please check the message:\n{response}\n {response.text}'
        raise getCategoryError(error_msg)
    

if __name__ == "__main__":
    main()
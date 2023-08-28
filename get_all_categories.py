import requests 
from get_access_token import get_access_token
from get_category import get_category

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    print(get_all_categories(access_token))


def get_all_categories(access_token: str, page=1, pageSize=10000, includeParameters=False) -> list[dict]:
    """Get all categories. If there is more categories than page size then you should request as many times as page number with appropriate page number argument.

    Args:
        access_token (str): access token required for authorization
        page (int, optional): the number of page, if there is more categories than pagesize then there will be more pages than 1. Defaults to 1.
        pageSize (int, optional): The number of categories per page. Defaults to 10000.
        includeParameters (bool, optional): include parameters. Defaults to False.

    Returns:
        list[dict]: each dict represents category with main information about them
            example of element:
                {'fields': [], 'adultOnly': False, 'unitPrice': {'enabled': False}, 'title': '', 'id': 15897, 'name': 'iPhone 15 Pro', 'parentId': 4173, 'hasSubcategories': False}
    """    
    END_POINT = "/categories"
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'includeParameters': includeParameters,
               'pageSize': pageSize,
               'page': page}
    response = requests.get(URL + END_POINT, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()['categories']
    else:
        print('something went wrong')
        print(response)
        print(response.text)

if __name__ == "__main__":
    main()
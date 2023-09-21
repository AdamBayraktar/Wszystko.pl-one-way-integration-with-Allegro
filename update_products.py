import requests 
from get_access_token import get_access_token

URL = "https://wszystko.pl/api"
def main():
    access_token = get_access_token()
    update_product(access_token, 1006805318, 20, 1 )


def update_product(access_token:str, product_Id: int, new_price:float, new_quantity:int):
    """Update product parameters such as price and stock

    Args:
        access_token (str): access token required for authorization
        product_Id (str | int): the unique ID of requested category
        new_price (float): the new price of the product
        new_quantity (int): the new quantity of the product
    """
    END_POINT = f"/me/update-offers"
    headers = {'Authorization': f'Bearer {access_token}',
               'Content-Type': 'application/json'
    }
    request_body = {
        'id': [product_Id],
        "price": {
            'value': new_price,
            "change": 'exactValue'
        },
        "quantity": {
            'value': new_quantity,
            "change": 'exactValue'
        },
    }
    response = requests.post(URL + END_POINT, headers=headers, json=request_body)
    if response.status_code == 200:
        print("Successfully updated")
    else:
        print(f"{response}\n{response.text}")

    
if __name__ == "__main__":
    main()
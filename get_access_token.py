import requests 
import time
from custom_exceptions import deviceCodeError, accessTokenError

URL = "https://wszystko.pl/api"

def main():
    device_code = get_device_code()
    time.sleep(20) 
    accessToken = request_access_token(device_code)
    print(accessToken)

def get_device_code() -> str:
    """Request for device code

    Raises:
        deviceCodeError: Failed to get device code

    Returns:
        str: device code
    """    
    END_POINT = "/integration/register"
    response = requests.get(URL + END_POINT)
    if response.status_code == 200:
        print(f"Follow the link to activate the device code, you have 20 seconds: {response.json()['verificationUriPrettyComplete']}")
        return response.json()['deviceCode']
    else:
        print(response)
        raise deviceCodeError(f'Something went wrong with device code, check the message: {response}\n {response.text}')
    

def request_access_token(device_code:str) -> str:
    """Get access token, which is required mostly for all requests in WSZYSTKO.PL API.

    Args:
        device_code (str): unique device code

    Raises:
        accessTokenError: failed to get access token

    Returns:
        str: access token
    """    
    END_POINT = "/integration/token"
    params = {"deviceCode": device_code}
    response = requests.get(URL + END_POINT, params = params)
    if response.status_code == 200:
        return response.json()['accessToken']
    else:
        raise accessTokenError(f'Something went wrong while obtaining the Access Token. Please check the message: {response}\n {response.text}')

# flow to get access token
def get_access_token() -> str:
    """First request for the device code, then get the access token with the device code.

    Returns:
        str: access token
    """    
    device_code = get_device_code()
    time.sleep(20) 
    accessToken = request_access_token(device_code)
    print({f'Access Token: {accessToken}'})
    return accessToken
    
if __name__ == "__main__":
    main()
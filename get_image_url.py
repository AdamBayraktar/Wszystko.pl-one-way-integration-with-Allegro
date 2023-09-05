import requests 
from get_access_token import get_access_token
from custom_exceptions import getImgUrlError

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    new_url = add_image(access_token, ['https://alemozgoldenrose.pl/632-tm_thickbox_default/002-woman.jpg', 'https://alemozgoldenrose.pl/1315-tm_thickbox_default/perfect-nail-color-nude-look-lakier-do-paznokci-golden-rose.jpg'])
    print(new_url)
    

def add_image(access_token:str, img_urls:list[str]) -> dict:
    """Add list of images to the service and get approved image url

    Args:
        access_token (str): access token required for authorization
        img_url (str): list of image urls

    Returns:
        dict: where the key is old url and the value is a new url
    """
    END_POINT = "/me/addFilesFromUrls"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        }
    data = img_urls
    r = requests.post(URL + END_POINT, headers=headers, json=data)
    if r.status_code == 200:
        new_img_urls = {}
        for img in r.json():
            new_img_urls[img['name']] = (img['url'])
        print(r)
        print(r.text)
        return new_img_urls
    else:
        error_msg = f'Something went wrong while obtaining the new URL of the images that were sent. Please check the message:\n{r}\n {r.text}'
        raise getImgUrlError(error_msg)
        
        
        
if __name__ == "__main__":
    main()
        
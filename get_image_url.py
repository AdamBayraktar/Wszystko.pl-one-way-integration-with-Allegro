import requests 
from get_access_token import get_access_token
from custom_exceptions import getImgUrlError

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    new_url = add_image(access_token, ['https://alemozgoldenrose.pl/632-tm_thickbox_default/002-woman.jpg', 'https://a.allegroimg.com/original/116e0f/9efd4f6e48f6a2003d9f4e633587'])
    print(new_url)
    

def add_image(access_token:str, img_urls:list[str]) -> list[dict[str, str]]:
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
        new_img_urls = []
        for old_img in data:
            for img in r.json():
                # new_img_urls[img['name']] = img['url']
                if img['name'] == old_img:
                    new_img_urls.append({img['name']:img['url']})
        print(r)
        print(r.text)
        return new_img_urls
    else:
        error_msg = f'Something went wrong while obtaining the new URL of the images that were sent. Please check the message:\n{r}\n {r.text}'
        raise getImgUrlError(error_msg)
        
        
        
if __name__ == "__main__":
    main()
        
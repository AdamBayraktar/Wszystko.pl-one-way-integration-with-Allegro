import requests 
from get_access_token import get_access_token
from custom_exceptions import guaranteePoliciesIdError

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    id_list = get_guarantee_policies_ids(access_token)
    print(id_list)
    

def get_guarantee_policies_ids(access_token):
    """Get list of IDs of guarantee policies

    Args:
        access_token (str): access token required for authorization

    Returns:
        list: list of IDs
    """
    END_POINT = "/me/guarantees"
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(URL + END_POINT, headers=headers)
    if response.status_code == 200:
        ids_list = []
        all_policies = response.json()
        for policy in all_policies:
            ids_list.append(policy['id'])
        return ids_list
    else:
        error_msg = f'Something went wrong while obtaining the IDs of guarantee policies. Please check the message:\n{response}\n {response.text}'
        raise guaranteePoliciesIdError(error_msg)
        
        
        
if __name__ == "__main__":
    main()
        
import requests 
from get_access_token import get_access_token
from custom_exceptions import complaintPoliciesIdError

URL = "https://wszystko.pl/api"

def main():
    access_token = get_access_token()
    id_list = get_complaint_policies_ids(access_token)
    print(id_list)
    

def get_complaint_policies_ids(access_token):
    """Get list of IDs of complaint policies

    Args:
        access_token (str): access token required for authorization

    Returns:
        list: list of IDs
    """
    END_POINT = "/me/complaintPolicies"
    headers = {'Authorization': f'Bearer {access_token}'}
    r = requests.get(URL + END_POINT, headers=headers)
    if r.status_code == 200:
        ids_list = []
        all_policies = r.json()
        for policy in all_policies:
            ids_list.append(policy['id'])
        return ids_list
    else:
        error_msg = f'Something went wrong while obtaining the IDs of complaint policies. Please check the message:\n{r}\n {r.text}'
        raise complaintPoliciesIdError(error_msg)
        
        
        
if __name__ == "__main__":
    main()
        
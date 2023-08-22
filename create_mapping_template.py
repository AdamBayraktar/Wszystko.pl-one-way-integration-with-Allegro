import requests
from get_access_token_allegro import get_token
from allegro_get_own_products_category_id import all_own_category_id
from allegro_get_category_by_id import get_category_by_id

requests.packages.urllib3.disable_warnings()

def main():
    access_token = get_token()
    id_list = all_own_category_id(access_token)
    mapping_template = create_mapping_template(access_token, id_list)
    write_to_python_file_as_variable(mapping_template, 'mapping_template.py')
        
def create_mapping_template(access_token:str, allegro_id_list: list) -> list[dict]:
    """Create mapping template from Allegro category ID list

    Args:
        access_token (str): unique token issued by Allegro. Use get_access_token_allegro module
        allegro_id_list (list): list of your products category IDs

    Returns:
        list[dict]: [{id, name, parent, wszystko_id, wszystko_name}...]
    """    
    mapping_template = []
    for cat_id in allegro_id_list:
        category = get_category_by_id(access_token, cat_id)
        # get parent category information. You will have a better view when you map categories   
        parent_category = get_category_by_id(access_token, category['parent']['id'])
        mapping_category = {
            'id': category['id'],
            'name': category['name'],
            'parent': parent_category['name'],
            'wszystko_id': 'int | str',
            'wszystko_name': 'str'
        }
        mapping_template.append(mapping_category)
    return mapping_template
        
def write_to_python_file_as_variable(mapping_template: list, file_name:str='mapping_template.py'):
    """Write data to file with py extension as a variable.

    Args:
        mapping_template (list): The category mapping template.
        file_name (str, optional): The name of the created file. Defaults to 'mapping_template.py'.
    """    
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write("\"Complete each row with the missing data. Each row\'s \'wszystko_id\' key must have wszystko.pl category ID that matches to the corresponding allegro category ID.\"\n\n\n")
        file.write("mapping_template_name = [\n")
        for category in mapping_template:
            file.write(f'    {category},\n')
        file.write("]")
        

if __name__ == "__main__":
    main()
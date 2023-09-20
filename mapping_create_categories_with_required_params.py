from get_access_token import get_access_token
from get_category_with_params import get_category_params
from variables.mapping_auto_template_finished import mapped_categories as all_categories

# it is based on my products
def main():
    wszystko_access_token = get_access_token()
    mapped_categories = get_required_params(wszystko_access_token, all_categories)
    write_it_as_variable(mapped_categories, 'variables/mapping_template_category_with_required_params.py', 'mapped_categories')

def get_required_params(wszystko_access_token:str, mapped_categories: list[dict]) -> list[dict]:
    """Add required parameters to given categories
    
    Args:
        wszystko_access_token (str): access token required for authorization
        mapped_categories (list[dict]): list of dictionaries of categories, required keys: wszystko_id

    Returns:
        list[dict]: list of dictionaries of categories with required parameters
    """    
    mapped_categories_with_params = []
    for category in mapped_categories:
        category_params = get_category_params(wszystko_access_token, category['wszystko_id'])
        parameters = []
        for parameter in category_params:
            if parameter['required'] and parameter['id'] not in [1, 2, 3 ]:
                parameters.append(parameter)
        mapped_categories_with_params.append(parameters)
        category['parameters'] = parameters
    return mapped_categories

def write_it_as_variable(file, file_name, variable_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f'{variable_name} = {file}')


if __name__ == "__main__":
    main()
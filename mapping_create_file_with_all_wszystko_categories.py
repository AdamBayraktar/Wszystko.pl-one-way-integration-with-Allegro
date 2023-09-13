from get_access_token import get_access_token
from get_all_categories_without_subcategories import get_all_categories_without_subcategories


def main():
    access_token = get_access_token()
    categories = get_all_categories_without_subcategories(access_token)
    write_it_as_variable(categories, "variables/mapping_all_wszystko_categories.py", "all_wszystko_categories")
    
    
def write_it_as_variable(file, file_name, variable_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f'{variable_name} = {file}')
        

if __name__ == "__main__":
    main()
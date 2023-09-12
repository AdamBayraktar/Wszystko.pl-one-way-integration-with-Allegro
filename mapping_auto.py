from get_access_token_allegro import get_token
from get_access_token import get_access_token
from create_mapping_template import create_mapping_template
from allegro_get_own_products_category_id import all_own_category_id
from get_all_categories_without_subcategories import get_all_categories_without_subcategories
# delete it after
from test_categories import wszystko_pl_categories_test

def main():
    wszystko_access_token = get_access_token()
    allegro_access_token = get_token()
    # get all user allegro categories [category name, parent name]
    all_allegro_id = all_own_category_id(allegro_access_token)
    allegro_categories = create_mapping_template(allegro_access_token, all_allegro_id)

    # get all wszystko pl categories [category name, parent name]
    # wszystko_pl_categories = get_all_categories_without_subcategories(wszystko_access_token)

    # for the time use hard written variable
    wszystko_pl_categories = wszystko_pl_categories_test

    # connect allegro categories with wszystkopl categories by category name and it's parrent name
    mapped_categories = map_categories(allegro_categories, wszystko_pl_categories)
    write_it(mapped_categories, 'test_auto_mapping.py')


def map_categories(allegro_categories: list[dict], wszystko_pl_categories: list[dict]):
    mapped_categories = []
    for allegro_category in allegro_categories:
        for wszystko_pl_category in wszystko_pl_categories:
            if allegro_category['name'] == wszystko_pl_category['name'] and allegro_category['parent'] == wszystko_pl_category.get('parent', False):
                new_mapping = allegro_category
                new_mapping['wszystko_id'] = wszystko_pl_category['id']
                new_mapping['wszystko_name'] = wszystko_pl_category['name']
                mapped_categories.append(new_mapping)
                break
    return mapped_categories
    

def write_it(file, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f'categories = {file}')
        

if __name__ == "__main__":
    main()
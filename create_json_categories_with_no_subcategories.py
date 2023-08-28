import json
from get_access_token import get_access_token
from get_category import get_category
from get_all_categories import get_all_categories

URL = "https://wszystko.pl/api"

# get all categories that have no subcategories
def main():
    access_token = get_access_token()
    # list of all categories without subcategories
    modified_categories = []
    all_categories = []
    # {catId: name} dictionary of parent categories to categories without subcategories
    all_parents = {}
    # request all categories, there are at least 2 pages
    for page_num in range(1, 4):
        category_page = get_all_categories(access_token, page_num)
        if category_page:
            all_categories.extend(category_page)
    for cat in all_categories:
        if cat['hasSubcategories'] == False:
            the_category = {
                "name": cat['name'],
                'id': cat['id']   
            }
            # if new: add parent {id: name} to all_parent dictionary
            # add parent name to the_category
            if 'parentId' in cat:
                if not cat['parentId'] in all_parents:
                    # get parent info
                    parent_category = get_category(access_token, cat['parentId'])
                    all_parents[cat['parentId']] = parent_category['name']
                the_category['parent'] = all_parents[cat['parentId']]
            modified_categories.append(the_category)
    # create file with categories without subcategories
    save_file(modified_categories, "wszystko_pl_all_categories.json")
   
    
def save_file(data, file_name):
    with open(file_name, "w", encoding='utf-8') as file:
        for cat in data:
            json.dump(cat, file, ensure_ascii=False)
            file.write('\n')

if __name__ == "__main__":
    main()
from get_access_token import get_access_token
from get_category import get_category
from get_all_categories import get_all_categories

def main():
    access_token = get_access_token()
    print(get_all_categories_without_subcategories(access_token))


def get_all_categories_without_subcategories(access_token:str) -> list[dict]:
    """Get all wszystko.pl categories that don't have subcategories.
    Return list of dictionaries with name, id, parent name of the category

    Args:
        access_token (str): access token required for authorization

    Returns:
        all_categories_without_subcategories: [{name, id, parent}]
    """    
    # list of all categories without subcategories
    all_categories_without_subcategories = []
    all_categories = []
    # {catId: name} dictionary of parent categories to categories without subcategories
    all_parents = {}
    # request all categories, there are at least 2 pages
    for page_num in range(1, 4):
        category_page = get_all_categories(access_token, page_num)
        if category_page:
            all_categories.extend(category_page)
    print("It may take up to 5 minutes")
    for cat in all_categories:
        if cat['hasSubcategories'] == False:
            the_category = {
                "name": cat['name'],
                'id': cat['id']   
            }
            # if new: add parent {id: name} to all_parent dictionary
            # add parent name to the_category
            if not cat['parentId'] in all_parents:
                # get parent info
                parent_category = get_category(access_token, cat['parentId'])
                all_parents[cat['parentId']] = parent_category['name']
            the_category['parent'] = all_parents[cat['parentId']]
            all_categories_without_subcategories.append(the_category)
    return all_categories_without_subcategories
            


if __name__ == "__main__":
    main()
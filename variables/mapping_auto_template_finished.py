from mapping_auto_template_to_do import mapped_categories as mapped_categories_to_do
# run file and check the output
# if there is not mapped category then follow the instruction below
# copy-paste variable from mapping_auto_template_to_do here and name it as mapped_categories
# then using 'mapping_all_wszystko_categories.py' map the remaining categories, those with 'To DO' value (probably there won't be any)
# finally run this file to be sure that each category is mapped
mapped_categories = mapped_categories_to_do


def main():
    mapped_correctly = True
    for category in mapped_categories:
        if 'TO DO!!!!!!!!!!!' in  [category['wszystko_id'], category['wszystko_name']]:
            print(f'Allegro category \"{category["name"]}\" - hasn\'t been mapped, please do it.')
            mapped_correctly = False
    if mapped_correctly:
        print('Everything is mapped correctly. You may proceed to the next step')
        print(f"Total number of categories {len(mapped_categories)}")


if __name__ == "__main__":
    main()
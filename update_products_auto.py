from get_access_token import get_access_token
from get_access_token_allegro import get_token
from update_products import update_product
from variables.active_products import active_products
from allegro_get_products_main_info import all_products_by_price_range

def main():
    wszystko_access_token = get_access_token()
    allegro_access_token = get_token()
    all_allegro_products = all_products_by_price_range(allegro_access_token)
    total_number_products_to_update = len(active_products)
    updated_products_number = 0 
    for product in active_products:
        product_is_not_in_allegro = True
        updated_products_number += 1
        print(f'Updating {updated_products_number}/{total_number_products_to_update}')
        for allegro_product in all_allegro_products[:]:
            if product['allegro_id'] == allegro_product['id']:
                new_price = allegro_product['sellingMode']['price']['amount']
                new_stock = allegro_product['stock']['available']
                if is_status_inactive(allegro_product): new_stock = 0
                update_product(wszystko_access_token, product['wszystko_product_id'], new_price, new_stock)
                # product was found in Allegro
                product_is_not_in_allegro = False
                all_allegro_products.remove(allegro_product)
                break
        # if product is not available in Allegro it means that it was deleted. Thus it should not be available in this platform 
        if product_is_not_in_allegro:
            print("Product is no longer available in Allegro. The stock of the products is set to 0")
            update_product(wszystko_access_token, product['wszystko_product_id'], 666, 0)
        print()
            
def is_status_inactive(allegro_product: dict) -> bool:
    return False if allegro_product['publication']['status'].lower() == 'active' else True

    

if __name__ == "__main__":
    main()
    
    
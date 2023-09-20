from get_access_token import get_access_token
from get_category_with_params import get_category_params
from variables.mapping_auto_template_finished import mapped_categories as all_categories

# it is based on my products
def main():
    access_token = get_access_token()
    # print(mapped_categories_with_params)
    mapped_categories = add_required_params_with_defined_values(access_token, all_categories)
    write_it_as_variable(mapped_categories, 'variables/mapping_auto_template_finished_with_params.py', 'mapped_categories')

def add_required_params_with_defined_values(access_token:str, mapped_categories: list[dict]):
    mapped_categories_with_params = []
    for category in mapped_categories:
        category_params = get_category_params(access_token, category['wszystko_id'])
        parameters = []
        for parameter in category_params:
            if parameter['required'] and parameter['id'] not in [1, 2, 3 ]:
                parameters.append({
                    "id": parameter['id'],
                    "label": parameter['label'],
                    "type": parameter['type'],
                })
                values = parameter.get('values', False)
                match parameter['id']:
                    case 151: # Przeznaczenie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([12669], values) # "kąpiel i prysznic"
                    case 1262: # Wielkość
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([99208], values) # Produkt pełnowymiarowy
                    case 3131: # Pojemność
                        parameters[-1]['ready_value'] = 99208104016 # brak info
                    case 8494: # Pojemność opakowania
                        parameters[-1]['extra'] = 'pojemnosc' # to do !!!!!!!!!!!!!!!!!!!!!
                    case 49: # Typ
                        parameters[-1]['ready_value'] = 992088538 # inny !!!!!!!!!! also differs 8307
                    case 495: # model
                        parameters[-1]['ready_value'] = 'Fish' # cykady wobler
                    case 11410: # Rodzaje rzęs
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([150170], values) # inny
                    case 824: # Barwa światła
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([98050], values) # inny
                    case 2303: # Kolor szkła
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([284218], values) # Inny
                    case 1183: # bohater ????
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([98839], values) # Inny
                    case 6: # Kolor 
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([284218], values) # Inny
                    case 1188: # płeć
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([99001], values) # brak info
                    case 11422: # liczba
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([150252], values) # brak info
                    case 7418: # Rodzaj włosia
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([126945], values) # brak info
                    case 801: # opakowanie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([97968], values) # Inne
                    case 2116: # Właściwości
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([101332], values) # Inne
                    case 13: # liczba sztuk
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([1], values) 
                    case 11424: # Typ skóry
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([150258], values) # Do wszystkich typów
                    case 2920: # zapach
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([103159], values) # Inne
                    case 312: # Wykończenie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([96913], values) # Inne
                    case 1328: # Zasilanie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([99385], values) # brak
                    case 2115: # forma
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([101243], values) # inny !!!!!!! the same
                    case 15: # pojemność
                        parameters[-1]['extra'] = 'pojemnosc' # Inne
                    case 11417: # Szczoteczka
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([150222], values) # Inne
                    case 3246: # Konsystencja
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([104151], values) # Inna
                    case 972: # Efekt
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([98164], values) # Inne
                    case 3058: # Działanie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([103522], values) # Inne
                    case 11655: # Typ włosów
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([150445], values) # Inne
                    case 43: # Materiał
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([7911], values) # Inne
                    case 2235: # Rodzaj rośliny
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([101817], values) # Inne
                    case 8: # marka
                        parameters[-1]['extra'] = "Marka"
                    case 261: # moc
                        parameters[-1]['extra'] = "moc"
                    case 793: # napiecie
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([97934], values)
                    case 9: # rodzaj
                        parameters[-1]['ready_value'] = check_for_id_or_return_any_id([1816, 1820], values) # inny  !!!!!!!! it is important - one product do not have that option - it is dict id value
                        # maybe check for "inny" label and if it is not found pick the first option
                        # use function for it
                        # function check the default ID and if it is equal to "inny" return as it is otherwise checks for it
                        # if it doesn't find any matching then pick random item
                    case _:
                        parameters[-1]["values"]: values
                        
            elif parameter['id'] in [277, 1184, 5]:
                if parameter['id'] == 277:
                    brand = {
                        "extra": 'Marka',
                        'id': parameter['id'],
                        'ready_value': parameter['values'][0]['id'],
                        "type": parameter['type']
                    }
                    for val in parameter['values']:
                        if val['label'] == 'Golden Rose':
                                brand['ready_value'] = val['id']
                    parameters.append(brand)    
                elif parameter['id'] == 1184:
                    parameters.append({
                        "extra": 'SKU',
                        'id': parameter['id'],
                        "type": parameter['type']
                        })
                elif parameter['id'] == 5:
                    parameters.append({
                        "extra": 'SKU',
                        'id': parameter['id'],
                        "type": parameter['type']
                    })
        mapped_categories_with_params.append(parameters)
        category['parameters'] = parameters
    return mapped_categories

def write_it_as_variable(file, file_name, variable_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(f'{variable_name} = {file}')

def check_for_id_or_return_any_id(id_list: list, values: list) -> int:
    # if there is no values list then return id as it is
    if not values:
        return id_list[0]
    
    for value in values:
        if value['id'] in id_list:
            return value['id']
    # if there is no matching element return first id
    return values[0]['id']


if __name__ == "__main__":
    main()
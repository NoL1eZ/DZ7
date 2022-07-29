cook_book = {}
with open('recepie.txt', 'r', encoding='utf-8') as recepie: #тут мы ссылаемся на текстовый документ
    for txt in recepie.read().split('\n\n'): #тут разбиваются блюда по двум отступам"('\n\n')"
        dish_name, amount_of_ingredients, *ingredients = txt.split('\n')
        tmp = [] #
        for ingredient in ingredients:
            ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, ingredient.split(' | '))
            # map это функция применения функции (в данном случае lambda) к каждому объекту
# Метод isdigit() возвращает True, если все символы в строке являются цифрами. Если нет, возвращается False.
            tmp.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = tmp
    # return cook_book
def get_shop_list_by_dishes(dishes, person_count):
    list_by_dishes = dict()
    for item in dishes:
        for dish, ingredients in cook_book.items():
            if item in dish:
                for ingredient in ingredients:
                    ingredient_name, quantity, measure = ingredient['ingredient_name'], int(ingredient['quantity']), ingredient['measure']
                    list_by_dishes.setdefault(ingredient_name, {'measure':measure, 'quantity':quantity*person_count})
    return list_by_dishes
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

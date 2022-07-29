# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
#
# class List_by_dishes:
#     def __init__(self, ingredient_name):
#         self.ingredient_name = ingredient_name
#         self.grocery_trolley = {}
#
#     def shopping_list (self, ingredient_name, quantity, measure):
#         if measure in ingredient_name.grocery_trolley:
#             ingredient_name.grocery_trolley[measure] += [quantity]
#         else:
#             ingredient_name.grocery_trolley[measure] = [quantity]
# def get_shop_list_by_dishes(dishes, person_count):
#     list_by_dishes = dict()
#     for item in dishes:
#         for dish, ingredients in cook_book.items():
#             if item in dish:
#                 for ingredient in ingredients:
#                     ingredient_name, quantity, measure = ingredient['ingredient_name'], int(ingredient['quantity']), ingredient['measure']
#                     list_by_dishes.setdefault(ingredient_name, {'measure':measure, 'quantity':quantity*person_count})
#     return list_by_dishes
# print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

with open('1.txt', 'r', encoding='utf-8') as f:
    f_lines = [l for l in f.readlines()]

with open('2.txt', 'r', encoding='utf-8') as f1:
    f1_lines = [l for l in f1.readlines()]

with open('3.txt', 'r', encoding='utf-8') as f2:
    f2_lines = [l for l in f2.readlines()]

class File:
    def __init__(self, name, text):
        self.name = name
        self.text = [line.rstrip() for line in text]
        self.length = len(text)



print
def print_file(file):
    # for item in file:
    print(file.name)
    print(file.length)
    for i in range(file.length):
        print(file.text[i])

text = File('1.txt', f_lines)
text1 = File('2.txt', f1_lines)
text2 = File('3.txt', f2_lines)
# print(text1.length)
# print(text1.text[0])
# # if (line_count1 < line_count) and (line_count1 < line_count2) and (line_count < line_count2):
print(print_file(text))





from pprint import pprint
import os

path = os.path.join(os.getcwd(),'recipes.txt')
with open(path, encoding="utf-8") as file:
    Book_of_recipes = {}
    for recipe in file:
        recipe_name = recipe.strip()
        counter = int(file.readline().strip())
        temp_data = []
        for item in range(counter):
            name, quantity, units = file.readline().strip().split('|')
            temp_data.append({'name':name.strip(),'quantity':quantity.strip(),'units':units.strip()})
        Book_of_recipes[recipe_name] = temp_data
        file.readline()
    print('Book of recipes =', end = ' ')
    pprint(Book_of_recipes, width = 150)
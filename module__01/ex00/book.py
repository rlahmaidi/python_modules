import sys
from datetime import datetime
from datetime import date
from recipe import Recipe

class Book:
    recipe_lst = []
    recipes_list = {"starter": [], "lunch": [], "dessert": []}
    def __init__(self, name, last_update = datetime.now, creation_date = datetime.now()):
        if isinstance(name, str) is False:
            print("name of book should be a string")
            sys.exit()
        else:
            self.name = name
        if isinstance(last_update, datetime.date) is False:
            print("last update(3rd arg) should be a datetime")
            sys.exit()
        else:
            self.last_update = last_update
        if isinstance(creation_date, datetime.date) is False:
            print("creation date(last arg) should be a datetime")
            sys.exit()
        else:
            self.creation_date = creation_date
        # if isinstance(recipes_list, dict) is False:
        #     print("the 2nd arg should be a dictionary")
        #     sys.exit()
        # else:
        #     self.recipes_list = recipes_list
    
    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        for i in recipe_lst:
            if i.name is name:
                return i
        
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        lst = []
        for i in recipe_lst:
            if i.recipe_type is recipe_type:
                lst.append(i)
        return lst
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is False:# to be tested
            print("you can only add propper recipes to this book")
        elif recipe.recipe_type is "desset":
            recipes_list["dessert"].append(recipe)
    
    def print_dectionary(self):
        print(recipes_list)


if __name__ == "__main__":
    book = Boo
    
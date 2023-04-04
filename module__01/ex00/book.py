import sys
from datetime import datetime
from datetime import date
from recipe import Recipe
import time 

class Book:
    # recipe_lst = []
    recipes_list = {"dessert": [], "starter": [], "lunch": []}
    def __init__(self, name, last_update = datetime.now(), creation_date = datetime.now()):
        if isinstance(name, str) is False:
            print("name of book should be a string")
            sys.exit()
        else:
            self.name = name
        if isinstance(last_update, datetime) is False:
            print("last update(3rd arg) should be a datetime")
            sys.exit()
        else:
            self.last_update = last_update
        if isinstance(creation_date, datetime) is False:
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
        for key in self.recipes_list.keys():
            for i in self.recipes_list[key]:
                if i is name:
                    print(i.__str__())
                    return
        return
        
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        types = ["dessert", "lunch", "starter"]
        if recipe_type  in types:
            for key in self.recipes_list.keys():
                if recipe_type is key:
                    return self.recipes_list[key]
        else:
            print("this type dosen't exist in the book")
            return
    
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if isinstance(recipe, Recipe) is False:# to be tested
            print("you can only add propper recipes to this book")
        elif recipe.type == 'desset':
            print("do we get inside the desired if")
            self.recipes_list["dessert"].append(recipe)
        else:
            self.recipes_list["dessert"].append(recipe)
        self.last_update = datetime.now()
        # print("from add printing the dictionary:")
        # print(self.recipes_list)
    
    def print_dectionary(self):
        print("we are now inside the print_dectionary")
        print("the name of the book is: ", self.name)
        print("the creation date is ", self.creation_date)
        print("the last update is: ",self.last_update)
        print("the book the following content")
        for key in self.recipes_list.keys():
            for i in self.recipes_list[key]:
                print(i.__str__())


# if __name__ == "__main__":
#     book = Book("first book")
#     recip = Recipe(
#     "lghda", 3, 23, ["haja", "haja1", "sdf"],
#     "chi haja katkal", "dessert")

#     recip1 = Recipe("l3cha", 5, 10, ["kafta, bassla, maticha, zit"],\
#                      "i'm cooking a ma9la now", "dessert")
#     # print(dir(recip))
#     # print(recip.__str__())
#     book.add_recipe(recip)
#     book.print_dectionary()
#     time.sleep(2)
#     book.add_recipe(recip1)
#     book.print_dectionary()
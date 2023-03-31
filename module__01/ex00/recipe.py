import sys


class Recipe:
    def __init__(
            self, name, cook_lvl, cook_time,
            ingredients, description, type):
        if isinstance(name, str) is False:
            print("the name of the recipe should be a string")
            sys.exit()
        else:
            self.name = name
        if isinstance(cook_lvl, int) is False or cook_lvl not in range(1, 6):
            print("the cooking level(2nd arg)\
                   should be an integer between 1 and 5")
            sys.exit()
        else:
            self.cook_lvl = cook_lvl
        if isinstance(cook_time, int) is False or cook_time < 0:
            print("the cooking time(3rd arg) should be a positive integer")
            sys.exit()
        else:
            self.cook_time = cook_time
        if isinstance(ingredients, list) is False:
            print("the ingredients[4th arg] should be a list of strings")
            sys.exit()
        elif all(isinstance(n, str) for n in ingredients) is False:
            print("the ingredients[4th arg] should be a list of strings")
        else:
            self.ingredients = ingredients
        if isinstance(description, str) is False:
            print("the description of the recipe(5th arg) should be a string")
            sys.exit()
        else:
            self.description = description
        lst = ["starter", "lunch", "dessert"]
        if isinstance(type, str) is False or type not in lst:
            print("the recipe type should be on of the\
                   following: starter-lunch-dessert")
            sys.exit()
        else:
            self.type = type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = "the recipe name is " + self.name\
        + "\nthe cooking level is " + str(self.cook_lvl)\
        + "\nthe cooking time is " + str(self.cook_time)\
        + "\nthe ingredients are" + ' '.join(self.ingredients)\
        + "\nthe description of the recipe is " + self.description\
        + "\nthe recipe type is " + self.type
        return txt

    def print_recipe_prop(self):
        print("the recipe name is ", self.name)
        print("the cooking lvl is ", self.cook_lvl)
        print("the cooking time is ", self.cook_time)
        print("the ingredients are", self.ingredients)
        print("the description of the recipe is ", self.description)
        print("the recipe type is ", self.type)
        return


# recipe = Recipe(
#     "lghda", 3, 23, ["haja", "haja1", "sdf"],
#     "chi haja katkal", "lunch")
# recipe.print_recipe_prop()
# to_print = str(recipe)
# print(to_print)

if __name__ == "__main__":
    recipe = Recipe(
    "lghda", 3, 23, ["haja", "haja1", "sdf"],
    "chi haja katkal", "lunch")
    # recipe.print_recipe_prop()
    # to_print = str(recipe)
    # print(recipe.__str__.__doc__)
    # print(to_print)
    print(recipe)
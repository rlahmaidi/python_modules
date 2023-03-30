import sys

cookbook = {
            "Sandwich": {"ingredient": ["ham", "bread", "cheese", "tomatoes"], "meal": "lunch", "prep_time": 10},
            "Cake": {"ingredient": ["flour", "sugar", "eggs"], "meal": "dessert", "prep_time":  60},
            "Salad": {"ingredient": ["avocado", "arugula", "tomatoes", "spinach"], "meal": "lunch", "prep_time": 15}
}


# 1. A function that print all recipe names.
def all_recipes_names():
    for key in cookbook:
        print(key)
    return


# 2. A function that takes a recipe name and print its details.
def recipe_details(recipe_name):
    if recipe_name not in cookbook:
        print("%s: recipe dosen't exist in the cookbook" % (recipe_name))
    else:
        print("recipe for %s:" % (recipe_name))
        print("             Ingredients list: %s" % cookbook[recipe_name]["ingredient"])
        print("             To be eaten for: %s" % cookbook[recipe_name]["meal"])
        print("             Takes %d minutes of cooking." % cookbook[recipe_name]["prep_time"])
    return


# 3. A function that takes a recipe name and delete it.
def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print("%s: recipe have been deleted successefully" % recipe_name)
    else:
        print("the recipe you want to delete dosen't exist in the cookbook")
    return


# 4. A function that add a recipe from user input. You will need a name, a list of
# ingredient, a meal type and a preparation time.
def add_recipe():
    name = input("what is the name of your recipe:\n")
    ingredient = " "
    print("Enter ingredients: ")
    ing_list = []
    while True:
        ingredient = input()
        if ingredient is "":
            break
        ing_list.append(ingredient)
    meal = input("what is the type  of your recipe?\n")
    while True:
        prep_time = input("how much time your recipe takes(NB: should be an integer)\n")
        if prep_time.isdigit() is True:
            break
    cookbook[name] = {"ingredient": ing_list, "meal": meal, "prep_time": int(prep_time)}
    return


def print_usage():
    print("\n\nList of available option:")
    print("     1: Add a recipe")
    print("     2: Delete a recipe")
    print("     3: Print a recipe")
    print("     4: Print the cookbook")
    print("     5: Quit")
    return


def print_cookbook():
    for key in cookbook.keys():
        recipe_details(key)


def call_appropriate_fun(inp):
    if inp is 1:
        add_recipe()
    if inp is 2:
        recipe_name = input("Please enter a recipe name to delete: \n")
        delete_recipe(recipe_name)
    if inp is 3:
        recipe_name = input("Please enter a recipe name to get its details:\n")
        recipe_details(recipe_name)
    if inp is 4:
        print_cookbook()
    if inp is 5:
        print("Cookbook closed. Goodbye !")
        sys.exit()
    return


if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    while True:
        print_usage()
        inp = input("Please select an option:\n")

        if inp.isdigit() is False or int(inp) > 5 or int(inp) < 1:
            print("Sorry, this option does not exist.")
            continue
        call_appropriate_fun(int(inp))

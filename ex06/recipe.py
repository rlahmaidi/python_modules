cookbook = {
            "Sandwich" : {"ingredient" : ["ham", "bread", "cheese" , "tomatoes"], "meal" : "lunch", "prep_time" : 10},
            "Cake" : {"ingredient" : ["flour", "sugar", "eggs"], "meal" : "dessert", "prep_time" :  60},
            "Salad" : {"ingredient" : ["avocado", "arugula", "tomatoes", "spinach"], "meal" : "lunch", "prep_time" : 15}
}
#1. A function that print all recipe names.
def all_recipe_names():
    for key in cookbook:
        print(key)
    return

#2. A function that takes a recipe name and print its details.
def recipe_details(recipe_name):
    if recipe_name  not in cookbook:
        print("%s: recipe dosen't exist in the cookbook" % (recipe_name))
    else:
        print("recipe for %s:" % (recipe_name))
        print("             Ingredients list: %s" % cookbook[recipe_name]["ingredient"])
        print("             To be eaten for: %s" % cookbook[recipe_name]["meal"])
        print("             Takes %d minutes of cooking." % cookbook[recipe_name]["prep_time"])
    return
        
#3. A function that takes a recipe name and delete it.
def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print("%s: recipe have been deleted successefully" % recipe_name)
    else:
        print("the recipe you want to delete dosen't exist in the cookbook")
    return

#4. A function that add a recipe from user input. You will need a name, a list of
#ingredient, a meal type and a preparation time.
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
    prep_time = input("how much time your recipe takes?\n")
    return


all_recipe_names()
add_recipe()
# recipe_details("Cake")
# delete_recipe("Cake")
# recipe_details("Cake")
all_recipe_names()
#print(cookbook)
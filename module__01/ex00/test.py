from recipe import Recipe
from book import Book

if __name__ == "__main__":
    recipe = Recipe(
    "lghda", 3, 23, ["haja", "haja1", "sdf"],
    "chi haja katkal", "lunch")
    recipe.print_recipe_prop()
    to_print = str(recipe)
    #print(to_print)
    book = Book("first book", )
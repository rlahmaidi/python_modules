from recipe import Recipe
from book import Book
import time

if __name__ == "__main__":
    book = Book("first book")
    recip = Recipe(
    "lghda", 3, 23, ["haja", "haja1", "sdf"],
    "chi haja katkal", "dessert")

    recip1 = Recipe("l3cha", 5, 10, ["kafta, bassla, maticha, zit"],\
                     "i'm cooking a ma9la now", "dessert")
    # print(dir(recip))
    # print(recip.__str__())
    book.add_recipe(recip)
    book.print_dectionary()
    time.sleep(2)
    book.add_recipe(recip1)
    book.print_dectionary()
    book = Book("first book", )
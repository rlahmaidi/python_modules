import sys
from datetime import datetime

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list):
        if isinstance(name, str) is False:
            print("name of book should be a string")
            sys.exit()
        else:
            self.name = name
        if isinstance(last_update, datetime) is False:
            print("last update(2nd arg) should be a datetime")
            sys.exit()
        else:
            self.last_update = last_update
        if isinstance(creation_date, datetime) is False:
            print("creation date(3nd arg) should be a datetime")
            sys.exit()
        else:
            self.creation_date = creation_date
        if isinstance(recipes_list, dict) is False:
            print("the last arg should be a dictionary")
            sys.exit()
        else:
            self.recipes_list = recipes_list
        
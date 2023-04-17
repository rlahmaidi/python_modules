class GotCharacter:
    """This the GotCharacter Class
        it tells the name of the character
        and wether it is alive or not"""
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        if is_alive in (True, False):
            self.is_alive = is_alive
        else:
            print("the is_alive can only be true of false")


class Stark(GotCharacter):
    """A class representing the Stark family. Or when bad
      things happen to good people."""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False


class Lannister(GotCharacter):
    """Fair-haired, tall and handsome and we win at whatever price"""
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "A Lannister Always Pays His Debts."

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

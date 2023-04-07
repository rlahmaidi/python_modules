class   GotCharacter:
    def __init__(self, first_name, is_alive = True):
        self.first_name = first_name
        if is_alive in (True, False):
            self.is_alive = is_alive
        else:
            print("the is_alive can only be true of false")

class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
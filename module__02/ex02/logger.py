from time import time,sleep
from random import randint
import os

def log(fun):
    def inner(ref, water_level = None):
        start = time()
        if water_level != None:
            result = fun(ref, water_level)
            end = time()
            exec_time = end - start
            to_print = "(cmaxime)Running: " + fun.__name__.ljust(20,) + "[ exec_time = {ex_time: .3f}".format(ex_time = exec_time) + " ms ]\n"
            log_file = open(r"machine.log","a")
            log_file.write(to_print)
            return result
        else:
            result = fun(ref)
            end = time()
            exec_time = end - start
            to_print = "(cmaxime)Running: " + fun.__name__.ljust(20,) + "[ exec_time = {ex_time: .3f}".format(ex_time = exec_time) + " ms ]\n"
            log_file = open(r"machine.log","a")
            log_file.write(to_print)
            return result
    return inner
    

        
# (cmaxime)Running: Start Machine [ exec-time = 0.001 ms ]
class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        # print("from start_machine")
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    @log
    def boil_water(self):
        return "boiling..."
    @log
    def make_coffee(self):
        # print("from make_coffe")
        if self.start_machine():
            for _ in range(20):
                sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    @log
    def add_water(self, water_level):
        # print("from add_water")
        sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    # print(machine.start_machine.__name__)
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)
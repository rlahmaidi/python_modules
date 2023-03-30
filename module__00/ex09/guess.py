import random
import sys


def congratulations(i):
    if i == 0:
        print("Congratulations! You got it on your first try!")
    else:
        i += 1
        print("You won in %d attempts!" % i)


if __name__ == "__main__":
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1\
           and 99 to find out the secret number.")
    print("Type 'exit' to end the game.")
    print("Good luck!")

    tries = 0
    while True:
        user_num = input("What's your guess between 1 and 99?\n")
        if user_num == "exit":
            print("Goodbye!")
            sys.exit()
        if user_num.isdigit() is False:
            print("That's not a number.")
            continue
        rand_num = random.randint(1, 99)
        user_num = int(user_num)
        if user_num > rand_num:
            print("Too high!")
        elif rand_num > user_num:
            print("Too low!")
        elif rand_num == user_num == 42:
            print("The answer to the ultimate question of life,\
                   the universe and everything is 42.")
            congratulations(tries)
            sys.exit()
        elif rand_num == user_num:
            print("Congratulations, you've got it!")
            congratulations(tries)
            sys.exit()
        tries += 1

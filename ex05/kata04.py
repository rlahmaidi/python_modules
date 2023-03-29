# Put this at the top of your kata04.py file
kata = (0, 4, 132.42222, 10000, 12345.67)

if __name__ == "__main__":
    print("module_%d%d, ex_0%d : %7.2f, %7.2e, %7.2e" % 
        (kata[0], kata[0], kata[1], kata[2], kata[3], kata[4]))

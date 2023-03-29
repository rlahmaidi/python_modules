# Put this at the top of your kata01.py file
kata = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }

if __name__ == "__main__":
    for key in kata:
        print(key, " was created by ", kata[key])

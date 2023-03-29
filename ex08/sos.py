import sys
import string
import json


if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("ERROR: the programm takes at least one argument")
        sys.exit()
    text = ""
    for i in range(1, len(sys.argv) - 1):
        text = text + sys.argv[i] + " "
    text = text +sys.argv[len(sys.argv) - 1]
    punc = string.punctuation
    for i in text:
        if i in punc:
            print("ERROR")
            sys.exit()
    text = text.lower()
    with open('morse_code.json') as morse_code:
        file_content = morse_code.read()
    #the type of file_content above is str that's why we parse it to a dictionary using loads methods
    morse_codes = json.loads(file_content)
    for i in text:
        print(morse_codes[i] + " ", end= "")

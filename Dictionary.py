import json
from difflib import get_close_matches

data = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    alt = get_close_matches(word, data.keys())
    if word in data:
        print(data[word])
    elif word.title() in data:
        print(data[word.title()])
    elif word.upper() in data:
        print(data[word.upper()])
    elif len(alt) > 0:
        print("do you mean %s instead" %alt[0])
        choice = input("y for yes, n for no: ").lower()
        if choice == "y":
            print(data[alt[0]])
        else:
            word = input("Please enter the right word: ")
            translate(word)
    else:
        print("Oops, the word does not exist")


trials = True
while trials:
    word = input('Please enter the word you want to search for\nType "exit to leave": ')
    if word == "exit":
        print("Thanks for coming, do have a wonderful day")
        trials = False
    else:
        result = translate(word)
        print(result)




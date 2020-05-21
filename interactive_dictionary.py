import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.title() in data:   #for checking words starting with capital letter. title() converts 1st letter of a word to capital
        return data[w.title()]

    elif w.upper() in data:   #for checking word where all letters are capital
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys(), n=3, cutoff=0.8)) > 0:
        yn = input("Did u mean any one in this list %s instead? Y/N: " % get_close_matches(w, data.keys(), n=3, cutoff=0.8))
        yn = yn.upper()
        if yn == "Y":
            i = int(input("Which word did you mean? Indicate your choice where the leftmost word is of index 0: "))
            return data[get_close_matches(w, data.keys(), n=3, cutoff=0.8)[i]] #returning the value of key

        elif yn == "N":
            return "Word doesn't exist"
        else:
            return "We didn't understand your entry"

    else:
        return "Word doesn't exist"

word = input("Enter a word: ")
output = meaning(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

# #1. read file => str
#   f = open("data.json")
#   text = f.read()
# #2. loads, str => dict
#   import json
#   dictionary = json.loads(text)

dictionary = {
    "Hallo": "Hello",
    "Tschuss": "Bye",
    "Danke": "Thanks",
}

while True:
    print(*dictionary)
    code = input("Your code? ")
    if code in dictionary: #Check
        print(dictionary[code])
        print()
        update = input("Do you want to update (Y/N)? ")
        if update == "Y":
            new_translation = input("Your translation? ")
            dictionary[code] = new_translation
            print(*dictionary)
            print("Done!")
    else:
        print("Not found!")
        contribute = input("Do you want to contribute (Y/N) ?").upper()
        if contribute == "Y":
            new_translation_nf = input("Your translation? ")
            dictionary[code] = new_translation_nf
            print(*dictionary)










from random import randint

word = "hexagon"
characters = list(word)

while len(characters) > 0:
    # 1. Select  character randomly
    i = randint(0, len(characters) - 1)
    ch = characters[i]

    # 2. Print selected character
    print(ch, end=" ")

    # 3. Remove selected character
    characters.pop(i)
    #print(characters)
print()

user_guess = input("Your answer: ")
if user_guess == word:
    print(True)
else:
    print(False)
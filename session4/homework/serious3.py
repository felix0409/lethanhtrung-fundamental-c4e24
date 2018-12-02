from random import randint

WORDS = ["window", "mac", "linux"]
word = WORDS[randint(0, len(WORDS)-1)]
char = list(word)
while len(char) > 0:
    i = randint(0, len(char) - 1)
    ch = char[i]
    print(ch, end=" ")
    char.pop(i)
print()

user_guess = input("Your answer: ")
if user_guess == word:
    print(True)
else:
    print(False)
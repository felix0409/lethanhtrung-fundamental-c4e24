while True:
    user = int(input("Guess my number 1-100? "))
    bingo = 45
    if user > bingo:
        print("Too large!")
    elif user < bingo:
        print("Too small!")
    else:
        print("Bingo!")
        break
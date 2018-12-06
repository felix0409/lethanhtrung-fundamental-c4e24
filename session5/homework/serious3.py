print("Answer the following algebra question")
print("If x = 8, then what is the value of 4(x+3) ?")
a = "Estimate this answer (exact calculation not needed)"
b = "Jack scored these marks in 5 math test: 49, 81, 72, 66 and 52. What is the mean?"
choices1 = [35, 36, 40, 44]
choices2 = [55, 65, 75, 85]

count = 0
for c in choices1:
   count += 1
   print(count, c, sep=". ") 
stop = True
while stop:
    answer = int(input("Your choice: "))
    if answer == 4:
        print("Bingo")
        print()
        print(a)
        print(b)
        count = 0
        for c in choices2:
            count += 1
            print(count, c, sep=". ")
        answer = int(input("Your choice: "))
        if answer == 2:
            print("Bingo")
            print("You answered correctly 2 out of 2 questions.")
            stop = False
        else:
            print("You answered correctly 1 out of 2 questions.")
            stop = False
    else:
        print(":(")
        print()
        print(a)
        print(b)
        count = 0
        for c in choices2:
            count += 1
            print(count, c, sep=". ")
        answer = int(input("Your choice: "))
        if answer == 2:
            print("Bingo")
            print("You answered correctly 1 out of 2 questions.")
            stop = False
        else:
            print("You answered correctly none of the questions.")
            stop = False
        
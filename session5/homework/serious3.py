a = "Answer the following algebra question"
b = "If x = 8, then what is the value of 4(x+3) ?"

choices1 = [35, 36, 40, 44]

print(a)
print(b)
count = 0
for c in choices1:
   count += 1
   print(count, c, sep=". ")

stop = True
while stop:
    answer = int(input("Your choice:"))
    if answer == 4:
        print("Bingo")
        stop = False**
    else:
        print(":(")
        stop = False


# 3. Nested conditionals is that one conditional can also 
# be NESTED within another.

n = int(input("Enter a number which is greater than 50: "))

if n == 50:
    print(n,"is not greater or less than 50!")
else:
    if n < 50:
        print(n, " is less than 50")
    else:
        print(n)
        print("Good job!")
    

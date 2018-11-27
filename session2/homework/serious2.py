n = int(input("Enter a number: "))
factorial = 1
for i in range(1, n+1, 1):
    factorial = factorial*i

print("The factorial of " + str(n) + " is", factorial)
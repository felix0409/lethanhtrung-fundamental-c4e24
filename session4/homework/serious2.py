flock = [5, 92, 10, 250, 35, 40, 66]
print("Hello, my name is Trung and these are my sheep sizes:",flock)

biggest = 0
for i in range(0, len(flock)):
        if flock[i] > biggest:
                biggest = flock[i]
     
print("Now my biggest sheep has size", biggest, end="")
print(", let's shear it!")

flock[flock.index(biggest)] = 8 #listindexfunc
print("After sheering, here is my flock:", flock)

for i in range(1, 4):
        after_flock = [x+(50*i) for x in flock]
        print()
        print("MONTH",i)
        print("One month has passed, now here is my flock:",after_flock)
        biggest = 0
        for i in range(0, len(after_flock)):
                if after_flock[i] > biggest:
                        biggest = after_flock[i]
        print("Now my biggest sheep has size", biggest, end="")
        print(", let's shear it!")
        after_flock[after_flock.index(biggest)] = 8
        print("After sheering, here is my flock:", after_flock)

total_size = 0
total_money = 0
for i in after_flock:
     total_size += i
print()
print("My flock has size in total:", total_size, end="")
print("$")

total_money = total_size * 2
print("I would get",total_size, end="")
print(" * 2$ = ", end="")
print(total_money, end="")
print("$")



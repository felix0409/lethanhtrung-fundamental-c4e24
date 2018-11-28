from random import randint
ran = randint(1, 100)
print(ran)

if ran < 30:
    print("RAINY")
elif ran < 60:
    print("Cloudy")
else:
    print("Sunny")

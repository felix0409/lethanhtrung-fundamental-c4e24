
height = int(input("Enter your height (cm): "))
weight = int(input("Enter Your weight? (kg): "))

cmtom = height/100
bmi = weight/(cmtom**2)

if bmi < 16:
    print("Severely underweight")
elif bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


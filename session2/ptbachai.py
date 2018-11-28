a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c
xkep = -b/(2*a)
x1 = (-b + delta**(1/2))/(2*a)
x2 = (-b - delta**(1/2))/(2*a)

if delta < 0:
    print ("Phuong trinh vo nghiem")
elif delta == 0:
    print ("Phuong trinh co 1 nghiem kep: ", xkep )
else:
    print("Phuong trinh co 2 nghiem phan biet: ", x1, x2)
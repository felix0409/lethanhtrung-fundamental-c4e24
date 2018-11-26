# 2. A flowchart is a type of diagram that represents an algorithm, workflow or process. The flowchart shows the steps as boxes of various kinds, and their order by connecting the boxes with arrows. This diagrammatic representation illustrates a solution model to a given problem. Flowcharts are used in analyzing, designing, documenting or managing a process or program in various fields 

a = int(input("a ?"))
b = int(input("b ?"))
c = int(input("c ?"))

delta = b**2 - 4*a*c

if delta < 0:
    print("Phuong trinh vo nghiem.")
elif delta == 0:
    xkep = -b/(2*a)
    print("Phuong trinh co mot nghiem kep: ", xkep)
else:
    x1 = (-b + delta**(1/2))/(2*a)
    x2 = (-b - delta**(1/2))/(2*a)
    print("Phuong trinh co 2 nghiem phan biet:")
    print("x1 = ", x1)
    print("x2 = ", x2)
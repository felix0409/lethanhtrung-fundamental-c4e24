dictionary = {}
strIn = input("Enter a string? ").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"
alp = list(alphabet)

for i in alp:
    dictionary[i] = strIn.count(i) #string.count(obj)  #so lan obj xuat hien trong list
    if dictionary[i] == 0:
        del dictionary[i]

for k in dictionary:
    print(k,dictionary[k])
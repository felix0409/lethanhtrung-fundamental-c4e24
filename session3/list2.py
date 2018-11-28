# list = ["apple"]
# ask = input("Do you wanna add something? ")
# list.append(ask)
# print(list)

favs = ["Teaching", "Netflix", "redbull"]
i = int(input("Enter an index to see your favorite things: "))
if i >= len(favs):
    print("Error")
else:
    print(favs[i])

# while True:
#     userType = int(input("Enter an index to see your favorite things: "))
#     if userType >= len(favs):
#         print("The number is longer than your list. Please enter a shorter one :) ")
#     else:
#         print(favs[userType])
#         break






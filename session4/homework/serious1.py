items = ["T-Shirt", "Sweater"]

while True:
    customer = input("Welcom to our shop, what do you want (C, R, U, D, E)?  ").upper()
    if customer == "R":
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif customer == "C":
        new_item = input("Enter new item: ")
        items.append(new_item)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif customer == "U":
        update_position = int(input("Update Position?  "))
        update_item = input("New item? ")
        items[update_position] = update_item
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif customer == "D":
        delete_item = int(input("Delete position?  "))
        items.pop(delete_item)
        print("Our items: ", end="")
        print(*items, sep=", ")
    elif customer == "E":
        print("Bye!")
        break
    
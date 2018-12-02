items = ["item1", "item2"]
print(*items, sep=", ")
cmd = input("What do you want (C,R,U,D,E) ?").upper() #
while True:
    if cmd == "C":
        create = input("What do you wanna add? ")
        items.append(create)
        print(*items, sep=", ")
    elif cmd == "R":
        # print(*items, sep=", ")
        for index, item in enumerate(items):
            print(index +1, item, sep=", ")
    elif cmd == "U":
        iUpdate = int(input("Position you want to update? "))
        new_update = input("Your update: ")
        items[iUpdate] = new_update
        print(*items, sep=", ")
    elif cmd == "D":
        iDelete = input("What do you want to delete? ")
        if iDelete == iDelete.isdigit():
            print("True")
        else:
            print("Flase")
        # if iDelete:
        #     items.remove(iDelete)
        # else:
        #     items.pop(int(iDelete))
        #     print(*items, sep=", ")
    elif cmd == "E":
        break
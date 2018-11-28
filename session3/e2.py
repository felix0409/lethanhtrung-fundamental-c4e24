while loop:
    p = input("Enter your password: ")
    if not (p.isupper() or p.islower()):
        break
print("OK")

# # su dung loop = true, loop = false de thoat khoi vong lap neu' phuc tap.
# loop = True 
# while loop:
#     p = input("Enter your password: ")
#     if not (p.isupper() or p.islower()):
#         loop = False
# print("OK")


# while True:
#     if len(p)>8:
#         if (not p.islower()) and (not p.isupper()) and (not p.isdigit()):
#             break
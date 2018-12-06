person = [
    {
        "name": "Huy",
        "VNDperHour": 20,
        "Hour": 25
    },
    {
        "name": "Quan",
        "VNDperHour": 30,
        "Hour": 30
    },
    {
        "name": "H.Duc",
        "VNDperHour": 25,
        "Hour": 15
    }
]

wage_list = [p["VNDperHour"]*p["Hour"] for p in person]
total = sum(wage_list)
print(total)

# sum = 0
# for p in person:
#     wage = p["VNDperHour"]*p["Hour"]
#     p["salary"] = wage
#     sum += p["salary"]
#     print(p["name"],p["salary"], sep=": ")
# print("Salaries:", sum)

#listcomprehension


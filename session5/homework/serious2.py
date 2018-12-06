prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for p in prices:
    print()
    print(p)
    print("prices: ", prices[p])
    print("stock: ", stock[p])
print()
total = 0
for p in prices:
    calc = prices[p]*stock[p]
    total += calc
    print(p, calc, sep =": ")

print("Total: ", total)
fruits = ["berries", "apples", "grapes","oranges"]
vegetables =["kale","brocoli","lettuce"]

fruits.extend(vegetables)
print(fruits)

vegetables.append("beans")
print(vegetables)

vegetables.sort()
print(vegetables)

vegetables.sort(reverse=True)
print(vegetables)

print(fruits.count("berries"))

print(fruits.index("grapes"))

vegetables.insert(1 , "carrot")
print(vegetables)

fruits.pop()
print(fruits)

vegetables.remove("kale")
print(vegetables)

del vegetables
print(vegetables)
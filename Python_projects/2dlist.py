fruits = [
    ["apples", "berries", "kiwi"],
    ["oranges", "berries", "plums"],
    ["mangoes", "banana", "coconuts"],
    ["pineapples"]
]
print(fruits[1][1])

for row in fruits:
    for col in row:
        print(col)
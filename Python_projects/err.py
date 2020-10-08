#print(x)


x =20
try:
    print(x)
except:
    print("value is not definrd")
else:
    print("Hello")
finally:
    print("You may get an error if no variable is specified")

while True:
    try:
        n = int(input("enter a whole number"))
        break
    except ValueError:
        print("No valid integer entered")

print("great you have entered an integer")

c = 12/0
print(y)
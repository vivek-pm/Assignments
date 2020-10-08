def mynum(a):
    def num(a):
        return a + 1
    result = num(a)
    return result
print(mynum(4))

def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()
display_message("Show me the money!!")

def dream_home():
    pass

def mynum(b):
    return b + 1
def addnum(c):
    newnum = 7
    return c(newnum)
print(addnum(mynum))

def total_numbers(a=7, *numbers , **phonebook):
    print("my fav number is ",a)

    for num in numbers:
        print("num ", num)

    for name,phone_number in phonebook.items():
        print(name,phone_number)
total_numbers(7,1,2,3,jane=2222, john=4444, Angela= 5555)

a = lambda b: b + 4
print(a(4))

c= lambda d, e : d + e
print(c(7,8))

def add_numbers(d,e):
    '''Adding two numbers.
    The values must be integers '''

    print(d+e)
add_numbers(8,4)
print(add_numbers.__doc__)

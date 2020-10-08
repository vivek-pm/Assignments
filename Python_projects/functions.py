def sum(x, y):
    c = x + y
    print(c)
    return c

sum(4, 5)
print(sum(8,4))

def student_names(names="Vivek"):
    print("Hello " + names)
student_names()
student_names("Kurian")

def more_num(a,b=7,c=10):
    print("a is ", a, "and b is", b, "while c ic ", c )
more_num(3, 7)
more_num(23, c=17)
more_num(c=40, a=80)
more_num(23, 15, c=20)

def greetings():
    def say_hello():
        return "Hello"
    return say_hello()
hello=greetings()
print(hello)
print(greetings())

def mynum(x):
    return x + 1
num = mynum
print(num(7))
print(mynum(10))

x = 10

def my_numbers(x):
    print(x)
    x = 7
    print("local X is ", x)
my_numbers(x)






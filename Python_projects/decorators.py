def my_decorator(function):
    def wraper():
        myfunc = function()
        convert_uppercase = myfunc.upper()
        return convert_uppercase
    return wraper
@my_decorator
def say_hello():
    return "hello wrold"
'''decorate=my_decorator(say_hello)'''
print(decorate())
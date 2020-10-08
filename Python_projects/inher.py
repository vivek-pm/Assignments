class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

florist = Person("Jane","Flowers")
florist.printname()

class Lawyers(Person):
    def __init__(self, fname, lname, casetype):
        Person.__init__(self, fname, lname)
        self.casetype = casetype
        #self.firstname = fname
        #self.lastname = lname

    def printinfo(self):
        print("Hello my name is", self.firstname, self.lastname)

happy_lawyers = Lawyers("Jack","smiley","criminal")
happy_lawyers.printinfo()
happy_lawyers.printname()

print(happy_lawyers.casetype)
class Instructors:
    companyName = "bluelime"

    def __init__(self,course, duration):
        self.course = course
        self.duration = duration

    def printinfo(self):
        print("My Company name is ", Instructors.companyName)

elearning = Instructors("Python for beginners", 7)

bls = Instructors("Django for beginners", 8)

bls.course = "HTML"

bls.printinfo()

print(bls.course)
print(bls.duration)
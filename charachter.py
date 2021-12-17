class Doctor:
    def char(self):
        return "I am Doctor"


class Person:
    def char(self):
        return "I am Normal Client(Person)"


a = Person()
b = Doctor()
for human in (a, b):
    human.char()

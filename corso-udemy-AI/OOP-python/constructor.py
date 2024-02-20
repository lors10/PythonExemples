
class Person:

    # class variables
    gender = "male"

    # constructor (or initialization block
    def __init__(self, name, surname, age):
        # these are instance variables
        self.name = name
        self.surname = surname
        self.age = age
        #self.gender = gender

    def show_info(self):

        return "My name is %s %s. I'm %s years old" % (self.name, self.surname, self.age)


#p = Person("Lorenzo", "Salvi", 30, "male")
p1 = Person(name="Lorenzo", age=30, surname="Salvi")
p2 = Person(name="Andrea", age=33, surname="Salvi")
print(p1.show_info())
print(p2.show_info())
print(p1.gender)
print(p2.gender)

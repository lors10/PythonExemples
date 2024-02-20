
# class
# encapsulation: we are able to group certain variables and functions
class Person:
    name = "Lorenzo"
    surname = "Salvi"
    age = 30
    gender = "male"

    def print_info(self):
        # print the variable values of the class
        print("My name is: " + self.name)
        print("My surname is: " + self.surname)
        print("I'm {} old".format(self.age))
        print("I'm a " + self.gender)


# instantiate a class: "p" is an object
p = Person()

p.print_info()



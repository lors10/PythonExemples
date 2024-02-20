

# inheritance allow us to define a class (child class or derived class) that
# inherits all the propertiesnd and functions from another class. We can
# define a given behavior only once in a class and then we can reuse this
# behavior in other classes without code duplication

class Person:

    # class variables
    name = 'Lorenzo'
    surname = 'Salvi'
    gender = 'male'

# child class
class Job(Person):

    # class variable
    profession = 'student'

p = Job()

print(p.name + " " + p.surname + " " + p.gender + " " + p.profession)

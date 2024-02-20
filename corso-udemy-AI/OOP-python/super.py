
class Account:

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def show_info(self):
        print("These are your general account info!")

class IgAccount(Account):

    def __init__(self, username, password, age):
        # super key-word
        super().__init__(username, password)
        self.age = age

    # override
    def show_info(self):
        print("These are your IG account info!")


login_account = IgAccount('lors10', 'password1', "30")
login_account.show_info()

print(login_account.username + " " + login_account.password + " " + login_account.age)


# __str__ function
# __eq__ function
# __gt__ function
# ....

class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


    # overriding functions: comparing objects
    def __str__(self):

        print(self.name + " " + self.age)

    def __lt__(self, other):

        return self.age < other.age

    def __gt__(self, other):

        return self.age > other.age

    def __eq__(self, other):

        return self.age == other.age

p1 = Person("Lorenzo", 30)
p2 = Person("Andrea", 33)

print(p1 < p2)
print(p1 > p2)
print(p1 == p2)

#p1.__str__()


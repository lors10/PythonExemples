"""
a function is a block statement that performs a specific tasks

- a function is defined using the "def" keyword
- we can pass data("parameters") into a function
- functions may "return data" (or can be "void")

"""

"""

- *args: if we're unsure about the number of parameters (tuple)

- keyword arguments: we can define key-value pairs

- **kwargs: if you're unsure about the number of keyword arguments (dictionary or arguments)

- you can define default values for the parameters: so if you call the given function without
  an argument the the default value is be used
  
- pass: function body can not be empty in Python. If you want to construct an empty function 
  then yuo have to use pass

"""

# parameters and arguments
def show_name(name): # parameter

    # local variable
    age = 10    # age è int quindi non posso concatenarlo ad una stringa (lo strasformo in stringa o ...)

    print("Name: " + name)
    print("Age: {}".format(age))


show_name("Lorenzo") # argument

def show_name_age(name, age): # positional parameter: the order does matter

    print("Name: " + name)
    print("Age: {}".format(age))


show_name_age("Lorenzo", 10) # argument

def show_name_age_one(name, age): # keyword: the order does not matter

    print("Name: " + name)
    print("Age: {}".format(age))


show_name_age_one(age=10, name="Lorenzo") # argument

def show_names(*names): # positional parameter: the order does matter

    # tuple: one dimensional array so we can use indexes

    # print names manually
    #print(names[0])
    #print(names[1])
    #print(names[2])

    # print names dinamically
    for index in range(len(names)):
        print(names[index])

show_names("Cesare", "Ida", "Andrea", "Lorenzo")

# keyword argument - ** to rapresent an arbitrary number of keyword arguments
def funct_double_asterisc(**params):
    # so it is a dictionary with key and value pairs
    print(params["fname"])
    print(params["fsurname"])
    print(params["fage"])
    print(params["fgender"])

funct_double_asterisc(fname="Lorenzo", fsurname="Salvi", fage=20, fgender="male")


# define a function without a body
def function_no_body(name, surname):
    pass

print("Before calling the fuction...")
function_no_body("Lorenzo", "Salvi")
print("After calling the function...")
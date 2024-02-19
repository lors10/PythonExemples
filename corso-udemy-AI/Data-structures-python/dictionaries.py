
# dictionaries in Python contain key-value pairs
#my_dictionarie = {"name": "Lorenzo", "age": 30, "gender": "male"}
#my_dictionarie = dict(name="Lorenzo", age=30, gender="male")
my_dictionarie = {"name":{"first-name": "Lorenzo", "last-name": "Salvi"}, "age": 30, "gender": "male"}

print(my_dictionarie["name"])
print(my_dictionarie["age"])
print(my_dictionarie["gender"])

print(len(my_dictionarie))

#my_dictionarie["name"] = "Lorenzo Salvi"
#print(my_dictionarie["name"])

for key in my_dictionarie:
    print(key)

print(my_dictionarie.items())

for key, value in my_dictionarie.items():
    print(key+": "+str(value))


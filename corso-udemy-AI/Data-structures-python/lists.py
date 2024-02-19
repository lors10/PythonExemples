
# usually this is called an array - but in Python it's called list
# if you want to use an array - then use NumPy arrays

my_list = [1, 4, 10, 5]

my_second_list = ["string", 10, 4.5]

print(my_second_list)
print(my_second_list[2])

my_second_list[2] = "ciao!" # change an item in the list
print(my_second_list)
print(my_second_list[2])

del my_second_list[2]   # delete an item in the list
print(my_second_list)

my_second_list.append("New Item!")  # add a new item at the end of the list
print(my_second_list)

result = my_list + my_second_list # combine lists
print(result)

my_list.extend(my_second_list) # append a list to another one
print(my_list)

my_second_list.pop()
print(my_second_list)

my_second_list.reverse()
print(my_second_list)

num_list = [1, 5, 7, 8, 18, 20, 15, 11]
num_list.sort() # reorder numbers
print(num_list)

my_third_list = (list(my_list))

for item in my_third_list:
    print(item)

print(len(my_third_list))
print(type(my_third_list))

# list comprehension: allows us to create a new list based on existing values of another list

number = [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
even_list = []

for item in number:

    if item % 2 == 0:
        even_list.append(item)

print(even_list)
print(number)

"""

even_list = [num for num in number if num % 2 == 0]     # we can simplify the loop!
print(even_list)




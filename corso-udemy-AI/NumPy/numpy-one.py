
import numpy as np

#print(np.__version__)  1.24.4

# we can create a numpy array from a list

python_list = [1, 2, 3, 4]

np_array = np.array(python_list)    # from python list to numpy array
print(np_array)
print(type(np_array))

a = np.array([1, 2, 3, 4, 5])
print(a)
print(type(a))

# we can store different types in Python BUT NOT with NumPy
# NumPy isn't able to store items with different types
b = np.array([1, 'Ciao', True, 3.55])

print(b)    # prints all values as String

# we can update the values based on indexes
b[1] = 10
b[2] = 5
b[3] = 15

print(b)

# we can insert new items with the insert() function
b = np.insert(b, 0, 30)     # insert '30' as first element
print(b)

# we can print the array's size
print(a.size)

# we can print the array's dimension
print(a.ndim)

# we can print the array's shape (number of items in each dimension)
print(a.shape)

c = np.array([[1, 2, 3, 4],['a','b','c','d']])
print(c)
print(c.ndim)
print(c.shape)  # prints (2, 4): 2 rows and 4 columns

print(c[0][0])
print(c[1][3])

# how to access to the items within one or multidimensional array
for index, row in enumerate(c):
    #print(index)
    #print(row)

    for item in row:
        print(item)

# update a multidimensional array's value
c[1][3] = 'e'
print(c)

d = np.array([[[1, 2, 3, 4],['a','b','c','d'],['e', 'f', 'h', 'i']]])
print(d)
print(d.shape)
print(d.ndim)

e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# indexes
print(e[5])
print(e[-1])

#slicing
print(e[1:10:2])
print(e[10:0:-2])

#reshape() function

print(e)
e = e.reshape(5, 2)
print(e)

# join and concatenate numpy array

a = np.array([[1, 2, 3], [4, 5 ,6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

# concatenate array (vertival-stack)
result = np.vstack((a, b))
print(result)

print(type(a))
print(type(b))
print(type(result))

print(a.ndim)       # one dimensional
print(result.ndim)  # bidimensional

print(result.shape)

# merge (join) array (horizontal-stack)
result = np.hstack((a, b))
print(result)

# stack function
result = np.stack((a, b), axis=0)   # create sub-array
print(result)

# filtering
f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
boolean_array = [True, True, True, True, True, False, False, False, False, False]

result = f[boolean_array]
print(result)

result = f > 5
print(f[result])



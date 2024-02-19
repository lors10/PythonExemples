
# list - []
# tuple - ()

my_tuple = ('Lorenzo', 30, True)
print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])

for item in my_tuple:
    print(item)

# my_tuple.append('Ciao') error! Tuples non are lists...

my_second_tuple = ('Ciao')

for item in my_second_tuple:
    print(item)
    # in this way, i print letters...

my_third_tuple = ('Ciao',)

for item in my_third_tuple:
    print(item)
    # now i print words...

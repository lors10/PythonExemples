"""
break and continue keywords:

- break: we can STOP the given loop before it has looped through all the items

- continue: we can SKIP (stop) the actual iteration of a loop and continue with the next iteration

"""

counter = 0

for number in range(0, 10, 1):

    if number == 5:
        continue

    elif number == 6:
        break

    print(number)


print("Finished...")
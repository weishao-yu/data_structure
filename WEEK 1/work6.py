# PF
T = int(input())

for _ in range(T):
    n = int(input())
    names = []
    for _ in range(n):
        name = input()
        names.append(name)
    print("Hello " + ", ".join(names))

# The Python String join() method takes all items in iterable and joins them into one string. 
# This method is helpful to generate strings from a list, tuples, and sets.


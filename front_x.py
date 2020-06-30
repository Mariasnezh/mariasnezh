list1 = []
list2 = []
emp = ""

while True:
    line = input()
    if line.strip() == emp:
        break
    a = line.startswith('x')
    if a:
        list1.append(line)
        list1.sort()
    else:
        list2.append(line)
        list2.sort()

list3 = list1 + list2

#print(list1)
#print(list2)
print(list3)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

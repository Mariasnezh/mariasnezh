list1 = []
list2 = []
emp = ""
while True:
    line = input()
    if line.strip() == emp:
        break
    list1.append(line)
    list1.sort()
print(list1)
while True:
    line = input()
    if line.strip() == emp:
        break
    list2.append(line)
    list2.sort()
print(list2)

list3 = list1 + list2
list3.sort()
print(list3)

#наверное, я не поняла задание
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

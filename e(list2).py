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

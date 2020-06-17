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

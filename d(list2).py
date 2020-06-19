list = []
list2 = []
emp = ""

while True:
    line = input()
    if line.strip() == emp:
        break
    list.append(int(line))

print(list)

i = 0
while i < len(list):
    if list[i] - list[i-1] != 0:
        list2.append(list[i])
    i += 1
print(list2)

#сама не знаю как это получилось, но вроде работает

list = []
emp = ""
i = 0
while True:
    line = input()
    if line.strip() == emp:
        break
    list.append(line)
    if len(line) >= 2 and line[0] == line[-1]:
        i = i+1
print(list)
print(i)

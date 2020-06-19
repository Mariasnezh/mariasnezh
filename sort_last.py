list = []
emp = ""

while True:
    line = input()
    if line.strip() == emp:
        break
    tup = tuple(line)
    list.append(tup)
print(sorted(list, key=lambda tup: tup[-1]))

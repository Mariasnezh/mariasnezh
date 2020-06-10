a = str(input())
b = str(input())

if len(a) % 2 == 0:
    c = int(len(a) / 2)
else:
    c = int(len(a) / 2 + 0.5)

if len(b) % 2 == 0:
    d = int(len(b) / 2)
else:
    d = int(len(b) / 2 + 0.5)

result = (a[0:c]+b[0:d]+a[c:]+b[d:])
print(result)

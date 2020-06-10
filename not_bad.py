a = str(input())
b = a.find('not')
c = a.find('bad')
if b == -1 or c == -1:
    print(a)
elif b < c:
    print(a[0:b]+'good'+a[c+3:])
else:
    print(a)

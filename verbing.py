a = str(input())
b = a.endswith('ing')
if len(a) < 3:
    print(a)
elif not b:
    print(a + 'ing')
else:
    print(a.replace('ing', 'ly'))

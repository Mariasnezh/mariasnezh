a = str(input())
b = a.endswith('ing')
c = a + 'ing'
d = a.replace('ing', 'ly')
if len(a) < 3:
    print(a)
elif b == False:
    print(c)
elif b == True:
    print(d)

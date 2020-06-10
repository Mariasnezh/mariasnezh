a = str(input())
b = a.endswith('ing')
c = a + 'ing'
d = a.replace('ing', 'ly')
if len(a) < 3:
    print(a)
elif not b:
    print(c)
elif b:
    print(d)    
    

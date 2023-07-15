m=input()
s='aeiouAEIOU'
l=[]

for i in m:
    if i in s and i not in l:
        l.append(i)
if(l==[]):
    print('-1')
else:
    print(*l)
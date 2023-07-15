m=input()
s='aeiou'
l=[]
f=0
for i in m:
    if i in s and i not in l:
        l.append(i)
l.sort()
l=''.join(l)
print(l==s)
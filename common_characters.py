a=list(input().lower().replace(' ',''))
b=list(input().lower().replace(' ',''))
s=[]
for i in a:
    if i in b and i not in s:
        s.append(i)
s.sort()
s=''.join(s)
print(s) if s else print('-1')
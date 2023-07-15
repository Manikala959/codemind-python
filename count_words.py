s=input().lower().split()
m='aeiou'
c=0
for i in s:
    if i[0] in m:
        c+=1
print(c)
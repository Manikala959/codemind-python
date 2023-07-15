s=input().replace(' ',' ')
c=0
for i in s:
    if i.islower():
        c+=1
print(c)
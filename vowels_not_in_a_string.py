m=input()
s='aeiou'
l=[]

for i in m:
    if i in s:
        l.append(i)
f=0
for i in s:
    if i not in l:
        f=1
        print(i,end=' ')
if(f==0):
    print('0')

a=[1,2,0,0,0]
b=[2,4,3]
c=[]

for i in a:
    if (i!=0):
        c.append(i)
for j in b:
    if (j!=0):
        c.append(j)
c.sort()
print(c)
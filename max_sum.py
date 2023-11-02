a=[3,2,3]
a.sort()
b=[]
c=0
for i in a:
    for j in a:
        if (i==j):
            c+=1
    b.append(c)
    c=0
print(b)
print(max(b))
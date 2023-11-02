x=[-2,-1,1,2]
c=[]
for i in range(len(x)-1):
    a=x[i]
    b=x[i+1]
    if ((a>0 and b<0) or (a<0 and b>0)):
        if (abs(a)>abs(b)):
            if (a not in c):
                c.append(a)
        if (abs(b)>abs(a)):
            if (a in c):
                c.remove(a)
            c.append(b)
    else:
        if (a==x[0]):
            c.append(a)
            c.append(b)
        else:
             c.append(b)
print(c)
d=[]
for i in range(len(c)-1):
    a=c[i]
    b=c[i+1]
    if ((a>0 and b<0) or (a<0 and b>0)):
        if (abs(a)>abs(b)):
            if (a not in d):
                d.append(a)
        if (abs(b)>abs(a)):
            if (a in d):
                d.remove(a)
            d.append(b)
    else:
        if (a==x[0]):
            d.append(a)
            d.append(b)
        else:
             d.append(b)

print(d)

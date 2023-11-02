a=[7,1,5,3,6,4]
x=[]
for i in range(len(a)):
    b=i
    m=0
    for i in range(b,len(a)):
            if (m<a[i]):
                m=a[i]
    c=(a.index(m))
    
    x.append(a[c]-a[b])
print(max(x))


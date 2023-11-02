a=[1,2,3]
l=len(a)
for i in range(len(a)//2):
    t=a[i]
    a[i]=a[l-1]
    a[l-1]=t
    l-=1
    i+=1
print(a)
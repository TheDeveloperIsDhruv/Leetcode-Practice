a=[1,2,3,4]
l=len(a)-1
for i in range(2):
    x=a[len(a)-1]
    a=a[0:l]
    print("Removing last elemnt",a)
    a.insert(0,x)
    print("Inserring removed elemnt at zero index",a)
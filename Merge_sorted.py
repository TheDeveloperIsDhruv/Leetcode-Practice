nums1=[0]
nums2=[1]
a=[]
for i in nums1:
           if (i!=0):
               a.append(i)
nums1=[]
nums1+=a
for i in nums2:
            if (i!=0):
                nums1.append(i)
print(nums1)
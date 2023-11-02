nums=[1,1,2,3,4,4]
a=[]
for i in range(len(nums)):
    for j in range(len(nums)):
            if (nums[i]==nums[j]):
                if (nums[i] not in a):
                        a.append(nums[i])
print(a)
print(nums)
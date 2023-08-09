nums = [3, 2, 4, 4, 3, 4,  3, 1, 3, 4, 3] 
tot=0
for i in range(len(nums)):
    count=0
    for j in range(len(nums)):
        if nums[i]==nums[j]:
            count=count+1 
        if count>tot:
            total=count
            majority=nums[i]  
print(majority,"is a majority element")
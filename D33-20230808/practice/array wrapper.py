# Input: nums = [[1,2],[3,4]], operation = "Add" 
# Output: 10

# nums = [[1,2],[3,4]]
# add=0
# list=[]
# for data in nums:
#     for data1 in range(len(nums)-1):
#         added=data[0]+data[1]
#         list.append(added)
#         for data2 in list:
#             add=add+data2
# print(add)  static




nums = [[1,2],[3,4]]
action=(input("Enter the action to be done : "))
add=0
list=[]
for data in nums:
    for data1 in range(len(nums)):
        if action=="add":
            add=add+data[data1]
        elif action=="string":
            list=list+[data[data1]]
if action=="add":
    print(add)
else:
    print(str(list))
    
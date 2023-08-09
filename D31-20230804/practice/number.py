nums = [2, 3, 5, 4, 7, 9, 8, 5]
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if i+j==9:
            print("pairs found",i,j)




            
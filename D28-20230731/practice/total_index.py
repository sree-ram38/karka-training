list=[4,6,7,1,8,9,5]
for i in range(len(list)):
    for j in range(len(list)):
        total=list[i]+list[j]
        if total==10:
            print(i,j)
x=int(input("enter the size of list:"))
y= int(input("enter the size of sublist:"))
list1=[]
sublist=[]
for i in range(x):
    for j in range(y):
        sublist.append(input())
    list1.append(sublist)
    sublist=[]
print (list1)
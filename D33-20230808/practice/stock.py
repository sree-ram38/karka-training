# a= [100,180,260,310,40,535,695]
# compare=0
# for data in range(len(a)):
#     for data1 in range(1,len(a)):
#         decrement=a[data]-a[data1]
#         if decrement>compare:
#             compare=decrement
# print(compare)
a=int(input("Enter the value : "))
a1=0
amd=[]
while a1<a:
    amoun=int(input("Enter the amount : "))
    amd=amd+[amoun]
    a1+=1
print(amd)
for data in range(len(amd)):
    for data1 in range(1,len(amd)):
        decrement=amd[data1]-amd[data]
        if decrement>a1:
            a1=decrement
            a2=data
            a3=data1
print(a1,(a2,a3))

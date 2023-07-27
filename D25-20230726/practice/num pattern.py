# inp=int(input("Enter the number : "))
# val=1
# for data in range(inp):
#     for data1 in range(inp):
#         print(val,end=" ")
#         val+=1
#     print("")


inp=int(input("Enter the number : "))
for data in reversed(range(1,(inp*inp)+1)):
    if data%inp==0:
        print("")
    print(data,end=" ")

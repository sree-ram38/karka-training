# val=5
# for data in range(1,val+1):
#     print("*"*data)
#     for data in range(data-1,0,-1):
#         print("*"*data)
#     print("")


# val=int(input("Enter the value : "))
# for data in range(1,val):
#     for data in range(data,0,-1):
#         print("*",end="")
#     print("")
# for data in range(val,0,-1):
#     for data in range(data,0,-1):
#         print("*",end="")
#     print("")   


# a=int(input("Enter the number: ")) 
# for data in range(1,a*2):
#     if data<=a:
#     print()


val=int(input("enter the val : "))
for data in range(1,val*2):
    if data<=val:
        data1=data
    else:
        data1=(val*2)-data
    for data in range(data1):
        print("*",end="")
    print("")
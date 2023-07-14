# def interest(principle,number,rate):
#     pnr=principle*number*rate/100
#     return pnr

# principle=100
# number=200
# rate=300
# ret=interest(principle,number,rate)
# print(ret)




def interest(principle,number,rate):
    pnr=principle*number*rate/100
    return pnr

principle=int(input("Enter the value of principle :"))
number=int(input("Enter the value of number of year :"))
rate=int(input("Enter the value of interest :"))
ret=interest(principle,number,rate)
print(ret)
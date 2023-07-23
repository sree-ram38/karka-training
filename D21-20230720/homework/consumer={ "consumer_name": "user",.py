consumer={   "consumer_name": "user",
    "eb reading": [1100, 1200, 1350, 1400, 2050]
}
zero=0
for data in range(0,4):
    # print(data)
    cal=consumer["eb reading"][data+1]-consumer["eb reading"][data]
    print(cal)
    if cal<100 :
        e=cal
        print("Unit consumed : ",cal)
        print("There is no amount to pay")
    elif cal>=100 and cal<200:
        a=cal*2
        print("Month : 2")
        print("Unit consumed : ",cal)
        print("Total amount :",a)
    elif cal>=200 and cal<500:
        b=cal*5
        print("Month : 3")
        print("Unit consumed : ",cal)
        print("Total amount :",b)
    elif cal>=500 and cal<1000:
        c=cal*10
        print("Month : 4")
        print("Unit consumed : ",cal)
        print("Total amount :",c)
    elif cal>=1000:
        d=cal*14
        print("Month : 5")
        print("Unit consumed : ",cal)
        print("Total amount :",d)
    

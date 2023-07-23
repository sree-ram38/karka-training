consumer={"name":"RAM","eb reading":[1100,1200,1450,1700,2004]}
reading=consumer["eb reading"]
# print(reading)

total=0
list=[]
for data in range(1,len(reading)):
    cal=reading[data]-reading[data-1]
    dic={
    "month":0,
    "unit_consumed":0,
    "bill-amount":0,
    }
    # print(cal)
    unit_amount =0
    if cal<100:
        print(unit_amount)
    elif cal>=100 and cal<=200:
        unit_amount = cal*2
    elif cal>=200 and cal<500:
        unit_amount = cal*5
    elif cal>=500 and cal<1000:
        unit_amount = cal*10
    elif cal>=1000:
        unit_amount = cal*14

    dic["month"]=data
    dic["unit_consumed"]=cal
    dic["bill-amount"]=unit_amount

    # print(dic)

    list.append(dic)
print("list",list)


new=open("/home/sreeram/karka/D21-20230720/homework/eb.txt","w")
new.write(str(list))
new.close()

new=open("/home/sreeram/karka/D21-20230720/homework/eb.txt","r")
# new.read()
print(new.read())

    
consumer={   "consumer_name": "user",
    "eb reading": [1100, 1200, 1450, 1700, 2050]
}
total=0
in=[{"Month":1,"Unit":"rs","Bill amount":"total"},{"Month"}]

for data in range(0,4):
    cal=consumer["eb reading"][data+1]-consumer["eb reading"][data]
    rs =0
    if cal<100:
        print(rs)
    elif cal>=100 and cal<=200:
        rs = cal*2
    elif cal>=200 and cal<500:
        rs = cal*5
    elif cal>=500 and cal<1000:
        rs = cal*10
    elif cal>=1000:
        rs = cal*14
    
    total+=rs
    print(rs)
    print("total",total)
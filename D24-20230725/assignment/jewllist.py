jewel=[
        {
            "month":"january",
            "gold_rate":1500,
            "jewel_list":[{"name":"chain","making_cost":13},
                          {"name":"ring","making_cost":15}
                         ]
        },
        {
            "month":"february",
            "gold_rate":1600,
            "jewel_list":[{"name":"chain","making_cost":11},
                          {"name":"ring","making_cost":20}                          
                         ]
        },
        {
            "month":"march",
            "gold_rate":2000,
            "jewel_list":[{"name":"chain","making_cost":26},
                          {"name":"ring","making_cost":22}
                         ]
        }
    ]

month=None
for data in jewel:
    gold=data["gold_rate"]
    dict={}
    for val in data["jewel_list"]:
        making=val["making_cost"]
        name = val['name']
        month=data["month"]
        dict["Month"]=month
        dict["Gold rate"]=gold
        dict[name]=making
        percentage=gold*making/100
        final_amount=gold+percentage
        # print("Month : ",month,"\n","Gold rate : ",gold,"\n", name,final_amount)
jewel.remove
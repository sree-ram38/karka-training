monthly_gold_rate=[{"month":"January","Gold rate":1000},
                   {"month":"February","Gold rate":950},
                   {"month":"March","Gold rate":1500},
                   {"month":"April","Gold rate":1600},
                  ]
# assigning
min_rate=monthly_gold_rate[0]["Gold rate"]
max_rate=0
# assigning
min_month=None
max_month=None

for data in monthly_gold_rate:
    if data["Gold rate"]<min_rate:
        min_month=data["month"]
        min_rate= data["Gold rate"]

    elif data["Gold rate"]>max_rate:
        max_month=data["month"]
        max_rate=data["Gold rate"]

print("Minimum value : ",min_rate,"\n""Month : ",min_month)
print("\n")
print("Maximum value : ",max_rate,"\n""Month : ",max_month)

    
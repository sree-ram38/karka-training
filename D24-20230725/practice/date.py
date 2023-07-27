# from datetime import date,time,datetime
# curr_date=date(2023,7,25)
# curr_date=date.today()
# curr_date=date.today().year
# curr_date=date.today().month
# curr_date=date.today().day
# # print(curr_date)

# curr_time=time(12,20,34)
# curr_time=time(12,20,34).hour
# curr_time=time(12,20,34).minute
# curr_time=time(12,20,34).second



# curr=datetime(2023,7,25,12,30,36)
# curr=datetime.now()
# curr1=curr.strftime("%d-%m-%y")
# curr2=curr.strftime("%m")
# print(curr2)

# from datetime import datetime
# from pytz import timezone

# date = datetime(2021, 6, 15, 8, 45, 17, 5)

# aware=datetime.now(timezone("IST"))
# print(aware)




from datetime import datetime
import pytz

aware= datetime.now(pytz.timezone("Asia/Kolkata"))
print("India", aware)
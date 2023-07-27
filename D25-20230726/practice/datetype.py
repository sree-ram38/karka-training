from datetime import datetime
date_str="25 may 2022"
tye_date=datetime.strptime(date_str,"%d %b %Y")
print(type(tye_date))

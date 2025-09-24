import datetime

mytime = datetime.time(13, 45, 30, 123456)
print(mytime)

print(type(mytime))

today = datetime.date.today()
print(today)

print(today.ctime())

from datetime import datetime
mydatetime = datetime(2023, 10, 5, 13, 45, 30, 123456)
print(mydatetime)


# Datetime Arithmetic
# Date

from datetime import date
date1 = date(2023, 10, 5)
date2 = date(2024, 1, 1)

delta = date2 - date1
print(delta)   
print(delta.days)


from datetime import datetime

datetime1 = datetime(2023, 10, 5, 13, 45, 30)
datetime2 = datetime(2024, 1, 1, 15, 30, 0)

delta = datetime2 - datetime1
print(delta)
print(delta.seconds)

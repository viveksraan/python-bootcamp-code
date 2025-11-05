'''
datetime module is very useful for accessing date and time related functionalities so you could use it to get the current date and time, or let's say you want to add date and time related date for some program you could add that
'''
import datetime

# You can pass arguments in this order ([hour, [min, [sec, [microsecond, [tzinfo]]]]) arguments are optional and never forget there's a dependency from i th arg i+1th
mytime = datetime.time(2, 20)
# You can access various attributes of datetime object to get desired results 
# 02:20:00
print(mytime)
# 2
print(mytime.hour)
# 20
print(mytime.minute)
print(mytime.microsecond)

# Similar to time date class could also be used to use date data
today = datetime.date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.ctime())

my_date_time = datetime.datetime(2021, 10, 3, 14, 20, 1)
print(my_date_time)

my_date_time = my_date_time.replace(year=2025)

another_date_time = datetime.datetime(2024, 1, 2, 2, 3)

#640 days, 12:17:01
print(my_date_time-another_date_time)
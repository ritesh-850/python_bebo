import datetime
# datetime.date #for working with dates
# datetime.time #for working with time
# datetime.datetime #for working with both
# datetime.timedelta #represet the duration
# datetime.tzinfo

current_datetime = datetime.datetime.now()
print("The current date and time",current_datetime)

#get current date only
date = datetime.date.today()
print("The current date is",date)

#Specific date and time
date = datetime.date(2025,12,6)
print(date)
time = datetime.time(11,20,25)
print(time)

#Extracting data and time components
now = datetime.datetime.now()
print("year",now.year)
print("month",now.month)
print("day",now.day)
print("hour",now.hour)
print("minute",now.minute)
print("seconds",now.second)

#Date arithmatic with timedelta
# add and subtract days
today = datetime.date.today()
future_date = today+datetime.timedelta(days = 10)
print("10days from today",future_date)

today = datetime.date.today()
future_date = today-datetime.timedelta(days = 10)
print("10days before today",future_date)

#
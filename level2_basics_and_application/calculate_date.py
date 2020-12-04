import datetime

year, month, date = (int(i) for i in input().split())
current_date = datetime.date(year, month, date)

date_delta = int(input())
new_date = current_date + datetime.timedelta(date_delta)
print(new_date.year, new_date.month, new_date.day)

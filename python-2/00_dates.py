#Fechas
from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
#Representacion unica de un tiempo
timestamp = now.timestamp()
print(timestamp)
#Creando un anio
year_2024 = datetime(2024,1,1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(year_2024)

from datetime import time
#time es un objeto que no tiene nada
current_time = time(hour=21,minute=5,second=6)
print(current_time.hour)
print(current_time.min)
print(current_time.second)

from datetime import date
current_date = date(2024,12,8)
print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.today())

current_date = date(current_date.year,current_date.month - 1,current_date.day)
print(current_date.month)

from datetime import timedelta
time_delta = timedelta(200,100,100,weeks= 10)
end_delta = timedelta(300,100,100,weeks= 13)

print(end_delta - time_delta)
print(end_delta + time_delta)
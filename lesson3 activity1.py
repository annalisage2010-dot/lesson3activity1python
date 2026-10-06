city= input("Enter your city name:")
temp= float(input("Enter the temperature in Celsius:"))
ab= float(input("Enter your marks:"))

if temp>35:
    print("Beware! It is super hot outside!")

if temp>25:
    print("Today will be a sunny day!")
else:
    print("Today will be quite chilly outside!")

if ab<100:
    print("congratulations! You have secured good marks!")
elif ab>90:
    print("You have scored good marks!")
elif ab>70:
    print("You have done well, keep it up!")
else:
    print("You need to work hard to improve your marks!")

import datetime
import calendar
now= datetime.datetime.now()
print("City:", city)
print("Time now:", now)
print(calendar.calendar(now.year))

    

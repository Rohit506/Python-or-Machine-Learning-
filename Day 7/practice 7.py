# calender package: work on calender package
import calendar
print(calendar.calendar(2020))
print("-"*100)
print(calendar.month(2020, 6))
print("-"*100)

print("IS 2008 Leap Year: ", calendar.isleap(2008))
print("Leap Year between 1900 and 2020 : ", calendar.leapdays(1900, 2020))
print("-"*100)

# Assignment : print all leap year between 1900 and 2020
x = range(1901, 2021)
yearlist = list(x)
newlist = list(filter(lambda x: x%4==0, yearlist))
print("Leap year list between 1900 and 2020: ",newlist)
print(len(newlist))
print("-"*100)

from datetime import datetime
print(datetime.now())
print("-"*100)

x = datetime.now()
print("Year :", x.year)
print("Month : ", x.month)
print("day :", x.day)
print("date : ", x.date())
print("-"*100)

# WAP to find age of any student, Birthdate is input by user
from datetime import datetime
x = datetime.now()
a = int(input("Enter your Birth year :"))
b = int(input("Enter your Birth Month :"))
c = int(input("Enter your Birth Day(Date) :"))
print("Your Current Age :",(x.year-a),"year ",(x.month-b),"Month ", (x.day-c), "days")
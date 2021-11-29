"""Module that allows to create programs that deal with date and time as the name implies."""
#Call the module as dt for simplicity
import datetime as dt

print(dt.datetime.now())                      #To print the date and time right now
print(dt.datetime.now().date())      #To print only the date

print(dir(dt))                       #To print what is inside the Module
print(help(dt.date))                 #To get help with the specified call
Dday = dt.date("year, month, day")   #to specify a date
print(Dday.year)                     #To print only the year
print(Dday.month)                    #To print month only, same can be done with day
"""time delta class is used to add or subtract days"""
#let's add 100 days to tomorrow:
today = dt.date(2021, 11, 29)        #Specify date
in_100_days = dt.timedelta(100)      #use time delta(#of days)to get future date
a_100_days_ago = dt.timedelta(-100)  # a negative number will decrease the date
print(today + a_100_days_ago)
print(today + in_100_days)
"""Format codes"""
"""
%b: Returns the first three characters of the month name.
%d: Returns day of the month, from 1 to 31.
%Y: Returns the year in four-digit format. 
%H: Returns the hour. 
%M: Returns the minute, from 00 to 59..
%S: Returns the second, from 00 to 59.
%a: Returns the first three characters
%A: Returns the full name of the weekday, e.g. Wednesday.
%B: Returns the full name of the month, e.g. September.
%w: Returns the weekday as a number, from 0 to 6, with Sunday being 0.
%m: Returns the month as a number, from 01 to 12.
%p: Returns AM/PM for time.
%y: Returns the year in two-digit format, that is, without the century. For example, "18" instead of "2018".
%f: Returns microsecond from 000000 to 999999.
%Z: Returns the timezone.
%z: Returns UTC offset.
%j: Returns the number of the day in the year, from 001 to 366.
%W: Returns the week number of the year, from 00 to 53, with Monday being counted as the first day of the week.
%U: Returns the week number of the year, from 00 to 53, with Sunday counted as the first day of each week.
%c: Returns the local date and time version.
%x: Returns the local version of date.
%X: Returns the local version of time.
"""
#Using format codes
my1styr  = dt.date(2017, 9, 1)
message = "My first year of university {:%A, %B %d, %Y}."
print(message.format(my1styr))
#Or
print(my1styr.strftime("%A, %B %d, %Y"))     #strftime is to turn date and time string 

#Access date, time seperately 
dob = dt.date(2013, 3, 23)
tob = dt.time(11, 47, 26)
birthdt = dt.datetime(2013, 3, 23, 11, 47, 26)

print(dob)      #Will only print date of birthdt
print(tob)      #Will print time of birth
print(birthdt)  #Will print all

print(tob.hour) #Will print hour only
print(tob.minute) #Will print minute only
print(tob.second) #Will print second only
""" same can be done with dob, where : print(dob.day) will print the day only etc"""

#Strptime class takes 2 args (str that can be converted to datetime and format code )
#returns equivalent datetime object of chosen format code, example: ;
Date_instr = "20 Aug, 21"
Dobject =  dt.datetime.strptime(Date_instr, "%d %B, %Y") #Will print 2021-08-20 00:00:00 


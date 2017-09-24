"""
Written by: C. West
Date: 09/24/17
Exercise: 3.33 (problem taken from C++ book)
"""

# User input
year = int(input("Enter year (e.g. 2012): "))
month = int(input("Enter month (e.g. 1-12): "))
day = int(input("Enter the day of the month (e.g. 1-31): "))
century = year//100
year %= 100

if month == 1:
    month = 13
    year -= 1
elif month == 2:
    month = 14
    year -= 1

dayNum = (day + (26*(month+1)//10) + year + (year//4) + (century//4) + (5 * century)) % 7
dayOfweek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("Day of the week is", dayOfweek[dayNum])

#print(dayOfweek)
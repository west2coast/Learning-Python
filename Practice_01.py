"""
Written by: C. West
Date: 09/23/17
Exercise: 1.11 (problem taken from C++ book)
"""

currentPop = 325365189
minuteSeconds = 60
hourSeconds = 60 * minuteSeconds
daySeconds = 24 * hourSeconds
yearSeconds = 365 * daySeconds
birth = (yearSeconds//7) * 1 # 1 birth every 7 seconds
death = (yearSeconds//13) * -1 # 1 death every 13 seconds
immigrant = (yearSeconds//45) * 1 # 1 new immigrant every 45 seconds
print("Current world population is", currentPop)
future = currentPop + birth + immigrant - death
count = 1
while (count < 6):
    future = currentPop + birth + immigrant - death
    currentPop = future
    print("Future population for year", count, "is", future)
    count = count + 1

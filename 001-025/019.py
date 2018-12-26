# 0 - 6 : Monday - Sunday
# 0 - 11 : January - December
sundays = 0
day = 365     # one year after 1 Jan 1900
for year in range(1901, 2001):
    for month in range(12):
        sundays += day%7==6
        if month == 1:
            if year%4==0 and (year%100!=0 or year%400==0):
                day += 29
            else:
                day += 28
        elif month in [3, 5, 8, 10]:
            day += 30
        else:
            day += 31
print(sundays)

import calendar

print(calendar.weekheader(5))
print()

print(calendar.firstweekday())
print()

print(calendar.month(2021,7))

print(calendar.calendar(2021))

day_of_the_week=calendar.weekday(2021,7,10)
print(day_of_the_week)

is_leap=calendar.isleap(2021)
print(is_leap)

how_many_leap_days=calendar.leapdays(2020,2070)
print(how_many_leap_days)
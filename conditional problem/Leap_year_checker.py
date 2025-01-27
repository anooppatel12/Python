# Determine if a year is a leap year.(leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "Is  a LEap Year")
else:
    print(year, "is NOt Leap year")

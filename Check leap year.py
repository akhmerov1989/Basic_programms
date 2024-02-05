year = int(input("Enter a year: "))

# divided by 100 means centuary year (ending with 00)
# century year divided by 400 is leap year
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))

# not divided by 100 means not a century year
# century year by 400 i leap year
elif (year % 4 == 0) and (year % 100 !=0):
    print("{0} is a leap year".format(year))

# if not divided by both 400 (century year) and 4 (not century year)
# year is mot leap year
else:
    print("{0} is mot a leap year".format(year))


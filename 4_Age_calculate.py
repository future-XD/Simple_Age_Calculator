# importing current time and date

import datetime
x = datetime.datetime.now()

# assigning variables to date , year and month

c_month = int(x.month)
c_date = int(x.day)
c_year = int(x.year)

# asking DOB in input

DOB = input("Please enter your DOB in 'DDMMYYYY' format : ")

# assigning variables to different parts of DOB

birth_date = int(DOB[0:2])
birth_month = int(DOB[2:4])
birth_year = int(DOB[4:])

# calculating age in years and months
# and revaulting age in years if correction needed

agey = int(c_year - birth_year)
if c_month > birth_month:
    agem = int(c_month-birth_month)
else:
    agey -= 1
    agem = int(12-(birth_month-c_month))

# calculating age in days and revaluating age in months as required

if c_date > birth_date:
    aged = c_date-birth_date
else:
    agem -= 1
    if c_month in {int(1), int(3), int(5), int(7), int(8), int(10), int(12)}:
        aged = int(31-(birth_date-c_date))
    if c_month == int(2):
        aged = int(28-(birth_date-c_date))
    if c_month in {int(4), int(6), int(9), int(11)}:
        aged = int(30-(birth_date-c_date))

# FINAL printing calculated age

print("Your Age is", agey, "year(s)", agem, "month(s)", aged, "day(s)")

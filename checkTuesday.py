# program to check if the day of the week is tuesday

import datetime

print("Check if it's Tuesday!")

today = datetime.datetime.today()
dayOfWeek = today.weekday()

if dayOfWeek == 1:
    print("It's Tuesday!")
else:
    print("It's not Tuesday")
    
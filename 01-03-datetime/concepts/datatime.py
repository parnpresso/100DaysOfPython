from datetime import date
from datetime import datetime


datetime.today()

today = datetime.today()
type(today)

todaydate = date.today()
type(todaydate)

todaydate.month
todaydate.day
todaydate.year

christmas = date(2018, 12, 25)

christmas - todaydate

(christmas - todaydate).days

if christmas is not todaydate:
    print("Sorry there are still " + str((christmas - todaydate).days) + " until Christmas!")
else:
    print("Yay it's Chirstmas!")

# Parsing dates from logs

In this bite we will look at this small server log finding the first and last Shutdown initiated events and calculate the time between the two events.

In order to do this you need to extract the timestamps from the log entries and convert them to datetime objects. You can then use datetime.timedelta to calculate time differences between them. Check out the docstrings and the TESTS for more info.

Good luck and have fun!

Ref: https://codechalleng.es/bites/7

----------

# Learn Today
- List comprehension - https://blog.teamtreehouse.com/python-single-line-loops
- `min()` and `max()` in array

"""
########################################################################
A lot of times you want to keep track of when something happened. We can do so in Python using datetime.

Here we’ll use datetime to print the date and time in a nice format.
#######################################################################
Getting the Current Date and Time

We can use a function called datetime.now() to retrieve the current date and time.

from datetime import datetime

print datetime.now()

The first line imports the datetime library so that we can use it.

The second line will print out the current date and time.
######################################################################

"""
from datetime import datetime


now = datetime.now()

print(now)



"""
Hot Date

What if we want to print today’s date in the following format? mm/dd/yyyy. Let’s use string substitution again!

from datetime import datetime
now = datetime.now()

print '%02d-%02d-%04d' % (now.month, now.day, now.year)
# will print the current date as mm-dd-yyyy

Remember that the standalone % operator after the string will fill the %02d and %04d placeholders in the string on the left with the numbers and strings in the parentheses on the right.

%02d pads the month and day numbers with zeros to two places, and %04d pads the year to four places. This is one way dates are commonly displayed.

#EXERCISE

Print the current date in the form of mm/dd/yyyy.

Change the string used above so that it uses a / character in between the %02d and %04d placeholders instead of a - character.

"""


from datetime import datetime
now = datetime.now()

print("%s/%02d/%04d" % (now.month,now.day,now.year))










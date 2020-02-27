"""
Pretty Time

Nice work! Let’s do the same for the hour, minute, and second.

from datetime import datetime
now = datetime.now()

print now.hour
print now.minute
print now.second

In the above example, we just printed the current hour, then the current minute, then the current second.

We can again use the variable now to print the time.

"""



from datetime import datetime
now = datetime.now()

print('%02d:%02d:%02d' % (now.hour,now.minute, now.second))

print('%s/%02d/%04d %02d:%02d:%02d' % (now.hour,now.minute, now.second, now.month,now.day,now.year))

"""
String Formatting with %, Part 1

When you want to print a variable with a string, there is a better method than concatenating strings together.

name = "Mike"
print "Hello %s" % (name)

The % operator after the string is used to combine a string with variables. The % operator will replace the %s in the string with the string variable that comes after it.

If you’d like to print a variable that is an integer, you can “pad” it with zeros using %02d. The 0 means “pad with zeros”, the 2 means to pad to 2 characters wide, and the d means the number is a signed integer (can be positive or negative).

day = 6
print "03 - %s - 2019" %  (day)
# 03 - 6 - 2019
print "03 - %02d - 2019" % (day)
# 03 - 06 - 2019


String Formatting with %, Part 2

Remember, we used the % operator to replace the %s placeholders with the variables in parentheses.

name = "Mike"
print "Hello %s" % (name)

You need the same number of %s terms in a string as the number of variables in parentheses:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"





"""

string_1 = "Camelot"
string_2 = "place"
name = input("What is your name? ")
quest = input("What is your quest? ")
color = input("What is your favorite color? ")


print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

print("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))








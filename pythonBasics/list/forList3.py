#day at the supermarket
"""
BeFOR We Begin

Before we begin our exercise, we should go over the Python for loop one more time. For now, we are only going to go over the for loop in terms of how it relates to lists and dictionaries. We’ll explain more cool for loop uses in later courses.

for loops allow us to iterate through all of the elements in a list from the left-most (or zeroth element) to the right-most element. A sample loop would be structured as follows:

a = ["List", "of", "some", "sort"]
for x in a: 
  # Do something for every x

This loop will run all of the code in the indented block under the for x in a: statement. The item in the list that is currently being evaluated will be x. So running the following:

for item in [1, 3, 21]: 
  print item

would print 1, then 3, and then 21. The variable between for and in can be set to any variable name (currently item), but you should be careful to avoid using the word list as a variable, since that’s a reserved word (that is, it means something special) in the Python language.

1. Use a for loop to print out all of the elements in the list names.

This is KEY!

You can also use a for loop on a dictionary to loop through its keys with the following:

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
  print d[key]  # prints "bar" 

Note that dictionaries are unordered, meaning that any time you loop through a dictionary, you will go through every key, but you are not guaranteed to get them in any particular order.

Use a for loop to go through the webster dictionary and print out all of the definitions.


"""

names = ["Adam","Alex","Mariah","Martine","Columbus"]

webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

for i in webster:
	print(webster[i])


for i in names:
	print(i)














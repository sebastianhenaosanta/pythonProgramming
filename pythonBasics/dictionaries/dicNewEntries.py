"""
New Entries

Like Lists, Dictionaries are mutable. This means they can be changed after they are created. One advantage of this is that we can add new key/value pairs to the dictionary after it is created like so:

dict_name[new_key] = new_value

An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.

The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, even if the value is a list. (That’s right: you can put lists inside dictionaries!)


Add at least three more key-value pairs to the menu variable, with the dish name (as a "string") for the key and the price (a float or integer) as the value. Here’s an example:

py menu['Spam'] = 2.50
"""

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!

menu['toySoup'] = 15.5
menu['babyBeef'] = 12.9
menu['pasta'] = 63

#
print("There are " + str(len(menu)) + " items on the menu.")
#keys
print(menu)



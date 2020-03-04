"""
More with 'for'

If your list is a jumbled mess, you may need to sort() it.

animals = ["cat", "ant", "bat"]
animals.sort()

for animal in animals:
  print animal

    First, we create a list called animals with three strings. The strings are not in alphabetical order.
    Then, we sort animals into alphabetical order. Note that .sort() modifies the list rather than returning a new list.
    Then, for each item in animals, we print that item out as "ant", "bat", "cat" on their own line each.


Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.

Then sort square_list!


"""


start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for x in start_list:
	square_list.append(x**2)
	

print(square_list.sort())


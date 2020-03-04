"""
List Slicing

Sometimes, you only want to access a portion of a list. Consider the following code:

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice
print letters

What is this code doing?

First, we create a list called letters.

Then, we take a subsection of the list and store it in the slice list. We do this by defining the indices we want to include after the name of the list: letters[1:3]. In Python, when we specify a portion of a list in this manner, we include the element with the first index, 1, but we exclude the element with the second index, 3.

Next, we print out slice, which will print ['b','c']. Remember, in Python indices always start at 0, so the 1 element is actually b.

Finally, we print out ['a', 'b', 'c', 'd', 'e'], notice that we did not modify the original letters list.

"""


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

# The first and second items (index zero and one)
first = suitcase[0:2]

# Third and fourth items (index two and three)
middle = suitcase[2:4] 

# The last two items (index four and five)
last =  suitcase[4:]







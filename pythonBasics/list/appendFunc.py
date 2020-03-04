"""
Late Arrivals & List Length

A list doesn’t have to have a fixed length. You can add items to the end of a list any time you like!

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters

    In the above example, we first create a list called letters.
    Then, we add the string 'd' to the end of the letters list.
    Next, we print out 4, the length of the letters list.
    Finally, we print out ['a', 'b', 'c', 'd'].
"""
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shoes")
suitcase.append("t-shirt")
suitcase.append("bathing suit")

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)


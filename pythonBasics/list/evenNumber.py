"""
Control Flow and Looping

The blocks of code in a for loop can be as big or as small as they need to be.

While looping, you may want to perform different actions depending on the particular item in the list.

numbers = [1, 3, 4, 7]
for number in numbers: 
  if number > 6:
    print number
print "We printed 7."

    In the above example, we create a list with 4 numbers in it.
    Then we loop through the numbers list and store each item in the list in the variable number.
    On each loop, if number is greater than 6, we print it out. So, we print 7.
    Finally, we print out a sentence.

Make sure to keep track of your indentation or you may get confused!

Like step 2 above, loop through each item in the list called a.

Like step 3 above, if the number is even, print it out. You can test if the item % 2 == 0 to help you out.


"""

a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for i in a:
	if i % 2 == 0:
		print(i)







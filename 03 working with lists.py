# LOOPING THROUGH AN ENTIRE LIST #

# magicians = ['alice','david','carolina']   We begin by defining a list, just as we did in chapter 2. Then we define a for loop. This line
# for magician in magicians:    tells Python to pull a name form the list magicians, and associate it with variable magician. Next, we tell
#     print(magician) Python to print the name that's just been assigned to magician. Python then repeats these last two lines, once for each
# name in the list. It might help to read this code as For every magician in the list of magicians, print the magician's name. The output is a
# simple printout of each name in the list:

 # A CLOSER LOOK AT LOOPING #
 #  For example, in a simple loop like we used in magicians.py, Python initially reads the firt line of the loop:
 # for magician in magicians:
 # this lines tells Python to retrieve the first value from the list magicians and associate it with the variable magician, This first value
 # is 'alice'. Python then reads the next line.
#  print(magician)
# Python prints the current value of magician, which is still 'alice'. Because the list contains more values, Python returns to the first line
# of the loop
# for magician in magicians:
# Python retrieves the next name in the list, 'david' and associates that value with the variable magician. Python then executes the line.
# print(magician)
# Python prints the current value of magician again, which is now 'david' Python repeats the entire loop once more with the last value in the
# list, 'carolina'. Because no more values are in the list, python moves on to the next line in the program. In this case nothing comes after the
# for loop, so the program ends. When you're using for the firt time, keep in mind that the set of steps is repeated once for each item in the list,
# If you have a million items in your list, python repeats these steps a million times-and usually very quickly. Also keep in mind when writing
# your own for loops that you can choose any name you want for the temporary variable that will be associated with each value in the list.
# However, it's helpful to choose a meaningful name that represents a single item form the list. For example, here's good way to start a for loop
# for a list of cats, a list of dogs, and a general list of items.
# for cat in cats:
# for dog in dogs:
# for item in list_of_items:
# These naming conventions can help you follow the action being done on each item within a for loop, Using singular and plural names can help you
# identify whether a section of code is working with single element from the list or the entire list.

# DOING MORE WORK WITHIN A FOR LOOOP #
# megicians = ['alice','david','carolina']
# for megician in megicians:
#     print(f'{megician.title()}, that was a great trick!')
#     print(f"I can't wait to see your next trick, {megician.title()}.\n")
# print('Thank you, everyone. That was great magic show!') The first two calls to print() are repeated once for each magician in the list,
# as you saw earlier. However, because the last line is not indented, it's printed only once. indented means space. if you accidently indent last
# line that code will be repeated once for each item in the list.

# AVOIDING INDENTATION ERRORS #
# Python uses indentation to determine how a line, or group of lines, is related to the rest of the program. In the previous examples, the lines
# that printed message to individual magiicians were part of the for loop because they were indented. people sometimes indent lines of code that
# don't need to be indented or forget to indent lines that need to be indented.
# FORGETTING TO INDENT #
# Always indent the line after the for statement in a loop. if you forget python will remind you.
# magicians = ['alice','david','carolina'] The call to print() should be indented, but it's not.
# for magician in magicians:
# print(magician)

# FORGETTING TO INDENT ADDITIONAL LINES #
# magicians = ['alice','david','carolina']
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick!')
# print(f"I can't wait to see your next trick {magician.title()}.\n")
# The second call to print() is supposed to be indented, but because Python finds at least one indented line after the for statement, it doesn't
# report an error. As a result, the first print() call is executed once for each name in the list because it is indented. The second print() call
# is not indented, so it is executed only once after the loop has finished running. Because the final value associated with magician is 'carolina',
# she is the only one who receives the 'looking forward to the next trick' message.

#INDENTING UNNECESSRILY #
# if you accidentally indent a line that doesn't need to be indented, Python informs you about the unexpected indent.
# message = 'Hello python world!'     We don't need to indent the print() call, because it is not part of a loop.
#     print(message)
# you can avoid unexpected indentation errors by indenting only when you have a specific reason to do so. In the programs you're wirting at this
# point, the only lines you should indent are the actions you want to repeat for each item in a for loop.

# FORGETTING THE COLON #
# The colon at the end of a for statement tells python to interpret the next line as the start of a loop. if you accidentally forget the colon
# you'll get a syntax error because Python doesn't know exactly what you're trying to do.

# MAKING NUMERICAL LIST # # USING THE range() FUNCTON #
# you’ll need to keep track of the positions of each character in a game, and you might want to keep track of a player’s high scores as well.
#  Lists are ideal for storing sets of numbers

## USING THE RANGE() FUNCTION##

# for value in range(1,5):
#  print(value)
#  range() prints only the numbers 1 through 4. This is another result of the off-by-one behavior you’ll see often in programming languages.
# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide.
# Because it stops at that second value, the output never contains the end value, which would have been 5 in this case.  To print the numbers
# from 1 to 5, you would use range(1,6): you can also pass range only one argument for example range(6): it would return the numbers from 0 to 5.

# USING RANGE() TO MAKE A LIST OF NUMBERS #
# If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.
# numbers = list(range(1,6))
# print(numbers)
# even_numbers = list(range(2,11,2))
# print(even_numbers)
# In this example, the range() function starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or
# passes the end value, 11, and produces this result.
# You can create almost any set of numbers you want to using the range() function. For example, consider how you might make a list of the first 10
# square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents.
# squares = []    (observe squares is plural form)
# for value in range(1,11):
#     square = value ** 2   (observe square is singular form)
#     squares.append(square)
# print(squares)
# We start with an empty list called squares at u. At v, we tell Python to loop through each value from 1 to 10 using the range() function. Inside
# the loop, the current value is raised to the second power and stored in the variable square at w. At x, each new value of square is appended to
# the list squares. Finally, when the loop has finished running, the list of squares is printed at.
# To write this code more concisely, omit the temporary variable square and append each new value directly to the list:
# squares = []
# for value in range(1,11):
#     squares.append(value**2)
# print(squares)

# SIMPLE STATISTICS WITH A LIST OF NUMBERS #
# >>> digits = [1,2,3,4,5,6,7,8,9,0]
# >>> min(digits)
# 0
# >>> max(digits)
# 9
# >>> sum(digits)
# 45

# LIST COMPREHENSIONS #
# The approach described earlier for generating the list squares consisted of using three or four lines of code. A list comprehension allows you to
# generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line,
# and automatically appends each new element.
# squares = [value**2 for value in range(1,11)]
# print(squares)
# To use this syntax, begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for
# the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write
# a for loop to generate the numbers you want to feed into the expression, and close the square brackets. The for loop in this example is for value
# in range(1,11), which feeds the values 1 through 10 into the expression value**2. Notice that no colon is used at the end of the for statement.

# WORKING WITH A PART OF LIST #
# SLICING A LIST # A SPECIFIC GROUP OF ITEMS IN A LIST CALLED SLICE #
# players = ['pradeep','rakesh','rajesh','sai kumar','nelopher']
# print(players[0:3])
# print(players[1:4])
# print(players[:4])
# print(players[2:])
# print(players[-3:])
# you can include a third value in the brackets indicating a slice. if a third value is included this tells python how many items
# to skip between items in the specified range
# list[start:end:step]
# start: The starting index of the slice (inclusive).
# end: The ending index of the slice (exclusive).
# step: The step size, indicating how many items to skip between items in the specified range. If not specified, the default value is 1.
# players = ['pradeep', 'rakesh', 'rajesh', 'sai kumar', 'nelopher']
# If you want to slice the list with a step size of 2, starting from index 0 and going up to index 4 (exclusive), you can use:
# print(players[0:4:2])
# This will print every second element from indices 0 to 3 (inclusive),  ( IMP every 2nd value skip in a list)
# Here, 'pradeep' is at index 0, 'rakesh' is at index 1, 'rajesh' is at index 2, and 'sai kumar' is at index 3. So, it skips
# 'rakesh' and 'sai kumar' and includes 'pradeep' and 'rajesh' in the sliced list.
# You can use a slice in a for loop if you want to loop through a subset of the elements in a list.
# players = ['rajesh','sai kumar','ranil','pradeep kumar','nelopher','angle']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player)
# Slices are very useful in a number of situations. For instance, when you’re creating a game, you could add a player’s final score to a list
# every time that player finishes playing. You could then get a player’s top three scores by sorting the list in decreasing order and taking a
# slice that includes just the first three scores.

# COPYING A LIST #
# Often, you’ll want to start with an existing list and make an entirely new list
# To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]). This tells
# Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# TO PROVE THAT WE ACTUALLY HAVE TWO SEPARATE LISTS #

# my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
#
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
#
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

 # If we had simply set friend_foods equal to my_foods, we would not produce two separate lists. For example,
# here’s what happens when you try to copy a list without using a slice:

# my_foods = ['pizza', 'falafel', 'carrot cake']
# This doesn't work:
# friend_foods = my_foods
# my_foods.append('cannoli')
# friend_foods.append('ice cream')
# print("My favorite foods are:")
# print(my_foods)
# print("\nMy friend's favorite foods are:")
# print(friend_foods)

# Instead of assigning a copy of my_foods to friend_foods, we set friend_foods equal to my_foods. This syntax actually tells Python to associate
# the new variable friend_foods with the list that is already associated with my_foods, so now both variables point to the same list. As a result,
# when we add 'cannoli' to my_foods, it will also appear in friend_foods. Likewise 'ice cream' will appear
# in both lists, even though it appears to be added only to friend_foods.

# TUPLES #
# sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot
# change as immutable, and an immutable list is called a tuple. A tuple looks just like a list, except you use parentheses instead of square
# brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.
# For example, if we have a rectangle that should always be a certain size, we
# can ensure that its size doesn’t change by putting the dimensions into a tuple:

# dimensions = (200,50)
# print(dimensions[0])
# print(dimensions[1])

# Let’s see what happens if we try to change one of the items in the tuple dimensions:
# dimensions = (200,50)
# dimensions[0] = 250
# print(dimensions)
# This code tries to change the value of the first dimension, but Python returns a type error.

# Tuples are technically defined by the presence of a comma; the parentheses make them
# look neater and more readable. If you want to define a tuple with one element, you
# need to include a trailing comma:
#  my_t = (3,)
# It doesn’t often make sense to build a tuple with one element, but this can happen
# when tuples are generated automatically.
# Including a trailing comma when defining a tuple with a single element ensures that Python interprets it as a tuple rather than just a single value
# enclosed in parentheses. This distinction is important for consistency in code and to avoid unexpected behavior, especially when
# tuples are generated automatically or in certain function calls where a single-element tuple might be required.

# LOOPING THROUGH ALL VALUES IN A TUPLE #
# You can loop over all the values in a tuple using a for loop, just as you did with a list:
# dimensions = (200, 50)
# for dimension in dimensions:
#     print(dimension)

# WRITING OVER A TUPLE #
# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple. For example, if we wanted to change
# the dimensions of this rectangle, we could redefine the entire tuple:
# dimensions = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)
# Python doesn’t raise any errors this time, because reassigning a variable is valid:
# When compared with lists, tuples are simple data structures. Use them
# when you want to store a set of values that should not be changed throughout the life of a program.

# STYLING YOUR CODE #
# THE STYLE GUIDE #
# When someone wants to make a change to the Python language, they write a Python Enhancement Proposal (PEP). One of the oldest PEPs is PEP 8, which
# instructs Python programmers on how to style their code. PEP 8 is fairly lengthy, but much of it relates to more complex coding structures than what
# you’ve seen so far.
 # INDENTATION #
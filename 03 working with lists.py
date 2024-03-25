# LOOPING THORUGH AN ENTIRE LIST #

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
#     print(f"I can't wait to see your next tirck, {megician.title()}.\n")
# print('Thank you, everyone. That was great magic show!') The first two calls to print() are repeated once for each magician in the list,
# as you saw earlier. However, because the last line is not indented, it's printed only once. indented means space. if you accidently indent last
# line that code will be repeated once for each item in the list.

# AVODING INDENTATION ERRORS #
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
# if you acciddently indent a line that doesn't need to be indented, Python informs you about the unexpected indent.
# message = 'Hello python world!'     We don't need to indent the print() call, because it is not part of a loop.
#     print(message)
# you can avoid unexpected indentation errors by indenting only when you have a specific reason to do so. In the programs you're wirting at this
# point, the only lines you should indent are the actions you want to repeat for each item in a for loop.

# FORGETTING THE COLON #
# The colon at the end of a for statement tells python to interpret the next line as the start of a loop. if you accidentally forget the colon
# you'll get a syntax error because Python doesn't know exactly what you're trying to do.

# MAKING NUMARICAL LIST # # USING THE range() FUNCTON #
# you can use the range()

# A SIMPLE DICTIONARIES #
# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])

# WORKING WITH DICTIONARIES #

# A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value
# associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. In fact, you can use any object
# that you can create in Python as a value in a dictionary. In Python, a dictionary is wrapped in braces ({}) with a series of key-value
# pairs inside the braces. A key-value pair is a set of values associated with each other. When you provide a key, Python returns the value
# associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated
# by commas. You can store as many key-value pairs as you want in a dictionary.

# ACCESSING VALUE IN A DICTIONARY #
# To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets.

# alien_0 = {'color':'green','points':5}
# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color':'green','points':5}
# new_points = alien_0['points']
# print(f'You just earned {new_points} points !')

# ADDING NEW KEY-VALUE PAIRS #
# Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. To add a new key-value pair,
# you would give the name of the dictionary followed by the new key in square brackets, along with the new value.
# Let’s add two new pieces of information to the alien_0 dictionary: the alien’s x- and y-coordinates, which will help us display
# the alien at a particular position on the screen. Let’s place the alien on the left edge of the screen, 25 pixels down from the top.
# Because screen coordinates usually start at the upper-left corner of the screen, we’ll place the alien on the left edge of the screen by
# setting the x-coordinate to 0 and 25 pixels from the top by setting its y-coordinate to positive 25, as shown here:
# alien_0 = {'color':'green','points':5}
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# Dictionaries retain the order in which they were defined. When you print a dictionary or loop through its elements, you will see
# the elements in the same order they were added to the dictionary.

# STARTING WITH AN EMPTY DICTIONARY #
# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)

# MODIFYING VALUES IN A DICTIONARY #
# alien_0 = {'color':'green','points':5}
# print(f'The alien is {alien_0}.')
# alien_0['color'] = 'yellow'
# print(f'The alien is now {alien_0}.')

# MORE INTERESTING EXAMPLE #
# alien_0 = {'x_position':1, 'y_position':25, 'speed':'medium'}
# print(f'Original position: {alien_0['x_position]}')
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.

# if alien_0['speed'] == 'slow':
#     x_increment = 1       # x_increment is a variable and 1 is value to set that variable.
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     This must be a fast alien.
#     x_increment = 3
    # The new position is the old position plus the increment.
# alien_0['final_position'] = alien_0['x_position'] + x_increment
# Here, 'final_position' is the new key being added to the alien_0 dictionary.
# The value assigned to this key is the result of the expression alien_0['x_position'] + x_increment.
# print(f'New position: {alien_0['final_position']}')

# alien_0['x_position'] is 1, and x_increment is 2, so the value assigned to 'z_position' is 1 + 2, which is 3.

# We start by defining an alien with an initial x position and y position, and a speed of 'medium'. We’ve omitted the color and point values
# for the sake of simplicity, but this example would work the same way if you included those key-value pairs as well. We also print the original
# value of x_position to see how far the alien moves to the right. An if-elif-else chain determines how far the alien should move to
# the right, and assigns this value to the variable x_increment . If the alien’s speed is 'slow', it moves one unit to the right; if
# the speed is 'medium', it moves two units to the right; and if it’s 'fast', it moves three units to the right. Once the increment
# has been calculated, it’s added to the value of final_position , and the result is stored in the dictionary’s final_position.
# Because this is a medium-speed alien, its position shifts two units to the right:
# This technique is pretty cool: by changing one value in the alien’s dictionary, you can change the overall behavior of the alien.
# For example, to turn this medium-speed alien into a fast alien, you would add this line:

# REMOVING KEY-VALUE PAIRS #

# All del needs is the name of the dictionary and the key that you want to remove.

# alien_0 = {'color':'green','points':5}
# print(alien_0)
# del alien_0['points']
# print(alien_0)

# NOTE Be aware that the deleted key-value pair is removed permanently.

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python',
# }

# language = favorite_languages['sarah']
# print(f" Sarah's favorite language is {language}")
# print('favorite_languages,['sarah']')

# When you know you’ll need more than one line to define a dictionary, press ENTER after the opening brace. Then indent the
# next line one level (four spaces) and write the first key-value pair, followed by a comma. From this point forward when you press
# ENTER, your text editor should automatically indent all subsequent key-value pairs to match the first key-value pair. Once you’ve finished
# defining the dictionary, add a closing brace on a new line after the last key-value pair, and indent it one level so it
# aligns with the keys in the dictionary. It’s good practice to include a comma after the last key-value pair as well,
# so you’re ready to add a new key-value pair on the next line.

# USING GET() TO ACCESS VALUES #

# Using keys in square brackets to retrieve the value you’re interested in from a dictionary might cause one potential problem:
# if the key you ask for doesn’t exist, you’ll get an error.

# alien_0 = {'color':'green', 'speed':'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# point_value = alien_0.get('speed', 'No point value assigned.')   #Replace speed you will know what exact get does #
# print(point_value)

# The get() method is used on the alien_0 dictionary to retrieve the value associated with the key 'points'. However,'points' is not
# a key in the alien_0 dictionary.
# 'points' is the key we want to retrieve the value for. 'No point value assigned.' is the default value returned if 'points' is not found
# in the dictionary. Since 'points' is not a key in alien_0, the get() method returns the default value 'No point value assigned.'.

# The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key
# doesn’t exist: If the key 'points' exists in the dictionary, you’ll get the corresponding value. If it doesn’t, you get the default
# value. In this case, points doesn’t exist, and we get a clean message instead of an error: No point value assigned.
# If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation
# If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special
# value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value.
# point_value = alien_0.get('points')

# LOOPING THROUGH DICTIONARY #
# You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.
# LOOPING THROUGH ALL KEY-VALUE PAIRS #

# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
# }
#
# for key, value in user_0.items(): (The .items() method returns a view object that contains the key-value pairs of the dictionary as tuples.)
    # print(f'\nKey: {key}')
    # print(f'Value: {value}')

# in for loop key and values are variable, To write a for loop for a dictionary, you create names for the two variables that will hold
# the key and value in each key-value pair. You can choose any names you want for these two variables. for ex: for k, v in user_0.items()
# The second half of the for statement includes the name of the dictionary followed by the method items(), which returns a sequence
# of key-value pairs. The for loop then assigns each of these pairs to the two variables provided.

# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil' : 'python',
# }
#
# for name, language in favorite_languages.items():   (in this case name is variable holds keys and language is also variable holds values)
#     print(f"{name}'s favorite language is {language}")

# LOOPING THROUGH ALL THE KEYS IN A DICTIONARY #
# The keys() method is useful when you don’t need to work with all of the values in a dictionary

# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil' : 'python',
# }
#
# for name in favorite_languages.keys():
#     print(name)

# IF YOU GIVE LIKE THIS YOU WILL GET A ERROR, IN THIS CASE YOU HAVE TO USE .ITEMS() FOR BOTH KEYS AND VALUES #
# for name, value in favorite_languages.keys():
#     print(name)

# Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly
# the same output if you wrote:
# for name in favorite_languages:
# rather than:
# for name in favorite_languages.keys():

#in this case .keys() method is not mandetory to use you can omit it You can choose to use the keys() method explicitly if it makes
# your code easier to read, or you can omit it if you wish. You can access the value associated with any key you care about inside
# the loop, by using the current key.

# favorite_languages = {
#     'jen': 'python',
#     'sarah':'c',
#     'edward': 'rust',
#     'phil': 'python',
# }
# friends = ['phil','sarah']
# for name in favorite_languages.keys():
#     print(f'Hi {name.title()}.')
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f'\t{name.title()}, I see you love {language}! ')

# in this code last print call how it have printed values like c and python because we gave only keys. answer is.
# Here's how the program works in detail:
#
# First Iteration:
#
# name is 'jen'.
# print(f'Hi {name.title()}.') prints Hi Jen.
# 'jen' is not in friends, so the if block is skipped.
# Second Iteration:
#
# name is 'sarah'.
# print(f'Hi {name.title()}.') prints Hi Sarah.
# 'sarah' is in friends, so the if block is executed.
# language = favorite_languages['sarah'].title() sets language to 'C'.
# print(f'\t{name.title()}, I see you love {language}!') prints Sarah, I see you love C!.

# First, we make a list of friends that we want to print a message to. Inside the loop, we print each person’s name. Then
# we check whether the name we’re working with is in the list friends. If it is, we determine the person’s favorite language
# using the name of the dictionary and the  current value of name as the key. We then print a special greeting, including a reference to
# their language of choice. You can also use the keys() method to find out if a particular person was polled.

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# LOOPING THROUGH A DICTIONARY'S KEYS IN A PARTICULAR ORDER #
# Looping through a dictionary returns the items in the same order they were inserted. Sometimes, though, you’ll want to loop through
# a dictionary in a different order.

# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward':'rust',
#     'phil':'python',
# }
# for name in sorted(favorite_languages.keys()):
#     print(f'{name.title()}, thank you for taking the poll.')

# LOOPING THROUGH ALL VALUES IN A DICTIONARY #
# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward':'rust',
#     'phil':'python',
# }
# print('The following languages have been mentioned:')
# for language in favorite_languages.values():
#     print(language.title())

# This approach pulls all the values from the dictionary without checking for repeats. This might work fine with a small number of values,
# but in a poll with a large number of respondents, it would result in a very repetitive list. To see each language chosen without
# repetition, we can use a set. A set is a collection in which each item must be unique.

# favorite_languages = {
#     'jen':'python',
#     'sarah': 'c',
#     'edward':'rust',
#     'phil':'python',
# }
# print('The following languages have been mentioned:')
# for language in set(favorite_languages.values()):
#     print(language)

# Why Use set? Uniqueness: Sets automatically remove duplicate elements. In the given dictionary, 'python' appears twice
# (for 'jen' and 'phil'). Converting the list of values to a set removes this duplicate. Unordered Collection: Sets do not maintain
# any specific order, but they are ideal for checking membership and removing duplicates.
# When you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the
# collection and builds a set from those items. Here we use set() to pull out the unique languages in
# favorite_languages.values(). You can build a set directly using braces and separating the elements with commas:

# >>> languages = {'python', 'rust', 'python', 'c'}
# >>> languages
# {'rust', 'python', 'c'}

# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs,
# you’re probably looking at a set. Unlike lists and dictionaries, sets do not retain items in any specific order.

# NESTING #
# A LIST OF DICTIONARIES #
# The alien_0 dictionary contains a variety of information about one alien, but it has no room to store information about a second alien
# How can you manage, One way is to make a list of aliens in which each alien is a dictionary of information aboutthat alien.

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points':10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# We first create three dictionaries, each representing a different alien. We store each of these dictionaries in a list called aliens.
# Finally, we loop through the list and print out each alien:

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points':5, 'speed':'medium'}
#     aliens.append(new_alien)
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# print(f'Total number of aliens:{len(aliens)}')

# A for loop iterates over a range of numbers from 0 to 29 (a total of 30 iterations). In each iteration, a new dictionary
# new_alien is created with the keys 'color', 'points', and 'speed', and their respective values 'green', 5, and 'medium'.
# This prints three dots (...) as a separator. This example begins with an empty list to hold all of the aliens that will be created.
# The range() function returns a series of numbers, which just tells Python how many times we want the loop to repeat. Each time the loop
# runs, we create a new alien and then append each new alien to the list aliens. We use a slice to print the first five aliens 4,
# and finally, we print the length of the list to prove we’ve actually generated the full fleet of 30 aliens.

#These aliens all have the same characteristics, but Python considers each one a separate object, which allows us to modify each alien individually

# aliens = []
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points':5, 'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
# for alien in aliens[:5]:
#     print(alien)

# for alien in aliens[:3]: (starts a loop that iterates over the first three aliens in the aliens list. aliens[:3] is a slice that returns
# a list of the first three aliens.)

# if alien['color'] == 'green': (checks if the current alien's color is 'green'. Since all aliens were initially created with 'green' color,
# this condition will be true for the first three aliens.)After this loop completes, the first three aliens in the aliens list
# have their attributes updated to 'yellow', 'medium', and 10 points. Because we want to modify the first three aliens, we loop through a
# slice that includes only the first three aliens. All of the aliens are green now, but that won’t always be the case, so we write
# an if statement to make sure we’re only modifying green aliens. If the alien is green, we change the color
# to 'yellow', the speed to 'medium', and the point value to 10,

# aliens = []
# for alien_number in range(30):
#     new_aline = {'color':'red','points':5, 'speed': 'medium'}
#     aliens.append(new_aline)
# for aline in aliens[0:2]:
#     if aline['color'] == 'red':
#         aline['color'] = 'black'
#         aline['points'] = 15
#         aline['speed'] = 'fast'
#     elif alien ['color'] == 'black':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'slow'
#         alien['points'] = 1
# for aline in aliens[:5]:
#     print(aline)
# print(f'Total number of aliens is {len(aliens)}')

# elif alien ['color'] == 'black':
# checks if the color of the current alien is black. However, since this is within the same loop and after the if block that
# changes the color to black, it won't be executed during the same iteration.
# Since the color was initially red, the if condition is met and changes the alien('s attributes to black, fast, and 15 points.'
# The elif block would only be executed if the alien')s  color was already black at the start of the iteration, which is not the case here.
# The elif block will not be executed in this scenario. Here’s why:
# The if condition changes the alien('s color from red to black and updates other attributes. During the same iteration, the elif block '
# checks the color. Since the color was initially red, the if condition is met and changes the color to black. The elif condition checks
# the color after it has been changed within the same iteration, but it won(')t re-evaluate the same alien in the same loop. Therefore,'
#  the elif block is not executed for the first two aliens. If there were subsequent iterations where the alien started as black,
# the elif block could be executed, but in this specific code structure, it doesn')t happen.
# Why elif Block Doesn't Execute:
# The elif statement is only checked if the if condition is false. When the if condition is true and its block executes, the control
# flow does not continue to the elif. Instead, it moves to the next iteration of the loop.

# First Alien (Index 0):
# Initial State: {'color': 'red', 'points': 5, 'speed': 'medium'}
# Check if aline['color'] == 'red': True
# Execute if Block: Changes to {'color': 'black', 'points': 15, 'speed': 'fast'}
# Skip elif Block: Control moves to the next iteration.
# Second Alien (Index 1):
# Initial State: {'color': 'red', 'points': 5, 'speed': 'medium'}
# Check if aline['color'] == 'red': True
# Execute if Block: Changes to {'color': 'black', 'points': 15, 'speed': 'fast'}
# Skip elif Block: Control moves to the next iteration.

# A LIST IN A DICTIONARY #
# To use the items in the list, we give the name of the dictionary and the key 'toppings',

# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# print(f'You ordered a {pizza['crust']}-crust pizza'
#       'with the following toppings:')
# for topping in pizza['toppings']:
#     print(topping)

# We begin with a dictionary that holds information about a pizza that has been ordered. One key in the dictionary is 'crust', and
# the associated value is the string 'thick'. The next key, 'toppings', has a list as its value that stores all requested toppings.
# We summarize the order before building the  pizza. When you need to break up a long line in a print() call, choose an appropriate
# point at which to break the line being printed, and end the line with a quotation mark. Indent the next line, add an opening quotation
# mark, and continue the string. Python will automatically combine all of the strings it finds inside the parentheses. To print the toppings,
# we write a for loop. To access the list of toppings, we use the key 'toppings', and Python grabs the list of toppings from the dictionary.

# favorite_languages = {
#     'jen': ['python'],
#     'sarah': ['c'],
#     'edward': ['rust', 'go'],
#     'phil': ['python', 'haskell']
# }
# for name, languages in favorite_languages.items():
#     print(f"{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f'\t{language.title()}')
"""The value associated with each name in favorite_languages is now a list. Note that some people have one favorite language and
others have multiple favorites. When we loop through the dictionary , we use the variable name languages to hold each value from
the dictionary, because we know that each value will be a list. Inside the main dictionary loop, we use another for loop to run through
each person’s list of favorite languages. Now each person can list as many favorite languages as they like: To refine this program
even further, you could include an if statement at the beginning of the dictionary’s for loop to see whether each person has
more than one favorite language by examining the value of len(languages). If a person has more than one favorite, the output would
stay the same. If the person has only one favorite language, you could change the wording to reflect that. For example, you could say,
“Sarah’s favorite language is C. You should not nest lists and dictionaries too deeply. If you’re nesting items much
deeper than what you see in the preceding examples, or if you’re working with someone else’s code with significant levels of nesting,
there’s most likely a simpler way to solve the problem.”"""

# A DICTIONARY IN A DICTIONARY #

# You can nest a dictionary inside another dictionary
# users = {
#     'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#     },
#     'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#     },
# }
# for username, user_info in users.items():
#     print(f'\nUsername: {username}')
#     full_name = f'{user_info['first']} {user_info['last']}'
#     location = user_info['location']
#     print(f'\tFull name: {full_name.title()}')
#     print(f'\tLocation: {location.title()}')
"""Outer Dictionary users
users is a dictionary where each key is a username, and the corresponding value is another dictionary with user details.
Keys in users dictionary: 'aeinstein' and 'mcurie'.
Values in users dictionary: Nested dictionaries 
Nested Dictionaries
Each value in the users dictionary is itself a dictionary:
Inside this nested dictionary:
Keys: 'first', 'last', and 'location'
Values: 'albert', 'einstein', and 'princeton' respectively.
 # for username, user_info in users.items(): #
 username: Holds the key from the outer dictionary (e.g., 'aeinstein').
user_info: Holds the corresponding value (e.g., {'first': 'albert', 'last': 'einstein', 'location': 'princeton'}).
user_info["first"]: Accesses the value 'albert' using the key 'first'.
user_info["last"]: Accesses the value 'einstein' using the key 'last'.
user_info['location']: Accesses the value 'princeton' using the key 'location'.
"""

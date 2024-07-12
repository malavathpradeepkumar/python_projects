#1)Variables names can contain only letters numbers and underscores They can start with a letter or an underscore but not with a number For
#instance you can call a variable message_1 but no 1_message
#2) Sapces are not allowed in variable names, but underscores can be used to separate words in vairable names. for example greeting_message works but
#greetin message will cause errors
#3) Avoid using Python keywords and function names as variable names For example print function
#4) Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0
#5) Variable names should be short but descriptive For example name is better than n, and student_name is better than s_n and name_length is better
#than legth_of_persons_name.
#message = 'Hello python crash course'
#print(message)

#STRINGS
#name = 'ada lovelace'
#print(name.title()) (the dot (.) after name in the name.title() tells python to make the title() method act on the variable name)
#print(name.upper())
#print(name.lower())

#COMBINING OR CONCATENATING STRINGS
# It’s often useful to combine strings. For example, you might want to store
# a first name and a last name in separate variables, and then combine them
# when you want to display someone’s full name:
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print(full_name)
# Python uses the plus symbol (+) to combine strings. In this example,
# we use + to create a full name by combining a first_name, a space, and a last name

# SECOND METHOD
# first_name = 'malavath'
# last_name = 'pradeep'
# full_name = first_name + ' ' + last_name
# print('Hello, ' + full_name.title() + '!')

# THIRD METHOD
# sur_name = 'malavath'
# first_name = 'pradeep'
# last_name = 'kumar'
# full_name = sur_name + ' ' + first_name + ' ' + last_name
# print(full_name)

# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# print("Hello, " + full_name.title() + "!")

# first_name = 'malavath pradeep'
# last_name = 'kumar'
# full_name = first_name + ' ' + last_name
# print('Hello, ' + full_name.title() + '!')

# You can use concatenation to compose a message and then store the entire message in a variable
# first_name = "ada"
# last_name = "lovelace"
# full_name = first_name + " " + last_name
# message = "Hello, " + full_name.title() + "!"
# print(message)

#USING VARIABLE IN STRINGS F STRINGS F FOR FORMAT
#first_name = 'malavath'
#last_name = 'pradeep kumar'
#full_name = f'{first_name} {last_name}'
#print(full_name)
#print(f'Hello, {full_name.title()}!')

#ADDING WHITESPACE TO STRINGS WITH TABS AND NEWLINES
#>>>print('\tpython\truby\thtml') ('t' means tab)
#>>>print('\nPython \njava\nJavaScript') ('n' means new line)

#STRIPING WHITESPACE
#>>>favorite_language = 'python         ' observe space after python
#>>>favorite_language.rstrop()       (use this in terminal rstrip() means remove space from right side this will remove space temporarily)
#To remove the whitespace from the string permanently you have to associate the stripped value with the variable name
#>>>favorite_language = 'python          '
#>>>favorite_language = favorite_language.rstrip()
#>>>print(favorite_language)
#>>>favorite_language = 'python        '
#>>>favorite_language.rstrip() remove space from right side
#>>>favorite_language.lstrip() remove space form left side
#>>>favorite_language.strip()remove space from both sides

#REMOVING PREFIXES
#A URL with the common prefix https://
#>>>fb_url = 'https://fb.com'
#>>>fb_url.removeprefix('https://') this will remove prefix temporarly
#remove perminantly
#>>>fb_url = 'https://fb.com'
#>>>fb_url = fb_url.removeprefix('https://')
#>>>simple_url = fb_url.removeprefix('https://') we can also use any changed variable names

#AVOIDING SYNTAX ERRORS WITH STRINGS APOSTROPHE
#message = "One of Python's strengths is its diverse community"
#print(message)
#message = 'One of Python's strengths is its diverse community'

#NUMBERS
#MULTIPLE ASSINGMENTS
#x,y,z = 1,2,3

#CONSTANTS (A constant is a variable whose value stays the same throughout the life of a program Python doesn't have built_in constant types but
#Python programmers use all capital letters to indicate a variable should be treated as a constant and never be changed no change fixed values)
#Any group of numbers there is only one decimal point not multiple(not more than one in any group of numbers) decimal points
#MAX_CONNECTIONS = 5000 (this is constant value)


#COMMENTS
#THE ZEN OF PYTHON
#import this

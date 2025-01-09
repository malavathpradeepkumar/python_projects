# lists allow you to store sets of information in one place
# A list is a collection of items in a particular order you can make a list that includes the letters of the alphabet the digits from 0 to 9
# or the names of all the people in your family. you can put anything you want into a list, and the items in your list don't have to be related
# in any particular way. because a list usually contains more than one element it's good idea to make the name of your list plural.
# that means take list name is plural example cars not car another example is such as letters
# , digits, or names. square brackets[] indicate a list , and individual elements in the list are separated by commas.
#cars = ['honda','audi','maruthi','mahindra']
#print(cars) #if you ask python to print a list python returns its representation of the list, including the square brackets. because this isn't the
# output you want your users to see, let's learn how to access the individual items in a list.

# bikes = ['honda shine', 'glammar', 'hero', 'royal enfield']
# Joining the list items with a comma and space
# output = ', '.join(bikes)
# print(output)

            # OR #
# bikes = ['honda shine', 'glammar', 'hero', 'royal enfield']
# Directly joining and printing the list items with a comma and space
# print(', '.join(bikes))

# To print the items in a list without the square brackets, you can use the join() method, which joins the elements of the list into a single string.
# Separator: The comma , is used as a separator between items. When you specify ',', it means that you want each item in the list to be separated by
# a comma in the resulting string. Single Quotes: The single quotes around the comma are used to define it as a string. You could also use double
# quotes, like ",".join(bikes); both would work the same way.

# ACCESSING ELEMENTS IN A LIST #
#cars = ['audi','mahindra','maruthi','suziki']
# print(cars[3].title()) #When we ask for a single item from a list Python returns just that element without square brackets.
# print(cars[1].upper())

# ACCESSING LAST ELEMENT IN A LIST #
# cars = ['audi','mahindra','maruthi','suziki']
# print(cars[-1].title()) #the index -2 returns the second item form the end of the list.

# USING INDIVIDUAL VALUES FROM A LIST #
# bike = ['glamour','honda shine','royal enfield','ktm']
# message = f'My first bike was a {bike[0].title()}.'
# print(message)
# numbers = [2,3,5,10]
# message = f'My favorite number is {numbers[3]}.'
# print(message)

# MODIFYING, ADDING, AND REMOVING ELEMENTS #
# MODIFYING # to change an element use the name of the list followed by the index of the element you want to change and then provide the new value
# you want that item to have.
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

#ADDING ELEMENT TO A LIST # when you append an item to a list the new element is added to the end of the list.
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles.append('ducati')
# print(motorcycles)
# you can start with an empty list and then add items to the list using a series of append() calls.
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# INSERTING ELEMENTS INTO A LIST # you can add a new element at any position in your list by using the insert() method. you do this by specifying
# the index of the new element and the value of the new item
# motorcycles = ['honda','yamaha','suzuki'] In this example we insert the value 'ducati' at the beginning of the list. The insert() method opens a
# motorcycles.insert(0,'ducati') space at position 0 and stores the value 'ducati' at that location. This operation shifts every other value in the
# print(motorcycles) list one position to the right

# TO ADD MULTIPLE ITEMS TO A LIST AT ONCE #
# EXTEND METHOD #
# bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm']
# bikes.extend(['apache', 'yamaha', 'suzuki'])  # Adding multiple items
# print(bikes)

# Using += Operator   # bikes = bikes + ['apache', 'yamaha', 'suzuki'] #
# bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm']
# bikes += ['apache', 'yamaha', 'suzuki']  # Adding multiple items
# print(bikes)

# using insert() in a Loop (if you want to add at a specific index)

# bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm']
# for item in ['apache', 'yamaha', 'suzuki']:
#     bikes.insert(0, item)  # Insert at index 0 (start of the list)
# print(bikes)


# This loop iterates over the list ['apache', 'yamaha', 'suzuki']. On each iteration, the variable item takes one element from this list
# First Iteration:
#
# item = 'apache'
# bikes.insert(0, 'apache')
# Updated bikes: ['apache', 'honda shine', 'glamour', 'royal enfield', 'Ktm']
# Second Iteration:
#
# item = 'yamaha'
# bikes.insert(0, 'yamaha')
# Updated bikes: ['yamaha', 'apache', 'honda shine', 'glamour', 'royal enfield', 'Ktm']


# REMOVING ELEMENTS FROM A LIST #
# REMOVING AN ITEM USING THE del STATEMENT #
# you can remove an item according to its position in the list. if you know the position of the item you want to remove
# from a list, you can use the del statement
# To delete an item from a list using the del statement in Python, you must specify the index of the item you want to delete, not the item name
# itself. The del statement does not accept item names; it operates only with the position (index) of the item in the list.

# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# del motorcycles[0]  you can no longer access the value that was removed from the list after the del statement is used.
# print(motorcycles)

# REMOVING AN ITEM USING THE pop() METHOD #
# Sometimes you will want to use the value of an item after you remove it from a list. the pop() method remove the last item in a list but it let's
# you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the
# stack. In this analogy, the top of a stack corresponds to the end of a list.
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles) to prove that we still have access to the value that was removed.
# How might  this pop() method be useful? Imagine that the motorcycles in the list are stored in chronological order, according to when we owned
# them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought.
# motorcycles = ['honda','yamaha','suzuki']
# last_owned = motorcycles.pop()
# print(f'The last motorcycle I owned was a {last_owned.title()}.')

# POPPING ITEMS FROM ANY POSITION IN A LIST # index means 0,1,2 means exact positions of items
# You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses
# motorcycles = ['honda','yamaha','suzuki'] Remember that each time you use pop(), the item you work with is no longer stored in the list.
# first_owned = motorcycles.pop(0) If you are unsure whether to use the del statement or the pop() method, here's a simple way to decide when
# print(f'The first motorcycles I owned was a {first_owned.title()}.') to delete an item from a list and not use that item in any way, use the del
# statement, if want to use an item as you remove it, use the pop() method.

# REMOVING AN ITEM BY VALUE #
# Sometimes you won't know the positon of the value you want to remove from a list. If you only know the value of the item you want to remove, you
# can use the remove() method. For example, say we want to remove the value 'ducati' from the list of motorcycles.
# motorcycles = ['honda','yamha','suzuki','ducati']
# print(motorcycles)
# motorcycles.remove('ducati')
# print(motorcycles)
# You can also use the remove() method to work with a value that's being removed from a list. let's remove the value 'ducti' and print a reason
# for removing it from the list.

# motorcycles = ['honda','yamaha','suzuki','ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f'\nA {too_expensive.title()} is too expensive for me.')

# After defining the list, we assign the value 'ducati' to a variable called too_expensive, we then use this variable to tell python which value
# to remove from the list , the value 'ducati' has been removed form the list, but is still accessible through the variable too_expensive, allowing
# us to print a statement about why we removed 'ducati' from the list of motorcycles. The remove() method only the first occurrence of the value
# you specify. if there's a possibility the value appears more than once in the list, you'll need to use a loop to make sure all occurrences of the
# value are removed. you will learn how to do this in chapter 7.

"""bikes.remove(too_expensive): This removes the 'glamour' item from the list, but it doesn't return the removed item or any value, so there's no
need to assign it to a variable. Printing the message: After removing the item, you can print the message using the value of too_expensive,
which still holds the value 'glamour'. you don't need to attach the removed value to a variable. Just remove the item and use the same variable
to reference it when printing."""

# ORGANIZING A LIST #
# SORTING A LIST PERMANENTLY WITH THE SORT() METHOD #
# Imagine we have list of cars and want to change the order of the list to store them alphabetically. to keep the task simple, let's assume that
# all the values in the list are lowercase.
# cars = ['bmw','audi','toyota','subaru'] the sort() method changes the order of the list permanently. The cars are now in alphabetical order,
# cars.sort() and we can never revert to the original order.
# print(cars)
# You can also sort this list in reverse-alphabetical order by passing the argument reverse=True to the sort() method.
# cars= ['bmw','audi','toyota','sabaru']
# cars.sort(reverse=True) again the order of the list is permanently changed.
# print(cars)

# REMOVE MULTIPLE ITEMS AT A TIME #
# 1. Using a Loop with remove() or del

# bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm', 'glamour', 'honda shine']
# items_to_remove = ['glamour', 'honda shine']
#
# for item in items_to_remove:
#     while item in bikes:
#         bikes.remove(item)
#
# print(bikes)  # Output: ['royal enfield', 'Ktm']

# 2nd METHOD #

 # bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm', 'glamour', 'honda shine']
# items_to_remove = ['glamour', 'honda shine']
# Create a new list excluding the items you want to remove
# bikes = [bike for bike in bikes if bike not in items_to_remove]
# print(bikes)  # Output: ['royal enfield', 'Ktm']

""" # if bike not in items_to_remove # This is a condition that checks whether the current bike is not in the items_to_remove list.
not in means that the condition will only be true if the item is absent from items_to_remove. For 'honda shine', 
since 'honda shine' is in items_to_remove, the condition bike not in items_to_remove is False, so it won’t be included in the new list.
 For 'royal enfield', since it’s not in items_to_remove, the condition is True, so 'royal enfield' will be added to the new list."""

# List Comprehension Structure:
# [expression for item in iterable if condition]

# Breaking Down Your Code:
# Outer bike (the first one):
#
# bikes = [bike ...]
# This bike is the expression. It represents what you want to include in the new list.

# bike before for:
# This is the expression that tells Python what to add to the new list.
# Each bike that passes the condition (if bike not in items_to_remove) gets added to the new list.
# Essentially, you are saying, "Add this bike to the new list if it’s not in the items_to_remove list."
# Why Place bike Before for?
# Placing bike before for tells Python, "Take each bike that meets the condition and include it in the new list."
# If you didn’t put bike before for, Python wouldn’t know what to include in the new list, and the list comprehension wouldn’t work.
# List Comprehension: Create a new list excluding the items you want to remove (clean and efficient).
# bikes = [vehicle for vehicle in bikes if vehicle not in rm_v]   # you can also use like this  #

     # 3rd METHOD #

# bikes = ['honda shine', 'glamour', 'royal enfield', 'Ktm', 'glamour', 'honda shine']
# items_to_remove = ['glamour', 'honda shine']
# Using filter to remove unwanted items
# bikes = list(filter(lambda x: x not in items_to_remove, bikes))
# print(bikes)  # Output: ['royal enfield', 'Ktm']

"""# # bikes = list(filter(lambda x: x not in items_to_remove, bikes)) 
filter: What it is: filter is a built-in Python function that allows you to process an iterable (like a list) and filter out elements based on 
a condition. How it works: The filter function takes two arguments means (1st is A function (or lambda): This is a condition that returns True or 
False for  each item. If it returns True, the item is included in the result; if it returns False, the item is excluded.
(2nd is An iterable (like a list): This is the collection of items you want to filter (in your case, the bikes list).: A function that returns True or False (this function defines the condition).
An iterable (like a list) to filter. It goes through each item in the iterable and applies the function to each item. If the function returns 
True, the item is included in the result.  If it returns False, the item is excluded. The filter function will take each bike from the bikes list 
and apply the lambda function to it.
 
lambda:
What it is: A lambda function is a small anonymous function that you can define in one line without formally using the def keyword.
Syntax: The basic syntax for a lambda function is $ lambda arguments: expression $ 
Usage: In the context of the code, lambda x(argument): x not in items_to_remove(expression) is defining a function that takes one argument x 
and checks if x is not  in the items_to_remove list. If x is not in the list, it returns True; otherwise, it returns False. 

list:
What it is: list is another built-in Python function that converts an iterable (like the one produced by filter) into a list.
Usage in this line: After filter processes the bikes list, it produces a filter object (an iterator), which is not a list. The list function 
converts this filter object into a list, allowing you to work with it as a regular Python list.

If x is not in items_to_remove, it returns True, and that bike is included in the new list.
If x is in items_to_remove, it returns False, and that bike is excluded from the new list. 
If x is in items_to_remove, it returns False, and that bike is excluded from the new list. 

in this code (lambda x: x not in items_to_remove, bikes)) the last bikes refers to the original list of bikes  that you want to filter."""


# SORTING A LIST TEMPORARILY WITH THE sorted() FUNCTION #
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
# cars = ['bmw','audi','toyota','subaru']
# print('Here is the original list:') The sorted() function can also accept a reverse=True argument for reverse-alphabetical order
# print(cars)
# print('\nHere is the sorted list:')
# print(sorted(cars))                #Sorted in ascending order
# print(sorted(cars, reverse=True)) #  # Sorted in descending order
# print(sorted(cars, reverse=False))  #  # Sorted in ascending order (same as default)
# print('\nHere is the original list again:')
# print(cars)
# Sorting a list alphabetically is a bit more complicated when all the values are not in lowercase. There are several ways to interpret capital
# letters when determining a sort order, and specifying the exact order can be more complex than we want to deal with at this time. However, most
# approaches to sorting will build directly on what you learned in this section.

# PRINTING A LIST IN REVERSE ORDER #
# cars = ['bmw','audi','toyota','subaru']
# print(cars)  Notice that reverse() doesn't sort backward alphabetically; it simply reverses the order of the list:
# cars.reverse() The reverse() method changes the order of a list permanently, but you can revert to the original order anytime by applying
# print(cars) reverse() to the same list a second time.

# FINDING THE LENGTH OF A LIST # len()
# >>>cars = ['bmw','audi','toyota','subaru'] the list has four items so its length is 4.
# >>>len(cars)
# another method this is i am writing open terminal type only >>>len ('freelancer') enter you will get answer 10.
# Python counts the items in a list starting with one, so you shouldn't run into any off-by-one errors when determining the length of a list.

# AVOIDING INDEX ERRORS WHEN WORKING WITH LISTS # INDEX MEANS 0.1,2,3,4 #
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles[3]) when print this it is showing index out of range, people think the third item is number 3, because they start counting
# at 1. But in python the third item is number 2, because it starts indexing at 0. An index error means Python can't find an item ar the index you
# requested. keep in mind that whenever you want to access the last item in a list, you should use the index -1 This will always work, even
# if your list has changed size since the last time you accessed it:
# The only time this approach will cause an error is when you request the last item from an empty list:
# motorcycles = []
# print(motorcycles[-1]) list index out of range
# If an index error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of your list. your list
# might look much different than you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the
# exact number of items in your list, can help you sort out such logical errors.



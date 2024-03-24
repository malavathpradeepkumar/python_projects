# lists allow you to store sets of information in one place
# A list is a collection of items in a particular order you can make a list that includes the letters of the alphabet the digits from 0 to 9
# or the names of all the people in your family. you can put anything you want into a list, and the items in your list don't have to be related
# in any particular way. because a list usually contains more than one element it's good idea to make the name of your list plural.
# that means take list name is plural example cars not car another example is such as letters
# , digits, or names. square brackets[] indicate a list , and individual elements in the list are separated by commas.
#cars = ['honda','audi','maruthi','mahindra']
#print(cars) #if you ask python to print a list python returns its representation of the list, including the square brackets. because this isn't the
# output you want your users to see, let's learn how to access the individual items in a list.

# ACCESSING ELEMENTS IN A LIST #
#cars = ['audi','mahindra','maruthi','suziki']
# print(cars[3].title()) #When we ask for a single item from a list Python returns just that element without square brackets.
# print(cars[1].upper())

# ACCESSING LAST ELEMENT IN A LIST #
# cars = ['audi','mahindra','maruthi','suziki']
# print(cars[-1].title()) #the index -2 returns the second item form the end of the list.

# USING INDIVIDUAL VALUES FROM A LIST #
# bike = ['glammer','honda shine','royal enfield','ktm']
# message = f'My first bike was a {bike[0].title()}.'
# print(message)
# numbers = [2,3,5,10]
# message = f'My favorite number is {numbers[3]}.'
# print(message)

# MODIFYING, ADDING, AND REMOVING ELEMENTS #
# MODIFYING # to change an element use the name of the list followed by the index of the element you want to change and then provide the new value
# you want that item to have
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# motorcycles[0] = 'ducati'
# print(motorcycles)

#ADDING ELEMENT TO A LIST # when you append an item to a list the new element is added to the end of the list.
# motorcycles = ['honda','yamaha','suziki']
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

# REMOVING ELEMENTS FROM A LIST #
# REMOVING AN ITEM USING THE del STATEMENT #
# you can remove an item according to its position in the list or according to its value. if you know the position of the item you want to remove
# from a list, you can use the del statement
# motorcyles = ['honda','yamaha','suzuki']
# print(motorcyles)
# del motorcyles[0]  you can no longer access the value that was removed from the list after the del statement is used.
# print(motorcyles)

# REMOVING AN ITEM USING THE pop() METHOD #
# Sometimes you will want to use the value of an item after you remove it from a list. the pop() method remove the last item in a list but it let's
# you work with that item after removing it. The term pop comes from thinking of a list as a stack of items and popping one item off the top of the
# stack. In this analogy, the top of a stack corresponds to the end of a list.
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)
# popped_motorcycles = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycles) to prove that ww still have access to the value that was removed.
# How might  this pop() method be useful? Imagine that the motorcycles in the list are stored in chronological order, according to when we owned
# them. If this is the case, we can use the pop() method to print a statement about the last motorcycle we bought.
# motorcycles = ['honda','yamaha','suzuki']
# last_owned = motorcycles.pop()
# print(f'The last motorcycle I owned was a {last_owned.title()}.')

# POPPING ITEMS FROM ANY POSITION IN A LIST # index ante 0,1,2 ante exact positions of items
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

# SORTING A LIST TEMPORARILY WITH THE sorted() FUNCTION #
# To mentain the orginal order of a list but present it in a sorted order, you can use the sorted() function.
# cars = ['bmw','audi','toyota','subaru']
# print('Here is the original list:') The sorted() function can also accept a reverse=True argument for reverse-alphabetical order
# print(cars)
# print('\nHere is the sorted list:')
# print(sorted(cars))
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
# at 1. But in python the third item is number 2, because it starts indexing at 0. An index error means Python can't fin an item ar the index you
# requested. keep in mind that whenever you want to access the last item in a list, you should use the index -1 This will always work, even
# if your list has changed size since the last time you accessed it:
# The only time this approach will cause an error is when you request the last item from an empty list:
# motorcycles = []
# print(motorcycles[-1]) list index out of range
# If an index error occurs and you can't figure out how to resolve it, try printing your list or just printing the length of your list. your list
# might look much different than you thought it did, especially if it has been managed dynamically by your program. Seeing the actual list, or the
# exact number of items in your list, can help you sort out such logical errors.

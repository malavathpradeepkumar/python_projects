# A SIMPLE EXAMPLE #
# Car names are proper names, so the names of most cars should be printed in title case. However, the value 'bmw' should be printed
# in all uppercase. The following code loops through a list of car names and looks for the value 'bmw'. Whenever the value is 'bmw', it’s
# printed in uppercase instead of title case.
# cars = ['audi','bmw','subaru','toyota']
# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# The loop in this example first checks if the current value of car is 'bmw' If it is, the value is printed in uppercase. If the value of car
# is anything other than 'bmw', it’s printed in title case:

# CONDITIONAL TESTS #
# At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test. Python uses
# the values True and False to decide whether the code in an if statement should be executed. If a conditional test evluates to True,
# Python executes the code following the if statement. If the test evaluates to False, Python ignores the  code following the if statement.

 # CHECKING FOR EQUALITY #
# Most conditional tests compare the current value of a variable to a specific value of interest. The simplest conditional test checks
# whether the value of a variable is equal to the value of interest:
# >>> car = 'bmw'
# >>> car == 'bmw'
# True
# The first line sets the value of car to 'bmw' using a single equal sign, as you’ve seen many times already. The next line checks whether
# the value of car is 'bmw' by using a double equal sign (==). This equality operator returns True if the values on the left and right side of
# the operator match, and False if they don’t match. The values in this example match, so Python returns True. When the value
# of car is anything other than 'bmw', this test returns False:
# >>> car = 'audi'
# >>> car == 'bmw'
# False
# A single equal sign is really a statement; you might read the first line of code here as “Set the value of car equal to 'audi'.”
# On the other hand, a double equal sign asks a question: “Is the value of car equal to 'bmw'?” Most
# programming languages use equal signs in this way.

# IGNORING CASE WHEN CHECKING FOR EQUALITY #
# Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:
# >>> car = 'Audi'
# >>> car == 'audi'
# False
# If case matters, this behavior is advantageous. But if case doesn’t matter and instead you just want to test the value of a variable,
# you can convert the variable’s value to lowercase before doing the comparison:
# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True
# The lower() method doesn’t change the value that was originally stored in car, so you can do this kind of comparison without
# affecting the original variable:
# We first assign the capitalized string 'Audi' to the variable car. Then, we convert the value of car to lowercase and compare the
# lowercase value to the string 'audi'. The two strings match, so Python returns True. We can see that the value stored in car
# has not been affected by the lower() method.

# CHECKING FOR INEQUALITY #
# requested_toppings = 'mushrooms'
# if requested_toppings != 'anchovies':
#     print('Hold the anchovies!')

# This code compares the value of requested_topping to the value 'anchovies'. If these two values do not match, Python returns True and executes
# the code following the if statement. If the two values match, Python returns False and does not run  the code following the if statement.
# Most of the conditional expressions you write will test for equality, but sometimes you’ll find it more efficient to test for inequality.

# NUMERICAL COMPARISIONS #
# >>> age = 18
# >>> age == 18
# True
# You can also test to see if two numbers are not equal.
# answer = 17
# if answer != 42:
#     print('That is not correct answer. Please try again!')
# The conditional test passes, because the value of answer (17) is not equal to 42. Because the test passes, the indented code block is executed:
# >>> age = 19
# >>> age < 21
# True
# >>> age <= 21
# True
# >>> age > 21
# False
# >>> age >= 21
# False

# CHECKING MULTIPLE CONDITIONS #
# You may want to check multiple conditions at the same time. For example, sometimes you might need two conditions to be True to take an action.
# Other times, you might be satisfied with just one condition being True. The keywords and and or can help you in these situations.
# To check whether two conditions are both True simultaneously, use the keyword and to combine the two conditional tests; if each test passes,
# the overall expression evaluates to True. If either test fails or if both tests fail, the expression evaluates to False.
# For example, you can check whether two people are both over 21 by using the following test:
# >>> age_0 = 22
# >>> age_1 = 18
# 1 >>> age_0 >= 21 and age_1 >= 21
# False
#  >>> age_1 = 22
# 2 >>> age_0 >= 21 and age_1 >= 21
# True
# First, we define two ages, age_0 and age_1. Then we check whether both ages are 21 or older (1). The test on the left passes, but the
# test on the right fails, so the overall conditional expression evaluates to False. We then change age_1 to 22 (2). The value of age_1 is
# now greater than 21, so both individual tests pass, causing the overall conditional expression to evaluate as True. To improve readability,
# you can use parentheses around the individual tests, but they are not required. If you use parentheses, your test would look like this:
# (age_0 >= 21) and (age_1 >= 21)

# USING OR TO CHECK MULTIPLE CONDITIONS #
# The keyword or allows you to check multiple conditions as well, but it passes when either or both of the individual tests pass. An or
# expression fails only when both individual tests fail.
# >>> age_0 = 22
# >>> age_1 = 18
# (1) >>> age_0 >= 21 or age_1 >= 21
# True
# (2) >>> age_0 = 18
# >>> age_0 >= 21 or age_1 >= 21
# False
# We start with two age variables again. Because the test for age_0 (1) passes, the overall expression evaluates to True. We then lower
# age_0 to 18. In the final test (2), both tests now fail and the overall expression evaluates to False.

# CHECKING WHETHER A VALUE IS IN A LIST # [IN KEYWORD]
# Sometimes it’s important to check whether a list contains a certain value before taking an action. For example, you might want to check whether a
# new username already exists in a list of current usernames before completing someone’s registration on a website
# >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
# >>> 'mushrooms' in requested_toppings
# True
# >>> 'pepperoni' in requested_toppings
# False

# CHECKING WHETHER  A VALUE IS NOT IN A LIST #
# Other times, it’s important to know if a value does not appear in a list. You can use the keyword not in this situation
# banned_users = ['pradeep','rakesh','sai kumar']
# user = 'sharath'
# if user not in banned_users:
#     print(f'{user.title()} you can post a response if you wish.')
# The if statement here reads quite clearly.If the value of user is not in the list banned_users, Python returns True and executes the indented line.

# BOOLEAN EXPRESSIONS #
# As you learn more about programming, you’ll hear the term Boolean expression at some point. A Boolean expression is just another name for  a
# conditional test. A Boolean value is either True or False, just like the value of a conditional expression after it has been evaluated.Boolean values
# are often used to keep track of certain conditions, such as whether a game is running or whether a user can edit certain content on a website.
# game_active = True
# can_edit = False
# KEYWORDS ARE (and, or, in, not) CONDITIONAL TESTS MEANS TRUE OR FALSE IF STATEMENT AND CONDITIONAL TESTS BOTH OR DIFFERENT

# SIMPLE IF STATEMENT #
# The simplest kind of if statement has one test and one action:
# if conditional_test:
#  do something

# You can put any conditional test in the first line and just about any action in the indented block following the test. If the conditional
# test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the
# code following the if statement.
# age = 18
# if age >= 18:
#     print('you are old enough to vote!')
# Indentation plays the same role in if statements as it did in for loops. All indented lines after an if statement will be executed if the
# test passes, and the entire block of indented lines will be ignored if the test does not pass

# IF-ELSE STATEMENTS #
# Often, you’ll want to take one action when a conditional test passes and a different action in all other cases. Python’s if-else syntax makes
# this possible. An if-else block is similar to a simple if statement, but the else statement allows
# you to define an action or set of actions that are executed when the conditional test fails.
# age = 17
# if age >= 18:
#     print('you are old enough to vote!')
#     print('Have you registered to vote yet?')
# else:
#     print('Sorry you are too young to vote !')
#     print('Please register to vote as soon as you turn 18!')
# If the conditional test 1 passes, the first block of indented print()
# calls is executed. If the test evaluates to False, the else block 2 is executed.
# ******* AFTER PRINT FUNCTION all indented at the same level

# THE IF-ELIF-ELSE CHAIN #
# Python executes only one block in an if-elif-else chain. It runs each conditional test in order, until one passes. When a test passes, the code
# following that test is executed and Python skips the rest of the tests
# age = 12
# if age < 4:
#     print("Your admission cost is $0")
# elif age <18:
#     print("Your admission cost is $25")
# else:
#     print("Your admission cost is $40")
# The if test  checks whether a person is under 4 years old. When the test passes, an appropriate message is printed and Python skips the
# rest of the tests. The elif line  is really another if test, which runs only if the previous test failed. At this point in the chain,
# we know the person  is at least 4 years old because the first test failed. If the person is under 18, an appropriate message is
# printed and Python skips the block. If both the if and elif tests fail, Python runs the code in the else block.
# age = 12
# if age < 4:
#     price = 0
# elif age <18:
#     price = 25
# else:
#     price = 40
# print (f"your admission cost is ${price}.")
#  ANOTHER METHOD
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 5
# else:
#     price = 10
# print('your admission cost is $'+ str(price) +' .')
#          OR
# print(f'your admission cost is ${price}.')

# ** IF YOU INDENT LAST PRINT CALL THAT IS INCORRECTLY INDENTED BECAUSE IT IS PART OF THE ELSE BLOCK. SO YOU SHOULD NOT INDENT.
# IT WILL EXECUTE ONLY ELSE STATEMENT WILL BE EVALUATED
# BE CAREFUL AT INDENTATION IF YOU INDENT IN PRINT CALL ONLY ELSE BLOCK WILL BE EXECUTED REST OF THE TEST PRINT CALL IS NOT
# EXECUTED TRY TO INDENT. YOU WILL KNOW WHAT HAPPENS.
# The indented lines set the value of price according to the person’s age, as in the previous example. After the price is set by the
# if-elif-else chain, a separate unindented print() call uses this value to display a message reporting the person’s admission price.

# MORE CONCISE

# USING MULTIPLE ELIF BLOCKS #
# You can use as many elif blocks in your code as you like.
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f' your admission cost is ${price}.')

# OMITTING THE ELSE BLOCK #
# Python does not require an else block at the end of an if-elif chain.Sometimes, an else block is useful. Other times, it’s clearer to
#  use an additional elif statement that catches the specific condition of interest
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65 :
#     price = 40
# elif age >= 65 :
#     price = 20
# print(f'Your total admission cost is ${price}.')
# The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test,
# and that can sometimes include invalid or even malicious data. If you have a specific final condition you’re testing for,
# consider using a final elif block and omit the else block. As a result, you’ll be more confident that your
# code will run only under the correct conditions.

# TESTING MULTIPLE CONDITIONS #
# The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. As soon as Python finds one
# test that passes, it skips the rest of the tests. This behavior is beneficial, because it’s efficient and allows you to test for one
# specific condition. However, sometimes it’s important to check all conditions of interest. In this case, you should use a series of
# simple if statements with no elif or else blocks. This technique makes sense when more than one condition could
# be True, and you want to act on every condition that is True
# requested_toppings = ['mushrooms','extra cheese']
# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms.')
# if 'pepperoni' in requested_toppings:
#     print('Adding peperoni.')
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print('\nFinished making your pizza!')
# The first if statement checks to see whether the person requested mushrooms on their pizza. If so, a message is printed confirming that
# topping. The test for pepperoni  is another simple if statement, not an elif or else statement, so this test is run regardless of
# whether the previous test passed or not. The last if statement checks whether extra cheese was requested, regardless of
# the results from the first two tests. These three independent tests are executed every time this program is run.
# This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes.
# requested_toppings = ['mushrooms','extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# elif 'pepperoni' in requested_toppings:
#     print('Adding pepperoni')
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nfinished making your pizza!")

# USING IF STATEMETNS WITH LISTS #
# CHECKING FOR SPECIAL ITEMS #
# You can do some interesting work when you combine lists and if statements. You can watch for special values that need to be treated
# differently than other values in the list.

# requested_toppings = ['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     print(f'adding {requested_topping}')
# print('\nFineshed making your pizza!')

# But what if the pizzeria runs out of green peppers? An if statement inside the for loop can handle this situation appropriately:

# requested_toppings =  ['mushrooms','green peppers','extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print('Sorry, we are out of green peppers right now.')
#     else:
#         print(f'Adding {requested_topping}')
# print('\nFinished making your pizza!')

# This time, we check each requested item before adding it to the pizza. The if statement checks to see if the person requested green
# peppers. If so, we display a message informing them why they can’t have green peppers. The else block ensures that all other toppings will be added to the pizza.
# The output shows that each requested topping is handled appropriately.

# CHECKING THAT A LIST IS NOT EMPTY #

# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f'Adding {requested_toppings}')
#     print('\nFinished making your pizza!')
# else:
#     print('Are you sure you wat a pain pizza?')

# This time we start out with an empty list of requested toppings. Instead of jumping right into a for loop, we do a quick check first.
# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates
# to False. If requested_toppings passes the conditional test, we run the same for loop we used in the previous example.
# If the conditional test fails, we print a message asking the customer if they really want a plain pizza with no toppings.
# The list is empty in this case, so the output asks if the user really wants a plain pizza: If the list is not empty,
# the output will show each requested topping being added to the pizza.

# USING MULTIPLE LISTS #

# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
#
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f'Adding {requested_topping}')
#     else:
#         print(f'Sorry, we do not have {requested_topping}')

# print('\nFinished making your pizza!')

# HOW THIS WORK HOW TO UNDERSTAND FOR STATEMENT #
# for requested_topping in requested_toppings:  ( this line tells us requested_topping = 'mushrooms' this variable takes only one value
# that is mushrooms then moves to next line untill loop finish for example.)
# requested_topping = 'mushrooms'
# requested_topping = 'french fries'
# requested_topping = 'extra cheese'

# (if requested_topping in available_toppings:   ( this line tells us requested_topping = 'mushrooms')
# so if 'mushrooms' in available_toppings, then print adding 'mushrooms'.)
# next if 'french fries' in available_toppings then print adding 'french fries' if not print else statement as same as another value.


# First, we define a list of available toppings at this pizzeria. Note that this could be a tuple if the pizzeria has a stable selection of toppings.
# Then, we make a list of toppings that a customer has requested. There’s an unusual request for a topping in this example
# 'french fries' Next we loop through the list of requested toppings. Inside the loop, we check to see if each requested topping
# is actually in the list of available toppings . If it is, we add that topping to the pizza. If the requested topping is not in the list
# of available toppings, the else block will run The else block prints a message telling the user which toppings are unavailable.

#STYLING YOUR IF STATEMENTS #

# # In every example in this chapter, you’ve seen good styling habits. The only recommendation PEP 8 provides for styling conditional
# # # tests is to use a single space around comparison operators, such as ==, >=, and <=. For example:
# # # if age < 4:
# # is better than:
# if age<4:
# Such spacing does not affect the way Python interprets your code; it just makes your code easier for you and others to read.


























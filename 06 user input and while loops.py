# HOW THE INPUT FUNTION WORKS #
# message = input('tell me something, and i will repeat it back to you: ')
# print(message)

'''The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it assigns that 
input to a variable to make it convenient for you to work with'''

# WRITING CLEAR PROMPTS #
# name = input('Please enter your name: ')
# print(f'Hello, {name.title()}')
'''Add a space at the end of your prompts (after the colon in the preceding example) to separate the prompt from the user’s response and to make
it clear to your user where to enter their text'''

# prompt = 'If you share your name, we can personalize the message you see.'
# prompt += '\nwhat is your first name? '
# name = input(prompt)
# print(f'\nHello, {name.title()}')
'''This example shows one way to build a multiline string. The first line assigns the first part of the message to the variable prompt. 
In the second line, the operator += takes the string that was assigned to prompt and adds the new string onto the end. The prompt now spans 
two lines, again with space after the question mark for clarity'''

#  USING INT() TO ACCEPT NUMERICAL INPUT #
# When you use the input() function, Python interprets everything the user enters as a string.
# >>> age = input('How old are you? ')
# How old are you? 21
# >>> age
# '21'

# >>> age = input('How old are you? ')
# How old are you? 21
# >>> age >= 18
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>=' not supported between instances of 'str' and 'int'

# When you try to use the input to do a numerical comparison , Python produces an error because it can’t compare a string to an integer.
# We can resolve this issue by using the int() function, which converts the input string to a numerical value.
# height = input('How tall are you, in inches? ')
# height = int(height)
# if height >= 48:
#     print('\nyou are tall enough to ride!')
# else:
#     print('\nYou\'ll be able to ride when you\'re a little older.')

# THE MODULO OPERATOR #
'''The modulo operator doesn’t tell you how many times one number fits into another; it only tells you what the remainder is. When one number
is divisible by another number, the remainder is 0, so the modulo operator always returns 0. You can use this fact to determine
if a number is even or odd:'''

# number = input('Enter a number, and I\'ll tell you if it\'s even or odd: ')
# number = int(number)
# if number % 2 == 0:
#     print(f'\nThe number{number} is even.')
# else:
#     print(f'\nThe number {number} is odd.')

# Even numbers are always divisible by two, so if the modulo of a number and two is zero (here, if number % 2 == 0) the
# number is even. Otherwise, it’s odd.

# INTODUCING WHEILE LOOPS #
# The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while
# loop runs as long as, or while, a certain condition is true.
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

'''current_number += 1 The right-hand side(in our case left hand side) current_number + 1 is calculated: 1 + 1 = 2. The result 2 is then 
assigned back to current_number.In the first line, we start counting from 1 by assigning current_number the value 1. The while loop is
 then set to keep running as long as the value of current_number is less than or equal to 5. The code inside the loop prints the value of 
 current_number and then adds 1 to that value with current_number += 1. (The += operator is shorthand for current_number = current_number + 1.) 
 Python repeats the loop as long as the condition current_number <= 5 is true. Because 1 is less than 5, Python prints 1 and then adds 1, making
the current number 2. Because 2 is less than 5, Python prints 2 and adds 1 again, making the current number 3, and so on. Once the value 
of current_number is greater than 5, the loop stops running and the program ends. current_number += 1 ensures that the loop progresses by updating
 the value of current_number on each iteration. This eventually leads to the loop's termination when the condition controlling the loop is
  no longer met. += is an assignment operator'''

# prompt = '\nTell me something, and i will repeat it back to you:'
# prompt += "\nenter 'quit' to end the program. "
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     print(message)

'''We first define a prompt that tells the user their two options: entering a message or entering the quit value (in this case, 'quit').
Then we set up a variable message to keep track of whatever value the user enters. We define message as an empty string, "", so Python has
something to check the first time it reaches the while line. The first time the program runs and Python reaches the while statement, it needs
to compare the value of message to 'quit', but no user input has been entered yet. If Python has nothing to compare, it won’t be able to
continue running the program. To solve this problem, we make sure to give message an initial value. Although it’s just an
empty string, it will make sense to Python and allow it to perform the comparison that makes the while loop work. This while 
loop runs as long as the value of message is not 'quit'. The first time through the loop, message is just an empty string, so Python
enters the loop. At message = input(prompt), Python displays the prompt and waits for the user to enter their input. Whatever they enter 
is assigned to message and printed; then, Python reevaluates the condition in the while statement. As long as the user has not entered 
the word 'quit', the prompt is displayed again and Python waits for more input. When the user finally
enters 'quit', Python stops executing the while loop and the program ends:'''

# MORE WITH IF STATEMENT #
# prompt = 'tell me something and i will repeat it back to you:'
# prompt += '\nEnter "quit" to end the program:  '
# message = ""
# while message != 'quit' :
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# IN THIS CODE IF USER ENTER QUIT IF STATEMNT DOESN'T PRINT QUIT IT WILL DIRECTLY QUITED WITHOUT SHOWING QUIT PRINT.
# If the condition message != 'quit' is True (meaning the user didn('t type "quit"), the program executes the print(message) line,'
# displaying the user(')s message. If the condition is False (meaning the user did type "quit"), the program skips the print(message)'
# line, so "quit" does not get printed.).

# USING A FLAG #
'''For a program that should run only as long as many conditions are true, you can define one variable that determines whether or not the
entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so they run while the
flag is set to True and stop running when any of several events sets the value of the flag to False. As a result, our overall while statement
needs to check only one condition: whether the flag is currently True. Then, all our other tests (to see if an event has occurred that should 
set the flag to False) can be neatly organized in the rest of the program.'''

# prompt = '\nTell me something, and I will repeat it back to you:'
# prompt += '\nEnter "quit" to end the program: '
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

'''We set the variable active to True so the program starts in an active state. Doing so makes the while statement simpler because no
comparison is made in the while statement itself; the logic is taken care of in other parts of the program. As long as the active variable
remains True, the loop will continue running. In the if statement inside the while loop, we check the value of message once the user enters
their input. If the user enters 'quit', we set active to False, and the while loop stops. If the user enters anything other than 'quit',
we print their input as a message. This program has the same output as the previous example where we placed the conditional test directly 
in the while statement. But now that we. have a flag to indicate whether the overall program is in an active state, it would be easy to add 
more tests (such as elif statements) for events that should cause active to become False. This is useful in complicated programs like games, 
in which there may be many events that should each make the program stop running. When any of these events causes the active flag to
become False, the main game loop will exit, a Game Over message can be displayed, and the player can be given the option to play again.'''

# USING A BREAK TO EXIT A LOOP #
'''To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test, use the
break statement. The break statement directs the flow of your program; you can use it to control which lines of code are executed and which 
aren’t, so the program only executes code that you want it to, when you want it to.'''

# prompt = '\nPlease enter the name of a city you have visited:'
# prompt += '\n(Enter "quit" when you are finished: '
# while True:
#     city = input(prompt)
#     if city == "quit" :
#         break
#     else:
#         print(f'I\'d love to go to {city.title()}!')
'''A loop that starts with while True  will run forever unless it reaches a break statement. The loop in this program continues asking 
the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit', the break statement runs, 
causing Python to exit the loop. You can use the break statement in any of Python’s loops. For example, you could use break to quit
 a for loop that’s working through a list or a dictionary.'''

# USING CONTINUE IN A LOOP #
# current_number = 0
# while current_number < 10 :
#     current_number += 1
#     if current_number % 2 == 0:    # IF TRUE REST OF THE CODE WILL BE SKIP #
#         continue
#     print(current_number) THIS IS WITHOUT SPACE OUTSIDE THE IF BLOCK NOT INSIDE BECASUE THERE IS NO INDENTATION
        # print(current_number) IN SIDE THE IF BLOCK

# IN THIS CODE THE 2ND PRINT IS WRONG TRY THAT YOU WILL SEE NOTHING WHEY THE REASON IS #
'''Indentation in Python:
Indentation defines scope: In Python, indentation is used to define the scope of code blocks. Code that('s indented under '
'a particular statement' (like if, while, for, etc.) is considered part of that block.) while loop block: All the code indented under
a while loop is part of that loop. if statement block: All the code indented under an if statement is part of that if block.
continue statement: When a continue statement is executed, the program skips the rest of the code in the current iteration of the loop
and moves on to the next iteration.'''

# Step-by-Step Execution: #
'''current_number = 0: Initializes current_number to 0.
while current_number < 10: Starts the loop that runs as long as current_number is less than 10.
current_number += 1: Increases current_number by 1 at each iteration.
if current_number % 2 == 0: Checks if current_number is even.
continue: If the number is even, the loop skips the rest of the code in that iteration and goes back to the start of the loop.
print(current_number): Because this line is indented under the if statement, it’s part of the if block. However, since continue 
is above it, this line is never executed for even numbers.
continue: When the loop encounters continue, it immediately jumps back to the start of the while loop, skipping the print statement
print(current_number): By moving this line outside the if block (and thus after the continue), the program ensures it only prints
current_number when the loop does not continue, continue: Skips the rest of the loop (including the print statement) for even numbers. '''

# Correct Placement: #
'''Inside the if block: The print statement would be skipped for even numbers due to continue.
Outside the if block: The print statement will execute for odd numbers because it is not affected by continue.
So the print(current_number) placement outside the if block is correct.'''

# AVOIDING INFINITE LOOPS #
'''Every while loop needs a way to stop running so it won’t continue to run forever. However, if you accidentally omit the line x += 1,
the loop will run forever.'''

# USING A WHILE LOOP WITH LISTS AND DICTIONARIES #
'''A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble 
keeping track of the items in the list. To modify a list as you work through it, use a while loop. Using while loops with lists and 
dictionaries allows you to collect, store, and organize lots of input to examine and report on later.'''

# MOVING ITEMS FROM ONE LIST TO ANOTHER #
'''Consider a list of newly registered but unverified users of a website. After we verify these users, how can we move them to a separate list
of confirmed users? One way would be to use a while loop to pull users from the list of unconfirmed users as we verify them and then add them 
to a separate list of confirmed users.'''

# Start with users that need to be verified,
# and an empty list to hold confirmed users.
# unconfirmed_users = ['alice','brain','candace']
# confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()    # IF YOU DON NOT SPECIFY INDEX POP REMOVES LAST VALUE AUTOMETICALLY #
#     print(f'Verifying user: {current_user.title()}') # OBSERVE THESE ARE ALL PART OF WHILE LOOP #
#     confirmed_users.append(current_user) # As the list of unconfirmed users shrinks, the list of confirmed users grows. #
# Display all confirmed users.
# print(f'\nThe following users have been confirmed:') #OBSERVE THESE ARE ALL NOT PART OF WHILE LOOP #
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

'''while unconfirmed_users:: This loop runs as long as there are elements in the unconfirmed_users list. The loop stops when
unconfirmed_users is empty.  current_user = unconfirmed_users.pop(): The pop() method removes the last item from the unconfirmed_users 
list and assigns it to the  variable current_user. In each iteration, pop() decreases the size of unconfirmed_users by one, and the 
removed element (e.g., 'candace') is stored in current_user. Why pop()?: pop() is used here because it allows us to remove the user 
from unconfirmed_users while  simultaneously capturing and storing that user in current_user for processing. The pop() method is essential
here because it allows the program to remove users from unconfirmed_users one by one while processing them. If you want to remove a value from
a list and use that removed value afterward, the pop() method is the better choice.'''

'''We begin with a list of unconfirmed users  (Alice, Brian, and Candace) and an empty list to hold confirmed users. The while loop runs
as long as the list unconfirmed_users is not empty . Within this loop, the pop() method removes unverified users one at a time from the
end of unconfirmed_users . Because Candace is last in the unconfirmed_users list, her name will be the first to be removed, assigned
to current_user, and added to the confirmed_users list . Next is Brian, then Alice. We simulate confirming each user by printing a
verification message and then adding them to the list of confirmed users. As the list of unconfirmed users shrinks, the list
of confirmed users grows. When the list of unconfirmed users is empty, the loop stops and the list of confirmed users
is printed.'''

# REMOVING ALL INSTANCES OF SPECIFIC VALUES FROM A LIST #
'''we used remove() to remove a specific value from a list. The remove() function worked because the value we were interested in appeared
only once in the list. But what if you want to remove all instances of a value from a list? Say you have a list of pets with the
value 'cat' repeated several times. To remove all instances of that value, you can run a while loop until 'cat' is no
longer in the list.'''

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

'''We start with a list containing multiple instances of 'cat'. After printing the list, Python enters the while loop because it finds the
value 'cat' in the list at least once. Once inside the loop, Python removes the first instance of 'cat', returns to the while line, and 
then reenters the loop when it finds that 'cat' is still in the list. It removes each instance of 'cat' until the value is no longer in
the list, at which point Python exits the loop and prints the list again.'''

# FILLING A DICTIONARY WITH USER INPUT #
# responses = {}
# polling_active = True
# while polling_active :
#     name = input('\nWhat is your name? ')
#     response = input('which mountain would you like to climb some day? ')
#     responses[name] = response
#     repeat = input('Would you like to let another person respond? (Yes/no)') # (this print no and if repeat == 'no' there is no relation
#     if repeat == 'no':                                                         between them both are different you want to stop you must
#         polling_active = False                                                 enter no that is if repeat no not print no) #
# print('\n--- Poll results ---')
# for name,response in responses.items():
#     print(f'{name} would you like to climb {response}.')

'''The while loop starts and will continue running as long as polling_active is True. name and response and repeat are variable to store 
user input. responses[name] = response  The user's name and their preferred mountain are stored as a key-value pair in the responses 
dictionary. The name is the key, and the response is the value.  if repeat == 'no':     polling_active = False  
If the user types 'no', the polling_active variable is set to False, which will cause the while loop to stop running, 
ending the polling process. If the user types anything other than 'no', the loop will continue. If they enter yes, the program enters
the while loop again. If they enter no, the polling_active flag is set to False, the while loop stops running.

Yes, in this code, polling_active is a variable A variable is a named storage location in memory that can hold a value. In this case, 
polling_active is used as a boolean variable that can hold either True or False.
Purpose of polling_active: It controls whether the while loop should continue running. When polling_active is set to True, the
loop continues to ask for user inputs. When it's set to False, the loop stops, ending the polling process. '''










# DEFINING A FUNCTION #
# def greet_user():
#     """simple prints a greet message"""
    # print('Hello!')
# greet_user()      #if you indent after greet_user that is RecursionError ask chatgpt #

"""" Any indented lines that follow def greet_user(): make up the body of the
function. def greet_user(): This line defines a function named greet_user.
The keyword def is used to create a new function.
greet_user is the name of the function.
The parentheses () after the function name indicate that this function does not take any arguments.
The colon : at the end of the line signifies the start of the function's code block.

simple prints a greet message   (docstring optional)
This is a docstring, a special type of comment used to describe what the function does.
The triple quotes  allow for a multi-line string and are typically used for documentation.
Here, the docstring explains that the function "simple prints a greet message."

print('Hello!')
The line print("Hello!") is the only line of actual code in the body of
this function, so greet_user() has just one job: print("Hello!"). This line is the actual code inside the greet_user function.
The print() function is called to output the string 'Hello!' to the console.

End of Function:
The function ends when the indentation returns to the same level as the def statement. Since there is no more indented
 code after the print() statement, the function definition is complete.

Call the Function:
greet_user()
This line of code is outside the function definition.
It calls or invokes the greet_user() function, which triggers the code inside the function to be executed.
When the function is called, it prints 'Hello!' to the console.

What is the Body of a Function?
The body of a function is the part of the function where you write the code that tells the function what to do.  It’s like the 
“instructions” that the function will follow when you call it. The "body" of a function in Python refers to the block of code that
is executed when the function is called.

# How is the Body of a Function Structured? #
Indentation:
The body of the function must be indented (moved to the right) under the function definition. 
This indentation is important because it shows that these lines belong to the function.

Statements:
The body of a function can contain any number of statements that define what the function does. These statements can include:
Expression Statements: Operations like calculations, string manipulations, etc.
Control Structures: if, for, while loops, etc.
Function Calls: Invoking other functions within this function.
Return Statements: Returning a value from the function.
Comments: Lines that describe what parts of the function do, often used for clarity.
Docstrings: Optional documentation that explains the purpose and behavior of the function.

What Goes in the Body?
Code that Does Something: Inside the function body, you write the actual code that you want the function to execute.
This could be printing a message, performing a calculation, or anything else you need.

How it Works:
When you call the function (like greet_user()), Python will look inside the function body and execute the code there."""

# PASSING INFORMATION TO A FUNCTION #
# def greet_user(username):
#     """display a simple greeting"""
#     print(f'Hello, {username.title()} ')
# greet_user('jesse')

# ARGUMENTS AND PARAMETERS #
'''The variable username in the definition of greet_user() is an example of a parameter, a piece of information the function needs to do 
its job. The value 'jesse' in greet_user('jesse') is an example of an argument. An argument is a piece of information that’s passed 
from a function call to a function. When we call the function, we place the value we want the function to work with in parentheses. 
In this case the argument 'jesse' was passed to the function greet_user(), and the value was assigned to the parameter username.'''

# PASSING ARGUMENTS #
'''Because a function definition can have multiple parameters, a function call may need multiple arguments. You can pass arguments to your 
functions in a number of ways. You can use positional arguments, which need to be in the same order the parameters were written; keyword
arguments, where each argument consists of a variable name and a value; and lists and dictionaries of values.'''

# POSITIONAL ARGUMENTS #
# def describe_pet(animal_type, animal_name):
#     """Display information about a pet"""
#     print(f'\nI have a {animal_type}')
#     print(f'My {animal_type} name is {animal_name}')
# describe_pet('harry', 'hamster')
# describe_pet('dog', 'willie')    # MULTIPLE FUNCTION CALLS #   TRY TO CHANGE ORDER OF THE ARGUMENTS YOU WILL GET CONFUCING RESULTS.
"""in the function call, the argument 'hamster' is assigned to the parameter animal_type and the argument 'harry'
is assigned to the parameter pet_name."""

# ORDER MATTERS IN POSITIONAL ARGUMENTS #
# You can get unexpected results if you mix up the order of the arguments in a function call when using positional arguments:

# KEYWORD ARGUMENTS #
'''A keyword argument is a name-value pair that you pass to a function. You directly associate the name and the value within the 
argument, so when you pass the argument to the function, there’s no confusion.'''
# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
#     print(f'\nI have a {animal_type}')
#     print(f'My {animal_type} name is {pet_name}')
# describe_pet(animal_type='hamster', pet_name='harry')
# describe_pet(pet_name='harry', animal_type='hamster')

 # DEFAULT VALUES #
'''When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the 
function call, Python uses the argument value. If not, it uses the parameter’s default value. So when you define a default value for 
a parameter, you can exclude the corresponding argument you’d usually write in the function call. Using default
values can simplify your function calls and clarify the ways your functions are typically used.In Python, all default
 arguments must come after the required arguments in a function definition.'''
# def describe_pet(pet_name, animal_type = 'dog'):
#     """Display information about a pet"""
#     print(f'\nI have a {animal_type}')
#     print(f'My {animal_type} name is {pet_name}')
# describe_pet(pet_name='willie')

'''Note that the order of the parameters in the function definition had to be changed. Because the default value makes it unnecessary 
to specify a type of animal as an argument, the only argument left in the function call is the pet’s name. Python still interprets this
as a positional argument, so if the function is called with just a pet’s name, that argument will match up with the first parameter listed 
in the function’s definition. This is the reason the first parameter needs to be pet_name. The only argument provided is 'willie', so it is
matched up with the first parameter in the definition, pet_name. Because no argument is provided for animal_type, Python uses the default
 value 'dog'. To describe an animal other than a dog, you could use a function call like this:'''
  # describe_pet(pet_name='harry', animal_type= 'hamster')
# Because an explicit argument for animal_type is provided, Python will ignore the parameter’s default value.
""" When you use default values, any parameter with a default value needs to be listed
after all the parameters that don’t have default values. This allows Python to continue interpreting positional arguments correctly"""

# EQUIVALENT FUNCTION CALLS #
"""Because positional arguments, keyword arguments, and default values can all be used together, you’ll often have several equivalent
ways to call a function. Consider the following definition for describe_pet() with one default value provided:"""
# def describe_pet(pet_name, animal_type='dog'):

"""With this definition, an argument always needs to be provided for
pet_name, and this value can be provided using the positional or keyword format. If the animal being described is not a dog,
an argument for animal_type must be included in the call, and this argument can also be specified using the positional or keyword format."""

# A dog named Willie.
# describe_pet('willie')
# describe_pet(pet_name='willie')
# A hamster named Harry.
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

# Each of these function calls would have the same output as the previous examples. It doesn’t really matter which calling style you use.
# As long as your function calls produce the output you want, just use the style you find easiest to understand.

# AVOIDING ARGUMENTS ERRORS #
"""When you start to use functions, don’t be surprised if you encounter errors about unmatched arguments. Unmatched arguments 
occur when you provide fewer or more arguments than a function needs to do its work."""

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet"""
    # print(f'\nI have a {animal_type}')
    # print(f'My {animal_type} name is {pet_name}')
# describe_pet()
# """ Python recognizes that some information is missing from the function call, and the traceback tells us that: """

# RETURN VALUES #
# def get_formatted_name(first_name, last_name):
#     """Return a full name neatly formatted"""
#     full_name = f'{first_name} {last_name}'  # full_name is a variable #   #this is jimmi hendrix #
#     return full_name.title()                                              # this is Jimmi Hendrix ## RETURN IS KEYWORD IN PYTHON #
# musician = get_formatted_name('jimmi', 'hendrix')       # musician = Jimmi Hendrix # this is function called #
# print(musician)                                                            # print(Jimmi Hendrix) #

""" return full_name.title()  The return keyword is used to send the result of the function back to the caller. full_name.title()
converts the full_name to title case, where the first letter of each word is capitalized. For example, 'jimmi hendrix' will be converted 
to 'Jimmi Hendrix'. The return statement terminates the function and sends the value 'Jimmi Hendrix' back to where the function was called.

Calling the Function and Storing the Result:
musician = get_formatted_name('jimmi', 'hendrix')
Here, the get_formatted_name() function is called with 'jimmi' as first_name and 'hendrix' as last_name.
The result of the function (which will be 'Jimmi Hendrix') is stored in the variable musician."""

"""Summary of Variables:
first_name and last_name: These are the function's input arguments (parameters).
full_name: A local variable inside the function that stores the concatenated and formatted full name.
musician: A variable that stores the returned value from the function call, which is the formatted name.

What Happens During a Function Call?
You call the function:
musician = get_formatted_name('jimmi', 'hendrix')  # this is a function call #
This triggers the execution of the code inside the function get_formatted_name.
The function runs:
The function receives 'jimmi' as the first_name and 'hendrix' as the last_name. Inside the function, the code concatenates the
names and formats them into title case.
The return statement:
return full_name.title()
This return statement sends the value 'Jimmi Hendrix' back to where the function was called (which is at the
line musician = get_formatted_name(...)). The function call is replaced by the returned value: After the function has finished running,
the return statement gives back the formatted name 'Jimmi Hendrix'. That value gets assigned to the variable musician.
So, the function call get_formatted_name('jimmi', 'hendrix') is essentially replaced with the value 'Jimmi Hendrix'. 
Stops execution: After the return statement, the function stops running."""

# def add_numbers(a,b):
#     return a + b                           # this is 7 #
# result = add_numbers(3,4)                   # result = 7 #
# print(result)                                # print(7) #

# Here, the function add_numbers(3, 4) calculates the sum and returns the value 7. The calling code (where the function was
# called) receives this value and assigns it to the variable result.

""" Calling the Function: musician = get_formatted_name('jimmi', 'hendrix')
At this point, you are calling the function get_formatted_name() and passing in 'jimmi' as the first_name and 'hendrix' as the last_name.
The function starts executing from the beginning. The values 'jimmi' and 'hendrix' are passed as arguments to the parameters first_name
and last_name, executing the Function Body: Inside the function, the following happens: full_name = f'{first_name} {last_name}'
The values 'jimmi' and 'hendrix' are used to create the variable full_name, which becomes 'jimmi hendrix'
The return Statement: return full_name.title()
At this point, the function encounters the return statement. Before the function exits, it returns the value of full_name.title(), 
which is 'Jimmi Hendrix'. This returned value is passed back to the line of code that called the function.
Assigning the Returned Value: musician = get_formatted_name('jimmi', 'hendrix')
The value 'Jimmi Hendrix' is returned from the function and assigned to the variable musician.
After this, the function completes its execution and exits. This is when the function truly stops running.
Continuing with the Program: print(musician)
Now, the program continues running, and the value of the variable musician ('Jimmi Hendrix') is printed.
Summary: The function does not stop executing until it reaches the return statement. All the code before the return statement runs 
completely, which includes taking the first_name and last_name, creating the full_name, and formatting it.
Once the return statement is encountered, the function stops running, but only after it has returned a value to the calling code.
In your case, 'Jimmi Hendrix' is returned by the return statement, assigned to musician, and then printed."""

# IMP #

"""In This code, the first line that runs is the function call, not the function definition. Python starts executing from
top to bottom, but functions do not run until they are called,  # musician = get_formatted_name('jimmi', 'hendrix') #
This is the first line that actually runs. Python calls the function get_formatted_name() with the arguments 'jimmi' and 'hendrix'.
# def get_formatted_name(first_name, last_name):#
Once the function is called, Python jumps to the function definition and starts executing the code inside the function. """

# MAKING AN ARGUMENT OPTIONAL #
# Sometimes it makes sense to make an argument optional, so that people using the function can choose to provide extra information only
# if they want to.
# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f'{first_name} {middle_name} {last_name}'
#     return full_name.title()
# musician = get_formatted_name('john','lee','hooker')
# print(musician)

""" But middle names aren’t always needed, and this function as written would not work if you tried to call it with only a first name and a 
last name. To make the middle name optional, we can give the middle_name argument an empty default value and ignore the argument unless 
the user provides a value. To make get_formatted_name() work without a middle name, we set the default value of middle_name to an empty
string and move it to the end of the list of parameters: """

# def get_formated_name(first_name, last_name, middle_name = ''):
#     """ Return a full name neatly formatted """
#     if middle_name:
#         full_name = f'{first_name} {middle_name} {last_name}'
#     else:
#         full_name = f'{first_name} {last_name}'
#     return full_name.title()
# musician = get_formated_name('jimmi', 'hendrix')
# print(musician)
# musician = get_formated_name('john', 'hooker', 'lee')
# print(musician)

""" # middle_name='': #  An optional parameter with a default value of an empty string ''. If no middle name is provided, this parameter 
will default to an empty string. if middle_name:: This checks if middle_name is not an empty string. In Python, a non-empty string evaluates 
to True, while an empty string evaluates to False. If middle_name is provided (not empty): The full_name is constructed with first_name,
 middle_name, and last_name, formatted as f'{first_name} {middle_name} {last_name}'. If middle_name is not provided (empty): The full_name
is constructed with just first_name and last_name, (else block execute). Explanation of Empty String and Middle Name
Why Use an Empty String for middle_name? Optional Parameter: Providing middle_name='' allows the function to be called with or without
a middle name. If a middle name isn’t needed, you can simply omit it, and the function will use the empty string as the default value.
Why Put middle_name Last in the Function Definition? Optional Parameters Last: In Python, optional parameters (with default values)
are typically placed at the end of the parameter list. This allows for more flexible function calls, where the optional parameter
can be omitted without causing errors.
 # Understanding Empty Strings #
An empty string in Python is a string that contains no characters and is represented as ''. Here's how it behaves:
Boolean Value: An empty string is considered False in a boolean context, meaning it evaluates to False when used in conditions.
Non-empty String: Any string with one or more characters is considered True in a boolean context. Conditional Check: The if
 middle_name: condition checks whether middle_name is non-empty. If middle_name is an empty string, the if condition evaluates to 
False, and the else block is executed. """

"""In this example, the name is built from three possible parts. Because there’s always a first and last name, these parameters are 
listed first in the function’s definition. The middle name is optional, so it’s listed last in the definition, and its default value is
an empty string. In the body of the function, we check to see if a middle name has been provided. Python interprets non-empty strings as
True, so the conditional test if middle_name evaluates to True if a middle name argument is in the function call. If a middle name is 
provided, the first, middle, and last names are combined to form a full name. This name is then changed to title case and returned to the
function call line, where it’s assigned to the variable musician and printed. If no middle name is provided, the empty string fails the if
test and the else block runs . The full name is made with just a first and last name, and the formatted name is returned to the
calling line where it’s assigned to musician and printed. Calling this function with a first and last name is straightforward. If
we’re using a middle name, however, we have to make sure the middle name is the last argument passed so Python will match up the positional
arguments correctly"""

# RETURNING A DICTIONARY #
# A function can return any kind of value you need it to, including more complicated data structures like lists and dictionaries.
# def build_person(first_name, last_name):
#     """ Return a dictionary of information about a person """
#     person = {'first': first_name, 'last': last_name}
#     return person
# musician = build_person('jimi', 'hendrix')
# print(musician)
"""The function build_person() takes in a first and last name, and puts these values into a dictionary . The value of first_name is
 stored with the key 'first', and the value of last_name is stored with the key 'last'. Then, the entire dictionary representing the 
person is returned . The return value is printed  with the original two pieces of textual information now stored in a dictionary."""

# You can easily extend this function to accept optional values like a middle name, an age, an occupation, or any other
# information you want to store about a person.

# def build_person(first_name, last_name, age=None):
#     """Return a dictionary of information about a person"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# age=None: An optional parameter with a default value of None. This means if no value is provided for age, the function
# will use None as its default.
# Conditional Check for age:
# if age:
#     person['age'] = age
"""if age:: This condition checks whether age has a value that is considered True. In Python, None, 0, empty strings (''), and 
empty collections ([], {}, etc.) are considered False, while any non-empty value is considered True. If age is not None (or another
 falsey value), the age is added to the person dictionary with the key 'age' and the corresponding value. # return person #
 The function returns the person dictionary, which contains the keys 'first', 'last', and optionally 'age' if a valid age was provided."""

"""None:
Default Value: None is used here as the default value for age to indicate that if no age is provided, the function will not include an 
'age' key in the dictionary. Conditional Check: When age is None, the if age: condition evaluates to False, so the 'age' key is not added 
to the dictionary. age Parameter:
If age is provided (and is not None), it is added to the person dictionary with the key 'age'.
If age is not provided (i.e., it remains as None), the 'age' key is not included in the dictionary."""

# USING A FUNCTION WITH A WHILE LOOP #
# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f'{first_name} {last_name}'
#     return full_name.title()
# while True:
#     print('\nPlease tell me your name:')
#     print('(enter \'q\' at any time to quit)')
#
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     l_name= input("Last name: ")
#     if l_name == 'q':
#         break
#     formated_name = get_formatted_name(f_name, l_name)
#     print(f'Hello, {formated_name}')
# if you do not use break statement it will go infinite times.

# PASSING A LIST #
# You’ll often find it useful to pass a list to a function, whether it’s a list of names, numbers, or more complex objects, such as
# dictionaries. When you pass a list to a function, the function gets direct access to the contents of the list.
# def greet_users(names):
#     """print a simple greeting to each user in the list. """
#     for name in names:           # name is a variable to hold values #
#         msg = f'Hello, {name.title()}!'
#         print(msg)
# usernames = ['pradeep', 'rakesh', 'sai kumar']
# greet_users(usernames)
"""We define greet_users() so it expects a list of names, which it assigns to the parameter names. The function loops through the
list it receives and prints a greeting to each user. Outside of the function, we define a list of users and then pass the list 
usernames to greet_users() in the function call."""

 # MODIFYING A LIST IN A FUNCTION #
# When you pass a list to a function, the function can modify the list. Any changes made to the list inside the function’s body are
# permanent, allowing you to work efficiently even when you’re dealing with large amounts of data.

# start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f'Printing models: {current_design}')
#     completed_models.append(current_design)
# Display all completed models
# print('\nThe following models have been printed.')
# for completed_model in completed_models:
#     print(completed_model)

# We can reorganize this code by writing two functions, each of which does one specific job. Most of the code won’t change; we’re just
# structuring it more carefully. The first function will handle printing the designs, and the second will summarize the prints
# that have been made.

"""while unprinted_designs:: This loop continues to execute as long as unprinted_designs is not empty.
unprinted_designs is a list, and in Python, a non-empty list evaluates to True, while an empty list evaluates to False
When the Loop Stops
The loop will stop when unprinted_designs becomes an empty list. Here's how this happens step-by-step in your code:
Initial State:
unprinted_designs contains: ['phone case', 'robot pendant', 'dodecahedron'] (non-empty list, evaluates to True).
First Iteration:
current_design = unprinted_designs.pop() removes 'dodecahedron' from the list and assigns it to current_design.
print(f'Printing models: {current_design}') prints 'Printing models: dodecahedron'.
completed_models.append(current_design) adds 'dodecahedron' to completed_models.
New state:
unprinted_designs: ['phone case', 'robot pendant']
completed_models: ['dodecahedron']

Second Iteration:
current_design = unprinted_designs.pop() removes 'robot pendant' from the list and assigns it to current_design.
print(f'Printing models: {current_design}') prints 'Printing models: robot pendant'.
completed_models.append(current_design) adds 'robot pendant' to completed_models.
New state:
unprinted_designs: ['phone case']
completed_models: ['dodecahedron', 'robot pendant']

Third Iteration:
current_design = unprinted_designs.pop() removes 'phone case' from the list and assigns it to current_design.
print(f'Printing models: {current_design}') prints 'Printing models: phone case'.
completed_models.append(current_design) adds 'phone case' to completed_models.
New state:
unprinted_designs: [] (empty list, evaluates to False)
completed_models: ['dodecahedron', 'robot pendant', 'phone case']

Loop Stops:
The loop condition while unprinted_designs: is now while []: (an empty list), which evaluates to False.
Therefore, the while loop stops executing. The while loop in Python stops when its condition evaluates to False
Evaluation: In Python, a non-empty list evaluates to True, and an empty list evaluates to False.
As long as designs remain in unprinted_designs, the while loop simulates printing each design by removing a design from the end of
the list, storing it in current_design, and displaying a message that the current design is being printed. It then adds the design 
to the list of completed models."""

# def print_models(unprinted_designs, completed_models):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f'Printing model: {current_design}')
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     """show all the models that were printed"""
#     print('\nThe following models have been printed:')
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_desings = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []   #  empty list that will hold the completed models. #
# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

"""In this code, the def lines are executed first, but they are not executed in the sense of running the code inside the functions. They define
the functions and store them in memory. The actual execution of the code inside the functions happens when the functions are called.
Execution Order
def Lines:
These lines define the functions and make them available to be called later.
They set up the functions print_models and show_completed_models but do not execute their code at this point.
Function Calls:
The actual code inside the functions runs only when the functions are called.
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
The print_models function is called first, and then the show_completed_models function is called.
 # Summary #
def lines: Define functions and prepare them for use. This is done first but does not execute the function code.
Function calls: Execute the code inside the functions. This happens after the function definitions.
In practical terms, the function definitions (def) are executed first when the script is loaded, but they only prepare the functions.
The actual execution of the code inside the functions happens when you call them.

After the Function Call:
When print_models(unprinted_desings, completed_models) is called, the completed_models list is initially empty.
During the execution of print_models, each design is moved from unprinted_designs to completed_models.
Example:
If unprinted_designs initially contains ['phone case', 'robot pendant', 'dodecahedron'], and the function is called, it will:
Print and remove 'dodecahedron', adding it to completed_models.
Print and remove 'robot pendant', adding it to completed_models.
Print and remove 'phone case', adding it to completed_models
By the end of the print_models function, completed_models will hold all the designs that were originally in unprinted_designs, a
nd unprinted_designs will be empty.

# 2nd function show_completed_models(completed_models): in this function how completed_models take values #
By the end of this function, completed_models will contain all the designs that were in unprinted_desings, and unprinted_desings 
will be empty. For example, if unprinted_desings had ['phone case', 'robot pendant', 'dodecahedron'], then after the function call, 
completed_models will be ['dodecahedron', 'robot pendant', 'phone case'].
 # show_completed_models(completed_models) #
 This function receives the completed_models list, which was modified by the print_models function.
It prints out each item in the completed_models list.
 # Summary #
How Values Are Passed:
When print_models is called, it modifies the completed_models list by adding items to it.
When show_completed_models is called after print_models, it uses the same completed_models list that now contains the values 
added during the print_models call.
The changes made to completed_models in the print_models function are preserved and reflected in the show_completed_models 
function call. This is because both functions are using the same list object in memory. Yes, the second function (show_completed_models) 
uses the same completed_models list that was modified by the first function (print_models)
Same List Object: The completed_models list is the same object in both function calls. Any changes made to this list in print_models
are  reflected in show_completed_models. List Modification: Modifications to completed_models in print_models will be visible to
show_completed_models because they operate on the same list reference."""

# PREVENTING A FUNCTION FROM MODIFYING A LIST #
""" Sometimes you’ll want to prevent a function from modifying a list. For example, say that you start with a list of unprinted designs
and write a function to move them to a list of completed models, as in the previous example. You may decide that even though you’ve
printed all the designs, you want to keep the original list of unprinted designs for your records. But because you moved all the design
names out of unprinted_designs, the list is now empty, and the empty list is the only version you have; the original is
gone. In this case, you can address this issue by passing the function a copy of the list, not the original. Any changes the function
makes to the list will affect only the copy, leaving the original list intact. You can send a copy of a list to a function like this:

 # function_name(list_name[:]) # use this in function call not def #

The slice notation [:] makes a copy of the list to send to the function. If we didn’t want to empty the list of unprinted designs 
in printing_models.py, we could call print_models() like this:

# print_models(unprinted_designs[:], completed_models) # this is a function call use slice in function call not def #

The function print_models() can do its work because it still receives the names of all unprinted designs. But this time it uses a
copy of the original unprinted designs list, not the actual unprinted_designs list. The list completed _models will fill up with the 
names of printed models like it did before, but the original list of unprinted designs will be unaffected by the function. Even though
you can preserve the contents of a list by passing a copy of it to your functions, you should pass the original list to functions unless
you have a specific reason to pass a copy. It’s more efficient for a function to work with an existing list, because this avoids using the
time and memory needed to make a separate copy. This is especially true when working with large lists."""

# PASSING AN ARBITRARY NUMBER OF ARGUMENTS #
"""Sometimes you won’t know ahead of time how many arguments a function needs to accept. Fortunately, Python allows a function to 
collect an arbitrary number of arguments from the calling statement. For example, consider a function that builds a pizza. It
needs to accept a number of toppings, but you can’t know ahead of time how many toppings a person will want. The function in the 
following example has one parameter, *toppings, but this parameter collects as many arguments as the calling line provides:"""

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

"""The asterisk in the parameter name *toppings tells Python to make a tuple called toppings, containing all the values this
function receives. The print() call in the function body produces output showing that Python can handle a function call with one
value and a call with three values. It treats the different calls similarly. Note that Python packs the arguments into a
tuple, even if the function receives only one value:"""

# def make_pizza(*toppings):
#     """Summarize the pizza we are about to make."""
#     print('\nMaking a pizza with the following toppings:')
#     for topping in toppings:
#         print(f'- {topping}')
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS #
"""If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number of arguments
must be placed last in the function definition. Python matches positional and keyword arguments first and then collects any remaining 
arguments in the final parameter. For example, if the function needs to take in a size for the pizza, that parameter must come before 
the parameter *toppings:"""

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print(f'\nMaking a {size}- inch pizza with the following toppings:')
#     for topping in toppings:
#         print(topping)
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""In the function definition, Python assigns the first value it receives to the parameter size. All other values that come after are 
stored in the tuple toppings. The function calls include an argument for the size first, followed by as many toppings as needed."""

# NOTE= You’ll often see the generic parameter name *args, which collects arbitrary positional arguments like this.
# In Python, *args is used to allow a function to accept an arbitrary number of positional arguments. This is useful when you
# don't know in advance how many arguments will be passed to the function.

# def greet(*args):       # YOU CAN USE ANY PARAMETER IN PLACE OF *ARGS #
#     for name in args:
#         print(f'Hello, {name}!')
#
# greet('Pradeep', 'Rakesh', 'Sai Kumar')
# *args in the Function Definition: The *args in def greet(*args): tells Python to collect any positional arguments into a tuple named args.
# Arbitrary Functions:
# Arbitrary functions are those that can accept any number of arguments due to the use of *args. This makes them flexible when
# you don't know how many arguments will be provided.

"""In programming, "arbitrary" typically means that the value or number of items is not fixed or predetermined; instead,
 it can be any value or amount. When we say that a function can accept an arbitrary number of arguments, we mean that the function
is designed to handle any number of inputs, without a specific limit."""

# USING ARBITRARY KEYWORD ARGUMENTS #
"""Sometimes you’ll want to accept an arbitrary number of arguments, but you won’t know ahead of time what kind of information 
will be passed to the function. In this case, you can write functions that accept as many key-value pairs as the calling statement provides.
One example involves building user profiles: you know you’ll get information about a user, but you’re not sure 
what kind of information you’ll receive"""

# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
# user_profile = build_profile('albert', 'einstein',
#                           location= 'princeton',
#                           field = 'physics')
# print(user_profile)

""""The double asterisks before the parameter **user_info cause Python to create a dictionary called user_info containing all the
extra name-value pairs the function receives. Within the function, you can access the key-value pairs in user_info just as you would 
for any dictionary"""

"""Function Definition:
def build_profile(first, last, **user_info)::
first and last are required positional parameters for the function.
**user_info is a special parameter that allows the function to accept any number of additional keyword arguments. 
These arguments are collected into a dictionary named user_info

Building the Dictionary:
user_info['first_name'] = first:
This line adds an entry to the user_info dictionary with the key 'first_name' and the value of the first parameter.
user_info['last_name'] = last:
This line adds an entry to the user_info dictionary with the key 'last_name' and the value of the last parameter

Return Statement:
return user_info:
The function returns the user_info dictionary, which now includes the first name, last name, and any other information provided via 
keyword arguments.

Calling build_profile:
'albert' and 'einstein':
These are passed as the values for first and last, respectively.
location='princeton' and field='physics':
These are additional keyword arguments and are captured in the user_info dictionary as {'location': 'princeton', 'field': 'physics'}.

Inside the Function:
The user_info dictionary inside the function is initially {'location': 'princeton', 'field': 'physics'}.
After adding 'first_name' and 'last_name', it becomes:

{
    'location': 'princeton',
    'field': 'physics',
    'first_name': 'albert',
    'last_name': 'einstein'
}

Returning the Result:
The function returns this updated dictionary, and it’s assigned to the variable user_profile.

print(user_profile):
This prints the contents of the user_profile dictionary.
NOTE= You’ll often see the parameter name **kwargs(keywords arguments used to collect nonspecific keyword arguments.
Collecting Nonspecific Keyword Arguments:
When a function is defined with **kwargs, it can accept keyword arguments that were not explicitly defined in the function's parameter
list. These arguments are collected into a dictionary where the keys are the argument names and the values are the argument values.

#  return user_info #
This line tells the function to return the user_info dictionary back to the place where the function was called.
The return user_info statement sends this dictionary back to the variable user_profile.
Now, user_profile holds the value of the dictionary returned by build_profile() user_profile Holds the Returned Value. 
Before the Function Call: user_profile has no value. After the Function Call: The function build_profile() returns a dictionary,
and the variable user_profile is assigned this returned dictionary.
when you define a function that accepts both positional arguments and keyword arguments, you need to call the function with the
positional arguments first, followed by the keyword arguments

#IMPORTANT #  ** (Double Asterisks):
When you use ** before a parameter in a function definition, it collects keyword arguments into a dictionary. The keyword arguments are the 
ones that are passed  in the form of key=value pairs.

* (Single Asterisk):
When you use * before a parameter, it collects positional arguments into a tuple. These are the arguments that are passed
without explicit keys. """

# STORING YOU FUNCTIONS IN MODULES #
# storing your functions in a separate file called a module and then importing that module into your main program An import
# statement tells Python to make the code in a module available in the currently running program file.

# IMPORTING AN ENTIRE MODULE #
"""To start importing functions, we first need to create a module. A module is a file ending in .py that contains the code you want
to import into your program. Let’s make a module that contains the function make_pizza(). To make this module, we’ll remove everything
from the file pizza.py except the function make_pizza():"""

# MAKE A SEPARATE MODULE(FILE) IN SAME DIRECTORY CALLED PIZZA.PY AND PASTE BELOW CODE IN THAT MODULE(FILE) #

# def make_pizza(size, *toppings):
#     """Summarize the pizza we are about to make"""
#     print(f'\nMaking a {size}-inch pizza with the following toppings:')
#     for topping in toppings:
#         print(f'-{topping}')

"""Now we’ll make a separate file called making_pizzas.py in the same directory as pizza.py. This file imports the module 
we just created and then makes two calls to make_pizza():"""

# IN THE SAME DIRECTORY CREATE A NEW FILE CALLED MAKING_PIZZAS.PY THIS IS OUR CURRENT WORKING PYTHON FILE AND PASTE BELOW CODE #
# import pizza
# pizza.make_pizza(16, 'pepperoni')
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

"""When Python reads this file, the line import pizza tells Python to open the file pizza.py and copy all the functions from it into
this program. You don’t actually see code being copied between files because Python copies the code behind the scenes, just before the 
program runs. All you need to know is that any function defined in pizza.py will now be available in making_pizzas.py. To call a function
from an imported module, enter the name of the module you imported, pizza, followed by the name of the function, make _pizza(), separated by 
a dot . This code produces the same output as the original program that didn’t import a module: This first approach to importing, in which you 
simply write import followed by the name of the module, makes every function from the module available in your program. If you use this kind of
import statement to import an entire module named module_name.py, each function in the module is available through the following syntax:
module_name.function_name()"""

# IMPORTING A SPECIFIC FUNCTIONS #

# You can also import a specific function from a module. Here’s the general syntax for this approach:
# from module_name import function_name
# You can import as many functions as you want from a module by separating each function’s name with a comma:
# from module_name import function_0, function_1, function_2
# The making_pizzas.py example would look like this if we want to import just the function we’re going to use:

# from pizza import make_pizza     # FROM IS A KEYWORD #
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#  """ With this syntax, you don’t need to use the dot notation when you call a function. Because we’ve explicitly imported the
# function make_pizza() in the import statement, we can call it by name when we use the function"""

# USING AS TO GIVE A FUNCTION AN ALIAS ( AS IS A KEYWORD) TO SEE RESERVED KEYWORDS USE BELOW CODE #

# import keyword
# print(keyword.kwlist)

"""If the name of a function you’re importing might conflict with an existing name in your program, or if the function name is long,
you can use a short, unique alias—an alternate name similar to a nickname for the function. You’ll give the function this special 
nickname when you import the function. Here we give the function make_pizza() an alias, mp(), by importing make _pizza as mp. The as 
keyword renames a function using the alias you provide:"""

# from pizza import make_pizza as mp
# mp(16, 'pepperoni')
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')
"""The import statement shown here renames the function make_pizza() to mp() in this program. Anytime we want to call make_pizza() 
we can simply write mp() instead, and Python will run the code in make_pizza() while avoiding any confusion with another make_pizza() 
function you might have written in this program file. The general syntax for providing an alias is:
# from module_name import function_name as fn # """

# USING AS TO GIVE A MODULE AN ALIAS #

"""You can also provide an alias for a module name. Giving a module a short alias, like p for pizza, allows you to call the module’s 
functions more quickly. Calling p.make_pizza() is more concise than calling pizza.make_pizza():"""
# import pizza as p
# p.make_pizza(16, 'pepperoni')
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""The module pizza is given the alias p in the import statement, but all of the module’s functions retain their original names.
Calling the functions by writing p.make_pizza() is not only more concise than pizza.make_pizza(), but it also redirects your attention 
from the module name and allows you to focus on the descriptive names of its functions. These function names, which clearly tell you what 
each function does, are more important to the readability of your code than using the full module name. 
The general syntax for this approach is: # import module_name as mn #"""

# IMPORTING ALL FUNCTIONS IN A MODULE #

# You can tell Python to import every function in a module by using the asterisk (*) operator:
# from pizza import *
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
"""The asterisk in the import statement tells Python to copy every function from the module pizza into this program file. Because 
every function is imported, you can call each function by name without using the dot notation. However, it’s best not to use this 
approach when you’re working with larger modules that you didn’t write: if the module has a function name that matches an existing
name in your project, you can get unexpected results. Python may see several functions or variables with the same name, and instead 
of importing all the functions separately, it will overwrite the functions. The best approach is to import the function or functions 
you want, or import the entire module and use the dot notation. This leads to clear code that’s easy to read and understand. I include 
this section so you’ll recognize import statements like the following when you see them in other people’s code:
# from module_name import * # """

# STYLING FUNCTIONS #
"""You need to keep a few details in mind when you’re styling functions. Functions should have descriptive names, and these names 
should use lowercase letters and underscores. Descriptive names help you and others understand what your code is trying to do. Module
names should use these conventions as well. Every function should have a comment that explains concisely what the function does. This 
comment should appear immediately after the function definition and use the docstring format. In a well-documented function, other 
programmers can use the function by reading only the description in the docstring. They should be able to trust that the code works as
described, and as long as they know the name of the function, the arguments it needs, and the kind of value it returns, they should be 
able to use it in their programs. If you specify a default value for a parameter, no spaces should be used
on either side of the equal sign:  # def function_name(parameter_0, parameter_1='default value') # 
The same convention should be used for keyword arguments in function calls: # function_name(value_0, parameter_1='value') #
PEP 8 (https://www.python.org/dev/peps/pep-0008) recommends that you limit lines of code to 79 characters so every line is visible in
a reasonably sized editor window. If a set of parameters causes a function’s definition to be longer than 79 characters, press ENTER after
the opening parenthesis on the definition line. On the next line, press the TAB key twice to separate the list of arguments from the body
of the function, which will only be indented one level. Most editors automatically line up any additional lines of arguments to
match the indentation you have established on the first line:"""
# def function_name(
#         parameter_0, parameter_1, parameter_2,
#         parameter_3, parameter_4, parameter_5):
#     function body...
"""If your program or module has more than one function, you can separate each by two blank lines to make it easier to see where 
one function ends and the next one begins. All import statements should be written at the beginning of a file. The only exception is if
you use comments at the beginning of your file to describe the overall program."""
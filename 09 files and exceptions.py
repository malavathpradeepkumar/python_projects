"""You’ll learn about exceptions, which are special objects Python creates to manage errors that arise while a program is running.
You’ll also learn about the json module, which allows you to save user data so it isn’t lost when your program stops running"""

# READING FROM A FILE #

"""you can write a program that reads in the contents of a text file and rewrites the file with formatting that allows a browser to display it.
When you want to work with the information in a text file, the first step is to read the file into memory. You can then work through all of 
the file’s contents at once or work through the contents line by line."""

# READING THE CONTENTS OF A FILE #  FILE NAME IS # pi_digits.txt # SAVE IN SAME PYTHON FOLDER #

"""To begin, we need a file with a few lines of text in it. Let’s start with a file that contains pi to 30 decimal places, with 10 decimal places
per line: Pi (π) is a mathematical constant Pi is an irrational number, meaning its decimal representation goes on forever without repeating."""

# from pathlib import Path   # pathlib IS MODULE AND Path IS CLASS STARTING WITH CAPITALIZE #
# path = Path('pi_digits.txt') # lowercase path is variable also indirect instance The name you use to reference this instance is
#                                                                                               the variable path. #
# contents = path.read_text()  # contents is a variable #
# print(contents)

"""The contents variable will hold the string: ("3.1415926535\n8979323846\n2643383279" THIS IS A SINGLE STRING IN PYTHON) we use the read_text() 
method to read the entire contents  of the file . The contents of the file are returned as a single string, which we assign to 
the variable contents."""

"""pathlib is a module in Python that provides classes to handle and operate on filesystem paths in an object-oriented manner.
A path is the exact location of a file or folder on a system. Path is a class within this module that allows you to create and manipulate 
filesystem paths."""

"""Path('pi_digits.txt') initializes a new Path object. The argument 'pi_digits.txt' specifies the file name or path relative to the 
current working directory. The path variable now holds this Path object, which can be used to interact with the file system.
Instance Creation:
A new Path object is created in memory, which holds the path 'pi_digits.txt'.
The instance is fully initialized and ready to be used.
Variable Assignment:

The reference to this new Path object is assigned to the variable path.
path now refers to this instance and can be used to call methods on it, such as read_text()."""

"""Instance Creation:

Code: Path('pi_digits.txt')
This line of code creates a new instance of the Path class.
Instance Name:

The instance itself does not have a name; rather, it is a reference to an object created by the Path class constructor.
The name you use to reference this instance is the variable path."""
# """pathlib It provides a set of classes and methods for working with file and directory paths """
""" read_text() method of the Path object to read the entire contents of the file into a string.
read_text() is a convenient method provided by pathlib to read the contents of a file as a string. It assumes the file is encoded 
in UTF-8 by default. """

"""Understanding Instances, Classes, and Arguments
# my_new_car = Car('audi') # 

Car: This is the class. A class is a blueprint for creating objects. It defines the attributes(data i wrote) and behaviors(methods i wrote) 
that the objects created from the class will have.

my_new_car: This is an instance of the Car class. An instance is a specific object created from a class. It has the attributes and 
behaviors defined by the class, and it holds actual data.

audi': This is an argument passed to the Car class’s __init__ method, when creating the my_new_car instance. It provides the data needed to 
initialize the new instance. In this case, it might be used to set the make attribute of the Car object. def __init__(self, make):
 
 path: This is an instance of the Path class. It represents a specific path to a file or directory—in this case, 'pi_digits.txt'.
 'pi_digits.txt': This is an argument passed to the Path class’s constructor to initialize the path instance. It specifies the path you are 
 referring to pi_digits.txt': This is an argument passed to the Path class’s constructor to initialize the path instance. It specifies the path 
 you are referring to. path is an instance of the Path class, holding the path 'pi_digits.txt' and providing methods to work with this path."""

"""The only difference between this output and the original file is the extra blank line at the end of the output. The blank line appears 
because read_text() returns an empty string when it reaches the end of the file; this empty string shows up as a blank line"""

# from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()
# print(contents)

"""When you print the string contents, if it ends with a newline, the print() function adds its own newline after the string. 
This results in an extra blank line appearing at the end of the output."""

# METHOD CHAINING #
# contents = path.read_text().rstrip()
"""This line tells Python to call the read_text() method on the file we’re working with. Then it applies the rstrip() method to the 
string that read _text() returns. The cleaned-up string is then assigned to the variable contents. This approach is called method chaining, 
and you’ll see it used often in programming."""

 # RELATIVE FILE PATH #

 # """There are two main ways to specify paths in programming. A relative file path tells Python to look for a given location relative
# to the directory where the currently running program file is stored"""
# Relative Path: A path that is relative to the current working directory.

# CREATE A SUB DIRECTORY IN CURRENT WORKING DIRECTORY NAME IS #minipython#
# If the minipython directory is not inside the python directory (or wherever your script is running from), the relative path won't find
# the file, hence the "No file exists" error.

# from pathlib import Path
# path = Path('minipython/pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

# ABSOLUTE PATH #

# from pathlib import Path
# path = Path('/home/thor/python/minipython/pi_digits.txt')
# contents = path.read_text().rstrip()
# print(contents)

# """ IMPORTANT NOTE
# Windows systems use a backslash (\) instead of a forward slash (/) when displaying file paths, but you should use forward slashes in
# your code, even on Windows. The pathlib library will automatically use the correct representation of the path when it
# interacts with your system, or any user’s system."""

# ACCESSING A FILE'S LINES #

""" You might want to read through a file of weather data and work with any line that includes the word sunny in the description of that day’s 
weather. In a news report, you might look for any line with the tag <headline> and rewrite that line with a specific kind of formatting.
You can use the splitlines() method to turn a long string into a set of lines, and then use a for loop to examine each line from a file, 
one at a time:"""

# from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# for line in lines:
#     print(line)

"""We start out by reading the entire contents of the file, as we did ear-lier . If you’re planning to work with the individual lines 
in a file, you don’t need to strip any whitespace when reading the file. The splitlines() method returns a list of all lines in the file, 
and we assign this list to the variable lines . We then loop over these lines and print each one:"""

# WORKING WITH A FILE'S CONTENTS #

"""After you’ve read the contents of a file into memory, you can do whatever you want with that data, so let’s briefly explore the digits 
of pi. First, we’ll attempt to build a single string containing all the digits in the file with no whitespace in it:"""

""""Hello World       # FOR EXAMPLE THIS IS TEXT FILE 
This is a test file.   # DIFFERENCE BETWEEN split() and splitlines() #
It has multiple lines.
Python is fun!"""

""" Using split()
The split() method in Python is used to split a string into words (or based on any delimiter). By default, it splits on whitespace 
(spaces, tabs, or newlines)."""

# Result using split(): ['Hello', 'World', 'This', 'is', 'a', 'test', 'file.', 'It', 'has', 'multiple', 'lines.', 'Python', 'is', 'fun!']

""" Using splitlines()
The splitlines() method splits a string into lines. It does this by recognizing the newline characters (\n) that separate lines in the file."""

# Result using splitlines(): ['Hello World', 'This is a test file.', 'It has multiple lines.', 'Python is fun!']

# from pathlib import Path
# path = Path('pi_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line
# print(pi_string)

""" pi_string = ''
Explanation: This initializes an empty string pi_string that will later hold the entire content of the file without line breaks.
Why Use It?: You are setting up an empty string to concatenate all lines of the file content into one continuous string without 
any newlines.  pi_string = '' (Why initialize an empty string?) What is it?: This is the initialization of a variable pi_string 
as an empty string (''). Why give an empty string?: You need to give pi_string an initial value (in this case, an empty string) so 
that you have a starting point for concatenating the lines. Without this, Python wouldn’t know what pi_string is when you try to add to it.
What happens if you don't give an empty string? If you don't initialize pi_string, Python will raise an error: UnboundLocalError. 
This is because you're trying to use and modify a variable (pi_string) that has not been assigned a value.
"""

""" pi_string += line
Explanation: This appends each line from the file (without line breaks) to the pi_string variable.
Why Use It?: This is how you build the continuous string by concatenating each line in the file. The += operator is used for string 
concatenation in Python. It appends each line to the existing value of pi_string

pi_string += line (Full form and how it works)  pi_string = pi_string + line  # THIS IS A FULL OF PI_STRING #
How it works:

This expression takes the current value of pi_string, adds (+) the line (a string) to it, and then stores the result back in pi_string.
Essentially, you're building up pi_string by appending each line from the file to it, one by one. Each iteration of the loop concatenates 
the current line to the existing string."""

"""What happens if you omit the + sign:
If you write pi_string = line (omitting the + sign), the variable pi_string will be assigned the value of line in every iteration of 
the loop. This means that during each iteration, the previous value of pi_string will be replaced by the current line. So, when the loop 
finishes, only the last line will be stored in pi_string, because every previous value has been overwritten."""

# THE VARIABLE PI_STRING CONTAINS WHITE SPACE THAT WAS ON THE LEFT SIDE #
# --snip--
# for line in lines:
#     pi_string += line.lstrip()
# print(pi_string)
# print(len(pi_string))

"""When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value 
in a numerical context, you’ll have to convert it to an integer using the int() function or a float using the float() function."""

# LARGE FILES: ONE MILLION FILES #

"""If we start with a text file that contains pi to 1,000,000 decimal places, instead of just 30, we can create a single string containing 
all these digits.  We’ll also print just the first 50 decimal places"""

# from pathlib import Path
# path = Path('pi_million_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
# print(f'{pi_string[:52]}...')
# print(len(pi_string))

# IS YOUR BIRTHDAY CONTAINED IN Pi ?

"""if someone’s birthday appears anywhere in the first million digits of pi. We can do this by expressing each birthday as a string of digits 
and seeing if that string appears anywhere in pi_string:"""

# from pathlib import Path
# path = Path('pi_million_digits.txt')
# contents = path.read_text()
# lines = contents.splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
# birthday = input("Enter you birthday in form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birth day doesn't appear in the first million digits of pi!")

# WRITING TO A FILE #

# One of the simplest ways to save data is to write it to a file You can also write programs that read the text back into memory
# and work with it again later.

# WRITING A SINGLE LINE #

# Once you have a path defined, you can write to a file using the write_text() method.

# from pathlib import Path
# path = Path('programming.txt')    # YOU DON'T NEED TO CREATE A FILE IT WILL CREATE AUTOMATICALLY #
# path.write_text('I love programming')

# The write_text() method takes a single argument: the string that you want to write to the file. Python can only write strings to a
# text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using
# the str() function.  # ask this letter to chat gpt #

# WRITING MULTIPLE LINES #

"""The write_text() method does a few things behind the scenes. If the file that path points to doesn’t exist, it creates that file. 
Also, after writing the string to the file, it makes sure the file is closed properly. Files that aren’t closed properly can lead to missing 
or corrupted data. To write more than one line to a file, you need to build a string containing the entire contents of the file, and then 
call write_text() with that string. Let’s write several lines to the programming.txt file:"""

# from pathlib import Path
# contents = "I love programming.\n"
# contents += "I love creating a new games.\n"
# contents += "I also love working with data.\n"
# path = Path('programming.txt')
# path.write_text(contents)

"""Be careful when calling write_text() on a path object. If the file already exists, write_text() will erase the current contents of 
the file and write new contents to the file. Later in this chapter, you’ll learn to check whether a file exists using pathlib."""

# EXCEPTIONS #

"""Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs that 
makes Python unsure of what to do next, it creates an exception object. If you write code that handles the exception, the program will 
continue running. If you don’t handle the exception, the program will halt and show a traceback, which includes a report of the exception 
that was raised. Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python 
what to do if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong. 
Instead of tracebacks, which can be confusing for users to read, users will see friendly error messages that you’ve written."""

# HANDLING THE ZeroDivisionError EXCEPTION #

# You probably know that it’s impossible to divide a number by zero.
# print(5/0)

"""In Python, exceptions are indeed classes. # ZeroDivisionError When an error occurs, Python raises an exception object, and the traceback 
gives details about the error  # ZeroDivisionError # This is the name of the exception class. Python defines a hierarchy of built-in exception 
classes, and ZeroDivisionError is a specific subclass of ArithmeticError, which is itself a subclass of the base class Exception.
# division by zero # This is the message or description associated with the exception, which provides more information about what went wrong.
 # only this line from book The error reported in the traceback, ZeroDivisionError, is an exception object""" #

# USING TRY_EXCEPT BLOCKS #

"""When you think an error may occur, you can write a try-except block to handle the exception that might be raised. You tell Python 
to try running some code, and you tell it what to do if the code results in a particular kind of exception."""

# try:
#     print(4/0)    # actually 5 for better understand 4.
# except ZeroDivisionError:
#     print("you can't divide by zero!")

"""We put print(5/0), the line that caused the error, inside a try block. If the code in a try block works, Python skips over the except 
block. If the code in the try block causes an error, Python looks for an except block whose error matches the one that was raised, and runs 
the code in that block. In this example, the code in the try block produces a ZeroDivisionError, so Python looks for an except block telling 
it how to respond. Python then runs the code in that block, and the user sees a friendly error message instead of a traceback"""

# USING EXCEPTIONS TO PREVENT CRASHES #

"""Handling errors correctly is especially important when the program has more work to do after the error occurs. This happens 
often in programs that prompt users for input. If the program responds to invalid input appropriately, it can prompt for more valid 
input instead of crashing."""

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond_number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

# WHILE DIVIDING IF YOU ENTER 5/0 IT CAUSES ZERO-DIVISION ERROR.

"""In this code, the while True: loop creates an infinite loop, meaning the code inside the loop will keep running until a break 
statement is encountered. Loop Start: The while True: ensures that the loop runs indefinitely, as True is always a valid condition.
First Number Input: The code prompts the user to input a value for first_number. If the user types 'q', the loop is exited using break.
Otherwise, the loop continues to the next step. Division Operation: The values of first_number and second_number are converted to integers 
and divided. The result is printed, and the loop repeats from the start, asking for new input. """

"""FROM BOOK so asking it to divide by zero causes it to crash: It’s bad that the program crashed, but it’s also not a good idea to let
users see tracebacks. and in a malicious setting, attackers will learn more than you want them to"""

# THE ELSE BLOCK #

"""The error occurs on the line that performs the division, so that’s where we’ll put the try-except block. This example also includes an 
else block. Any code that depends on the try block executing successfully goes in the else block"""

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond_number: ")
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# WHY TRY AND EXCEPT BLOCK INSIDE THE LOOP #

"""Why it must be inside the loop: 
Error Handling for Each Input: Every time the user enters numbers, there's a possibility that they could enter 0 for the second number, 
which would cause a ZeroDivisionError. By placing the try and except blocks inside the loop, the program can catch this error each time 
the user enters new numbers and prevent the program from crashing. If Placed Outside the Loop: If you put the try and except blocks outside 
the loop, only one attempt at division would be protected from errors. The program would crash as soon as an error occurs, and the loop 
wouldn’t continue because the error wouldn't be caught for subsequent inputs."""

# THIS CODE IS FROM CHAT GPT #
# try:
#     while True:
#         first_number = input("\nFirst number: ")
#         if first_number == 'q':
#             break
#         second_number = input("\nSecond_number: ")
#         if second_number == 'q':
#             break
#
#         answer = int(first_number) / int(second_number)
#         print(answer)
# except ZeroDivisionError:
#     print("You can't divide by 0!")

"""As soon as the user enters 0 for second_number, a ZeroDivisionError will occur, and the program will immediately jump to the except 
block. The loop will not continue, and the user won’t be able to input any more numbers after that error"""

"""Why the try: block is first:
Global Error Handling: By placing the try block before the while True: loop, you're telling Python to monitor everything inside the loop 
for specific errors (like ZeroDivisionError). This allows you to handle the error for any part of the loop that could cause the exception.
What happens inside the try: block: Input Gathering: Inside the loop, the program asks the user to enter first_number and second_number.
The if first_number == 'q' and if second_number == 'q' conditions allow the user to exit the loop by typing 'q'. Division Operation:
The program attempts to divide first_number by second_number using the expression int(first_number) / int(second_number).
If the user enters 0 for second_number, this division would raise a ZeroDivisionError because division by zero is not allowed 
in Python. Error Catching: If the division by zero occurs, Python immediately stops executing the code in the try block and jumps to the 
except block. The except ZeroDivisionError block catches the error and prints "You can't divide by 0!" to notify the user without crashing 
the program."""

"""FROM BOOK We ask Python to try to complete the division operation in a try block , which includes only the code that might cause an error. 
Any code that depends on the try block succeeding is added to the else block. In this case, if the division operation is successful, we use the 
else block to print the result . The except block tells Python how to respond when a ZeroDivisionError arises 2. If the try block doesn’t succeed 
because of a division-by-zero error, we print a friendly message telling the user how to avoid this kind of error.
The program continues to run, and the user never sees a traceback: The only code that should go in a try block is code that might cause an
exception to be raised. Sometimes you’ll have additional code that should run only if the try block was successful; this code goes in the 
else block. The except block tells Python what to do in case a certain exception arises when it tries to run the code in the try block."""

# HANDLING THE FileNotFoundError EXCEPTION #

"""Let’s try to read a file that doesn’t exist. The following program tries to read in the contents of Alice in Wonderland, but I haven’t 
saved the file alice.txt in the same directory as alice.py:"""

# from pathlib import Path
# path = Path('alice.txt')
# contents = path.read_text(encoding= 'utf-8')

"""It’s often best to start at the very end of the traceback. On the last line, we can see that a FileNotFoundError exception was raised . 
This is important because it tells us what kind of exception to use in the except block that we’ll write. The rest of the traceback shows 
some code from the libraries that are involved in opening and reading from files. You don’t usually need to read through or understand all 
of these lines in a traceback. To handle the error that’s being raised, the try block will begin with the line that was identified as problematic 
in the traceback. In our example, this is the line that contains read_text():"""

"""UTF-8 is one of the most common encodings and is able to represent all characters in the Unicode character set. When you specify 
encoding='utf-8', you are telling Python to interpret the file contents using the UTF-8 encoding scheme. Without specifying an encoding, 
Python uses a default encoding, which depends on the system's locale. Specifying encoding='utf-8' ensures that the file is read as UTF-8, 
avoiding potential encoding issues if your file includes non-ASCII characters."""

# from pathlib import Path
# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding= 'utf-8')
# except FileNotFoundError:
#     print(f'Sorry, the file {path} does not exist.')

"""How to recognize which line goes into the try block: Look for the line that triggers the exception in the traceback. In your traceback, 
the line that raises the error is  # contents = path.read_text(encoding='utf-8') # This is the line you should place in the try block because 
it’s trying to read the file, which can result in a FileNotFoundError."""

# ANALYZING TEXT #

# from pathlib import Path
# path = Path('alice.txt')
# try:
#     contents = path.read_text(encoding= 'utf-8')
# except FileNotFoundError:
#     print(f'Sorry, the file {path} does not exist.')
# else:
#     counts the approximate number of words in the file:
    # words = contents.split()
    # num_words = len(words)
    # print(f'The file {path} has about {num_words} words.')

"""We take the string contents, which now contains the entire text of Alice in Wonderland as one long string, and use  split() to produce a list 
of all the words in the book . Using len() on this list  gives us a good approximation of the number of words in the original text."""

# WORKING WITH MULTIPLE FILES #

"""Let’s add more books to analyze, but before we do, let’s move the bulk of this program to a function called count_words(). This will make 
it easier to run the analysis for multiple books:"""

# from pathlib import Path
# def count_words(path):   # `path` is a parameter here #
#     """Count the approximate number of words in a file."""
#     try:
#         contents = path.read_text(encoding= 'utf-8')  # Unicode Transformation Format - 8-bit. #
#     except FileNotFoundError:
#         print(f'Sorry, the file {path} does not exist.')
#     else:
#         Counts the approximate number of words in the file.
        # words = contents.split()
        # num_words = len(words)
        # print(f'The file {path} has about {num_words} words.')
# path = Path('alice.txt')
# count_words(path)  # path` is an argument here, the value passed to the function #

"""count_words is a function, not a method, because it is defined outside the context of a class. A function, on the other hand, is a standalone 
block of code that performs a specific task and can be called from anywhere in the program.
Methods are defined inside classes and operate on instances of that class."""

""". What is encoding?
In the method path.read_text(encoding='utf-8'), the encoding parameter specifies how the text in the file is represented internally by the 
computer. Files are stored as bytes, and these bytes need to be converted to characters when read as text. The encoding tells Python how to 
interpret these bytes to display human-readable characters correctly. In simple terms, the encoding is like a "translator" that converts 
between bytes (stored in the file) and characters (that you can read). Different languages and symbols are represented differently depending 
on the encoding used."""

# A MISSING FILE #

"""Now we can write a short loop to count the words in any text we want to analyze. We do this by storing the names of the files we want to 
analyze in a list, and then we call count_words() for each file in the list. We’ll try to count the words for Alice in Wonderland, Siddhartha, 
Moby Dick, and Little Women, which are all available in the public domain. I’ve intentionally left siddhartha.txt out of the directory containing 
word_count.py, so we can see how well our program handles a missing file:"""

# from pathlib import Path
#
# def count_words(filename):   # # filename = Path('alice.txt') #
#     """Count the approximate number of words in a file."""
#     try:
        # 'filename' is now the Path object passed to the function
        # contents = filename.read_text(encoding='utf-8')  # # Reads content from 'alice.txt'
    # except FileNotFoundError:
    #     print(f"Sorry, the file {filename} does not exist.")
    # else:
        # Counts the approximate number of words in the file.
        # words = contents.split()
        # num_words = len(words)
        # print(f"The file {filename} has about {num_words} words.")

# List of filenames
# filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

# Loop through the filenames and create a Path object for each
# for filename in filenames:
#     folder = Path(filename)   # Create a Path object for each filename
#     count_words(folder)       # Pass the Path object to the function

# EXPLAIN ABOUT LOOP   filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
""" First Iteration (Handling alice.txt):
The loop starts with the first file: 'alice.txt'. NOW # filename = 'alice.txt' # filename is just a string representing the file 'alice.txt'.
Convert filename to a Path object:  # folder = Path(filename) # folder is now a Path object that represents the path to 'alice.txt'. This allows 
us to use methods like read_text(). Call the count_words() function: # count_words(folder) # Here, we pass the folder object 
(which represents 'alice.txt') to the count_words function. Inside the function, the parameter filename (inside the function definition) 
will now refer to the Path object for 'alice.txt'.  The filename inside the function now refers to Path('alice.txt').
The function attempts to read the text from 'alice.txt' using the read_text() method. If successful, it splits the text into words, counts them, 
and prints how many words are in the file.

Second Iteration (Handling siddhartha.txt):
Call the count_words() function: #  count_words(folder) # Inside the count_words() function: The filename parameter now refers to 
Path('siddhartha.txt'), and the same process repeats: read the text, split it into words, count them, and print the result.   

Argument:
When you call count_words(folder), folder is the argument. It is the actual Path object (e.g., Path('siddhartha.txt')) that gets passed 
to the function. Inside the Function: When you call count_words(Path('siddhartha.txt')), the filename parameter inside the function will be 
assigned the value of Path('siddhartha.txt'). So, filename inside the function refers to the Path object for 'siddhartha.txt'.
  
  # AS SAME AS REPEAT FOR THIRD AND FORTH FILES #

What is a path object? An object that may be used to locate a file in a file system Explanation of the Path Object:
Class Name:
Path is the class name provided by the pathlib module.
Instance:
folder is an instance of the Path class. It represents a specific file or directory path in a way that allows you to perform various 
operations on it. Instance Variable: folder folder is a variable holding an instance of the Path class. This instance represents the 
path to a file or directory specified by filename. 

For example:
filename = 'siddhartha.txt'
folder = Path(filename)
folder is now a Path object representing the path to 'siddhartha.txt'. """

# FAILING SILENTLY #

"""In the previous example, we informed our users that one of the files was unavailable. But you don’t need to report every exception you catch.
Sometimes, you’ll want the program to fail silently when an exception occurs and continue on as if nothing happened. To make a program fail
silently, you write a try block as usual, but you explicitly tell Python to do nothing in the except block. Python has a pass statement that 
tells it to do nothing in a block:"""

# def count_words(filename):
#     """Counts the approximate number of words in a file."""
#     try:
#         --snip--
#     except FileNotFoundError:
#         pass
#     else:
#         --snip--

""" The only difference between this listing and the previous one is the pass statement in the except block. Now when a FileNotFoundError 
is raised, the code in the except block runs, but nothing happens. No traceback is produced, and there’s no output in response to the error 
that was raised. Users see the word counts for each file that exists, but they don’t see any indication that a file wasn’t found:"""

  # NOTE WORKING WITH MULTIPLE FILE AND FAILING SILENTLY WE HAVE CHANGED SOME CODE YOU CAN SEE IN THE BOOK THAT CODE FORM CHAT GPT #

# STORING DATA #

"""Many of your programs will ask users to input certain kinds of information. You might allow users to store preferences in a game 
or provide data for a visualization. Whatever the focus of your program is, you’ll store the information users provide in data structures 
such as lists and dictionaries. When users close a program, you’ll almost always want to save the information they entered. A
simple way to do this involves storing your data using the json module. The json module allows you to convert simple Python data structures
into JSON-formatted strings, and then load the data from that file the next time the program runs. You can also use json to share data between 
different Python programs. Even better, the JSON data format is not specific to Python, so you can share data you store in the JSON format 
with people who work in many other programming languages. It’s a useful and portable format, and it’s easy to learn. The JSON 
(JavaScript Object Notation) format was originally developed for JavaScript. However, it has since become a common format used by 
many languages, including Python."""

# USING json.dumps() AND json.loads() #

"""Let’s write a short program that stores a set of numbers and another program that reads these numbers back into memory. The first 
program will use json.dumps() to store the set of numbers, and the second program will use json.loads(). The json.dumps() function takes 
one argument: a piece of data that should be converted to the JSON format. The function returns a string, which we can
then write to a data file:"""

# from pathlib import Path
# import json
# numbers = [2,3,5,7,11,13]
# path = Path('numbers.json')
# contents = json.dumps(numbers)   # json.dumps() is a function #
# path.write_text(contents)

"""contents = json.dumps(numbers)
 The numbers list is serialized (converted) into a JSON-formatted string using json.dumps(). The contents variable now holds the 
 string "[2, 3, 5, 7, 11, 13]". path.write_text(contents) The method write_text() writes the string in contents to the file represented by the 
path object (numbers.json). If the file already exists, its content will be replaced. If the file doesn't exist, it will be created."""

# json.loads () to read the same list back into memory: #

# from pathlib import Path
# import json
# path = Path('numbers.json')
# contents = path.read_text()
# numbers = json.loads(contents)   # here see loads not load if you give load you will get error #
# print(numbers)

# print(type(contents))  # This will show <class 'str'>
# print(type(numbers))  # This will show <class 'list'>  # FIRST READ BELOW LINES #


"""contents = path.read_text()
path.read_text() reads the entire content of the file (numbers.json) as a string. 
What is read? If the file numbers.json contains: [2, 3, 5, 7, 11, 13] Then, contents will store the string: "[2, 3, 5, 7, 11, 13]".
Convert the JSON String Back to a Python List: numbers = json.loads(contents)
json.loads(): This method converts (or "deserializes") a JSON-formatted string into its corresponding Python object.
In this case, contents contains the string "[2, 3, 5, 7, 11, 13]", which represents a list in JSON format. After json.loads(contents) is 
called, the string is converted back into the Python list [2, 3, 5, 7, 11, 13] and assigned to the variable numbers
"""

#  important in this code in print function parenthesis  if you use # contents#  you will get same output when you use numbers why #
"""Scenario 1: Printing contents # print(contents) #
contents holds the JSON-formatted string read from the file.
If numbers.json contains:  [2, 3, 5, 7, 11, 13]
then contents will be:
"[2, 3, 5, 7, 11, 13]"
Output: When you print contents, you'll see the exact JSON string: # THIS LINE IS IMPORTANT #
[2, 3, 5, 7, 11, 13]


Scenario 2: Printing numbers
print(numbers)
numbers is the result of parsing the JSON string with json.loads(). It converts the JSON string into a Python list.
After parsing, numbers will be:  [2, 3, 5, 7, 11, 13]
Output: When you print numbers, you'll see the Python list:  # THIS LINE IS IMPORTANT # [2, 3, 5, 7, 11, 13] """

"""FROM BOOK Since the data
file is just a text file with specific formatting, we can read it with the read_text() method . We then pass the contents of the file 
to json.loads() . This function takes in a JSON-formatted string and returns a Python object (in this case, a list)"""

# SAVING AND READING USER-GENERATED DATA #

"""Saving data with json is useful when you’re working with user-generated data, because if you don’t store your user’s information 
somehow, you’ll lose it when the program stops running."""

# from pathlib import Path
# import json
#
# username = input("what is your name? ")
# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We'll remember when you come back, {username}")

# Now let’s write a new program that greets a user whose name has  already been stored #

# from pathlib import Path
# import json
# path = Path('username.json')
# contents = path.read_text()
# username = json.loads(contents)
# print(f"Welcome back, {username}")

"""We need to combine these two programs into one file. When someone runs remember_me.py, we want to retrieve their username from memory if
possible; if not, we’ll prompt for a username and store it in username.json for next time. We could write a try-except block here to respond 
appropriately if username.json doesn’t exist, but instead we’ll use a handy method from the pathlib module:"""

# from pathlib import Path
# import json
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)

# The exists() method returns True if a file or folder exists and False if it doesn’t.

#  REFACTORING #

# refactoring not only for functions. it covers many areas in python you can ask chatgpt
# Why Refactor?
# Refactoring is done for several reasons:
# Improving Readability: Clean up messy code so it's easier to understand.
# Reducing Complexity: Simplify complex code to make it more manageable.
# Enhancing Maintainability: Make the code easier to maintain and modify.
# Removing Duplications: Eliminate repeated code to follow the "DRY" (Don't Repeat Yourself) principle.
# Optimizing Performance: Refactor code to improve efficiency or reduce resource consumption.
# Preparing for New Features: Simplify code to make it easier to extend or add new features.

"""FROM BOOK you’ll recognize that you could improve the code by breaking it up into a series of functions that have specific jobs. This 
process is called refactoring. Refactoring makes your code cleaner, easier to understand, and easier to extend."""

# from pathlib import Path
# import json
#
#
# def greet_user():
#     """Greet the user by name"""
#     path = Path('username.json')
#
#     Check if the file 'username.json' exists
    # if path.exists():
    #     If the file exists, read its contents (the username)
        # contents = path.read_text()
        # username = json.loads(contents)  # Convert JSON string to Python object (the username)
        #
        # Greet the user with the retrieved username
        # print(f"Welcome back, {username}")
    # else:
    #     If the file doesn't exist, ask for a new username
        # username = input("What is your name? ")
        #
        # Convert the username to a JSON string and save it to 'username.json'
        # contents = json.dumps(username)
        # path.write_text(contents)
 # Function Call    # when you call the function whatever code inside the function will run.
# greet_user()  # this is function call #

"""The reason your function works and greets the user, even though you didn't pass any arguments in the function call or definition, is that 
the function doesn't require any external inputs from the caller. Instead, it works by interacting with a file (username.json) that already 
contains data."""

"""No Arguments Required:
The function doesn't take any arguments because it reads the username from an external file (username.json) rather than from a parameter 
passed to the function. All the required information is handled internally by the function: it checks whether the file exists, reads from it 
if it does, or asks for the user's name if the file is missing."""

"""FROM BOOK This file is a little cleaner, but the function greet_user() is doing more than just greeting the user—it’s also retrieving a 
stored username if one exists and prompting for a new username if one doesn’t. Let’s refactor greet_user() so it’s not doing so many different 
tasks. We’ll start by moving the code for retrieving a stored username to a separate function:"""

# from pathlib import Path
# import json


# 1. Function to get the stored username
# def get_stored_username(path):
    """Get stored username if available."""
    # if path.exists():
    #     contents = path.read_text()  # Read the contents of the file as a string
    #     username = json.loads(contents)  # Parse the string (JSON format) into a Python object
    #     return username  # Return the username if it exists
    # else:
    #     return None  # If the file doesn't exist, return None


# 2. Function to greet the user
# def greet_user():
#     """Greet the user by name."""
#     path = Path('username.json')  # Create a Path object for 'username.json'

    # Try to get the stored username using the helper function
    # username = get_stored_username(path)

    # Check if a username was found
    # if username:
    #     print(f"Welcome back, {username}!")  # Greet the user with the stored username
    # else:
        # If no username is found, ask for a new one
        # username = input("What is your name? ")
        # contents = json.dumps(username)  # Convert the username to JSON format
        # path.write_text(contents)  # Write the new username to 'username.json'
        # print(f"We'll remember you when you come back, {username}!")  # Confirm that the username has been stored


# 3. Call the greet_user function
# greet_user()

"""get_stored_username(path) Function:
This is the refactored helper function that is responsible for retrieving the username from username.json. Purpose: To encapsulate the logic of 
checking if a file exists and reading its contents, separating this logic from the greeting function. Return: If a username is found, it returns 
the username. If not, it returns None. By having this function, the responsibility of fetching the stored username is now isolated, making the 
code more modular. 

greet_user() Function:
This is the main function that greets the user, refactored to utilize the helper function get_stored_username().
Purpose: To greet the user either by using the stored username or by asking for a new one if no username is stored.
Steps:

Check for Existing Username: It creates a Path object pointing to the username.json file. Calls get_stored_username(path) to check if the 
username is stored in the file. If a username is found, it prints a welcome message: Welcome back, {username}!. Handle New User:
If None is returned (meaning no username was found), it prompts the user to enter their name with input(). json.dumps(username) converts 
the entered username into a JSON-formatted string. path.write_text(contents) saves the username into the username.json file.
It then prints: We'll remember you when you come back, {username}!, confirming that the username has been saved for future use.
3. Calling the greet_user() Function: This is where the program starts running. When greet_user() is called, it first checks if a username 
is stored. If not, it asks for a new one."""

"""Understanding Scope in Functions:
Each function in Python has its own local scope, meaning the variables created inside one function are completely separate from variables in another function, even if they share the same name.
The username variable in both functions refers to different variables. Even though they have the same name, they exist independently in the scope of their respective functions.
"""
# WHAT IS LIBRARIES, PACKAGES AND DEPENDENCIES IN PYTHON. #

"""Libraries:
A library is a collection of pre-written code that you can reuse in your programs. Libraries contain functions, classes, and methods that
solve common tasks, allowing you to avoid reinventing the wheel. For example, Python's standard library includes libraries like math, datetime,
json, etc."""

"""Packages:
A package is a collection of Python modules (or libraries). A package can contain multiple modules organized in a directory structure. 
Packages allow for better code organization and distribution. Modules: Individual Python files (.py) containing functions, classes, or variables.
Packages: Directories with a special __init__.py file that can contain multiple modules."""

"""Dependencies:
A dependency refers to external code or libraries that your project relies on to work properly. When your code depends on other libraries, 
these libraries are called dependencies. Dependency management is crucial for ensuring that all the libraries your code needs are installed 
and available. Tools like pip and virtual environments help manage these dependencies. Example: If your project relies on requests to make 
HTTP requests, you would declare it as a dependency and install it:"""  # pip install requests #
# this line is from python book A third-party package is a library that’s developed outside the core Python language.

# UPDATING PIP

# pip = package installer of python,
# Python includes a tool called pip that’s used to install third-party packages. Because pip helps install packages from external resources.
# $ python -m install pip --upgrade pip

"""The first part of this command, python -m pip, tells Python to run the module pip. The second part, install --upgrade, tells pip to update a 
package that’s already been installed. The last part, pip, specifies which third-party package should be updated"""

# You can use this command to update any third-party package installed on your system.
# $ python -m pip install --upgrade package_name

# INSTALLING PYTEST #
# $ python -m pip install --user pytest
"""We’re still using the core command pip install, without the --upgrade flag this time. Instead, we’re using the --user flag, which tells 
Python to install this package for the current user only"""

# You can use this command to install many third-party packages:
# $ python -m pip install --user package_name

# If you have any difficulty running this command, try running the same command without the --user flag.

# TESTING A FUNCTION #
   # FILE NAME IS name_functions.py #

# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name"""
#     full_name = f'{first} {last}'
#     return full_name.title()

# FILE NAME IS names.py #

# from practice import get_formatted_name
#
# print("Enter 'q' to any time to quit. ")
# while True:
#     first = input("\nPlease give me first name: ")
#     if first == 'q':
#         break
#     last = input("Please give me a last name: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print(f"\tNeatly formatted name: {formatted_name}")

"""In practice.py, the function get_formated_name is defined to take two parameters:
def get_formated_name(first, last):
Here, first and last are placeholders for the actual values you will provide when you call the function.

Function Call:

formatted_name = get_formated_name(first, last)
This is where you actually invoke the function. Values Passed:

In this case, first and last represent the values that the user has inputted through the prompts in the program. Specifically:
When the user enters their first name, that value is stored in the variable first.
When the user enters their last name, that value is stored in the variable last.
What Happens During the Call:

When you call get_formated_name(first, last), Python takes the current values of the variables first and last and passes them into the function.
Inside the function, first and last now contain the actual strings that the user entered. The function uses these strings 
to create a formatted name. 
Example Scenario
Let's say a user runs trash.py and inputs:
First name: john
Last name: doe
In this case:

The value of the variable first is now 'john'.
The value of the variable last is now 'doe'.

So when you call:

formatted_name = get_formated_name(first, last)

It's equivalent to:

formatted_name = get_formated_name('john', 'doe')

Parameters: first and last in the function definition act as placeholders.
Values: The actual values provided by the user during input replace those placeholders when the function is called. """


"""We can see that the names generated here are correct. But say we want to modify get_formatted_name() so it can also handle middle names. 
As we do so, we want to make sure we don’t break the way the function handles names that have only a first and last name. We could test our 
code by running names.py and entering a name like Janis Joplin every time we modify get_formatted_name(), but that would become tedious. 
Fortunately, pytest provides an efficient way to automate the testing of a function’s output. If we automate the testing of get_formatted_name(), 
we can always be confident that the function will work when given the kinds of names we’ve written tests for."""

# UNIT TESTS AND TEST CASES #

"""Unit Test
What It Is: A test that checks a single part of your code (like a function) to make sure it works correctly.
Focus: Tests one small piece of functionality.
Example: Testing if a function that adds two numbers returns the correct result.

Test Case
What It Is: A broader term that describes a specific scenario you want to test, which can involve multiple parts of your code.
Focus: Can test various aspects, like entire features or interactions between different parts of the application.
Example: Testing if a user can log in successfully with valid credentials.
Summary
Unit tests are specific tests for small code parts.
Test cases can cover larger scenarios, including multiple functions or features. """

# A PASSING TEST #

"""With pytest, writing your first unit test is pretty straightforward. We’ll write a single test function. The test function will call the 
function we’re testing, and we’ll make an assertion about the value that’s returned. If our assertion is correct, the test will pass; if the 
assertion is incorrect, the test will fail."""


# File name is # test_name_function.py #

# from practice import get_formated_name
# def test_first_last_name():
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formated_name('janis', 'joplin')    # OUTPUT # formatted_name = 'Janis Joplin' # because we use .title() method.
#     assert formatted_name == 'Janis Joplin'

"""Before we run the test, let’s take a closer look at this function. The name of a test file is important; it must start with test_. When we 
ask pytest to run the tests we’ve written, it will look for any file that begins with test_, and run all of the tests it finds in that file.
In the test file, we first import the function that we want to test: get _formatted_name(). Then we define a test function: in this case, 
test_first _last_name() . This is a longer function name than we’ve been using, for a good reason. First, test functions need to start with the 
word test, followed by an underscore. Any function that starts with test_ will be discovered by pytest, and will be run as part of the testing 
process. Also, test names should be longer and more descriptive than a typical function name. You’ll never call the function yourself; pytest 
will find the function and run it for you. Test function names should be long enough that if you see the function name in a test report, you’ll 
have a good sense of what behavior was being tested. Next, we call the function we’re testing . Here we call get_formatted
_name() with the arguments 'janis' and 'joplin', just like we used when we ran names.py. We assign the return value of this function to 
formatted_name. Finally, we make an assertion 3. An assertion is a claim about a condition. Here we’re claiming that the value of formatted_name 
should be  'Janis Joplin'."""

# above code from chatgpt
# formatted_name = get_formated_name('janis', 'joplin')
# Calling the Function: This line calls the get_formated_name function with the first name 'janis' and the last name 'joplin'. The result is stored
# in the variable formatted_name.

# assert formatted_name == 'Janis Joplin'

"""Assertion: This line checks whether formatted_name is equal to the expected output 'Janis Joplin'.
If the condition is true (meaning the function returned the correct formatted name), the test passes silently.
If it's false, an AssertionError is raised, indicating the test failed."""

# RUNNING A TEST #
"""If you run the file test_name_function.py directly, you won’t get any output  because we never called the test function. Instead, we’ll 
have pytest run the test file for us. To do this, open a terminal window and navigate to the folder that contains the test file."""

# ┌──(thor㉿thor) - [~ / python]
# └─$ pytest
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == test
# session
# starts == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# platform
# linux - - Python
# 3.12
# .6, pytest - 8.3
# .2, pluggy - 1.5
# .0
# rootdir: / home / thor / python
# plugins: typeguard - 4.3
# .0, anyio - 4.4
# .0
# collected
# 1
# item
#
# test_name_function.py. (single dot)
# [100 %]
#
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = 1
# passed in 0.61 (seconds)
# s == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#

"""The single dot after the name of the file tells us that a single test passed, and the 100% makes it clear that all of the tests have been run. 
A large project can have hundreds or thousands of tests, and the dots and percentage-complete indicator can be helpful in monitoring the overall 
progress of the test run. This output indicates that the function get_formatted_name() will always work for names that have a first and last name, 
unless we modify the function. When we modify get_formatted_name(), we can run this test again. If the test passes, we know the function will 
still work for names like Janis Joplin."""


# A FAILING TEST #

"""What does a failing test look like? Let’s modify get_formatted_name() so it can handle middle names, but let’s do so in a way that breaks the 
function for names with just a first and last name, like Janis Joplin."""

# file name is # name_function.py #

# def get_formated_name(first, middle, last):
#     """Generate a neatly formatted full name."""
#     full_name = f'{first} {middle} {last}'
#     return full_name.title()

# $ pytest
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == test
# session
# starts == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# platform
# linux - - Python
# 3.12
# .6, pytest - 8.3
# .2, pluggy - 1.5
# .0
# rootdir: / home / thor / python
# plugins: typeguard - 4.3
# .0, anyio - 4.4
# .0
# collected
# 1
# item
#
# test_name_function.py
# F[100 %]
#
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == FAILURES == == == == =
# = == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
# ________________________________________________________________________
# test_first_last_name
# ________________________________________________________________________
#
#
# def test_first_last_name():
#     """Do names like 'Janis Joplin' work?"""
#
# > formatted_name = get_formated_name('janis', 'joplin')
# E
# TypeError: get_formated_name()
# missing
# 1
# required
# positional
# argument: 'last'
#
# test_name_function.py: 4: TypeError
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == short
# test
# summary
# info == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == =
# FAILED
# test_name_function.py::test_first_last_name - TypeError: get_formated_name()
# missing
# 1
# required
# positional
# argument: 'last'
# == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == = 1
# failed in 0.34
# s == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == == ==
#
#

"""There’s a lot of information here because there’s a lot you might need to know when a test fails. The first item of note in the output is a 
single F , which tells us that one test failed. We then see a section that focuses on FAILURES , because failed tests are usually the most 
important thing to focus on in a test run. Next, we see that test_first_last_name() was the test function that failed . An angle bracket 
indicates the line of code that caused the test to fail. The E on the next line  shows the actual error that caused the failure: a TypeError due 
to a missing required positional argument, last. The most important information is repeated in a shorter summary at the end, so when you’re running 
many tests, you can get a quick sense of which tests failed and why."""

# RESPONDING TO A FAILED TEST #

"""What do you do when a test fails? Assuming you’re checking the right conditions, a passing test means the function is behaving correctly and a 
failing test means there’s an error in the new code you wrote. So when a test fails, don’t change the test. If you do, your tests might pass, 
but any code that calls your function like the test does will suddenly stop working. Instead, fix the code that’s causing the test to fail. 
Examine the changes you just made to the function, and figure out how those changes broke the desired behavior.
In this case, get_formatted_name() used to require only two parameters: a first name and a last name. Now it requires a first name, middle name, 
and last name. The addition of that mandatory middle name parameter broke the original behavior of get_formatted_name(). The best option here 
is to make the middle name optional. Once we do, our test for names like Janis Joplin should pass again, and we should be able to accept middle 
names as well. Let’s modify get_formatted_name() so middle names are optional and then run the test case again. If it passes, we’ll move on to 
making sure the function handles middle names properly. To make middle names optional, we move the parameter middle to the
end of the parameter list in the function definition and give it an empty default value. We also add an if test that builds the full name 
properly, depending on whether a middle name is provided:"""

# file name is # name_function.py #

def get_formated_name(first, last, middle = ''):
    """Generate a neatly formatted full name."""
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()  # return statement outside of the else block if inside  it will not execute when a middle name is provided. #

"""In this new version of get_formatted_name(), the middle name is optional. If a middle name is passed to the function, the full name will 
contain a first, middle, and last name. Otherwise, the full name will consist of just a first and last name. Now the function should work for 
both kinds of names. To find out if the function still works for names like Janis Joplin."""

# ADDING NEW TESTS #

"""Now that we know get_formatted_name() works for simple names again, let’s write a second test for people who include a middle name. 
We do this by adding another test function to the file test_name_function.py."""

FILE NAME IS # test_name_function.py #

# from practice import get_formated_name
# def test_first_last_name():
#     """Do names like 'Janis Joplin' work?"""
#     formatted_name = get_formated_name('janis', 'joplin')
#     assert formatted_name == 'Janis Joplin'
#
# def test_first_last_middle_name():
#     """Do name like 'Wolfgang Amadeus Mozart' work?"""
#     formatted_name = get_formated_name(
#         'wolfgang', 'mozart', 'amadeus')
#     assert formatted_name == 'Wolfgang Amadeus Mozart'


"""After the first test passes, the report says "[50%]" because it’s halfway through running the tests.
After the second test passes, the report says "[100%]" because all tests have been run successfully.
Both tests passed, and everything is working correctly. You can safely ignore the "50%"—it just shows the testing progress, not the success 
rate of individual tests."""

"""FROM BOOK We name this new function test_first_last_middle_name(). The function name must start with test_ so the function runs automatically 
when we run pytest. We name the function to make it clear which behavior of get_formatted _name() we’re testing. As a result, if the test fails, 
we’ll know right away what kinds of names are affected. To test the function, we call get_formatted_name() with a first, last, and
middle name 1, and then we make an assertion 2 that the returned full name matches the full name (first, middle, and last) that we expect.
 The two dots indicate that two tests passed, which is also clear from the last line of output. """

# TESTING A CLASS #
# In the first part of this chapter, you wrote tests for a single function. Now you’ll write tests for a class.

# A VARIETY OF ASSERTIONS #

"""So far, you’ve seen just one kind of assertion: a claim that a string has a specific value. When writing a test, you can make any 
claim that can be expressed as a conditional statement. If the condition is True as expected, your assumption about how that part of your 
program behaves will be confirmed; you can be confident that no errors exist. If the condition you. assume is True is actually False, the test 
will fail and you’ll know there’s an issue to resolve. shows some of the most useful kinds of assertions
you can include in your initial tests."""
# Commonly Used Assertion Statements in Tests. #

# Assertion:                                              Claim:
#
# assert a == b                                       Assert that two values are equal.
# assert a != b                                       Assert that two values are not equal.
# assert a                                            Assert that a evaluates to True.
# assert not a                                        Assert that a evaluates to False.
# assert element in list                              Assert that an element is in a list.
# assert element not in list                          Assert that an element is not in a list

# A CLASS TO TEST #

"""Testing a class is similar to testing a function, because much of the work involves testing the behavior of the methods in the class. 
However, there are a few differences, so let’s write a class to test. Consider a class that helps administer anonymous surveys:"""
# FILE NAME IS # language_survey.py #

# class AnonymousSurvey:
#     """Collect anonymous answers to a survey question."""
# def __init__(self, question):
#     """Store a question, and prepare to store responses."""
#     self.question = question
#     self.responses = []
#
# def show_question(self):
#     """Show the survey question."""
#     print(self.question)
#
# def store_response(self, new_response):
#     """Store a single response to the survey."""
#     self.responses.append(new_response)
#
# def show_results(self):
#     """Show all the responses that have been given."""
#     print("Survey results:")
#     for response in self.responses:
#         print(f"- {response}")

# What it does: This line defines a class named AnonymousSurvey. A class is a blueprint for creating objects. The class here represents a survey
# that collects anonymous responses to a question.

# 2. The __init__ Method (Constructor)

# What it does: This is a special method called the constructor. It runs automatically when an object of this class is created.
# Parameters:
# self: Refers to the current object. Every method in a class takes self as the first argument.
# question: A variable where you pass the survey question when creating an object.

# Inside the method:
# self.question = question:
# This stores the survey question inside the object so it can be used later. The self refers to the current instance of the class.
# self.responses = []:
# This creates an empty list responses that will store all the answers (responses) people give to the survey.

# 3. The show_question Method
# What it does: This method displays the survey question by printing it out.
# How it works:
# print(self.question) prints the question that was stored when the object was created. It gets the question from self.question, which was set
# in the __init__ method.

# 4. The store_response Method
# What it does: This method takes a response (answer) to the survey and stores it in the responses list.
# Parameters:
# self: Refers to the current object.
# new_response: The response (answer) given by the user.
# How it works:
# self.responses.append(new_response):
# It adds the new response to the list self.responses. Every time a new response is provided, it will be added to this list.

# 5. The show_results Method
# for response in self.responses: Loops through each item (response) in the responses list.
# print(f"- {response}"): For each response in the list, it prints the response with a hyphen (-) before it, like a bullet point.

# Calling code
# survey = AnonymousSurvey("What is your favorite programming language?")
# survey.show_question()
# survey.store_response("Python")
# survey.store_response("JavaScript")
# survey.store_response("C++")
# survey.show_results()


"""What it does:
This line creates an object (instance) of the AnonymousSurvey class, and the name of this object is survey. Why we do this:
In Python, a class is just a blueprint. To use the class, you need to create an object from it. This is done by calling the class with 
parentheses  like a function. What happens inside the parentheses: "What is your favorite programming language?":This string is passed as an 
argument to the class. It becomes the value of the question parameter in the __init__ method. Inside the class, self.question is set to this 
string, meaning your object now stores this question for future use."""

"""FROM BOOK: This class starts with a survey question that you provide 1 and includes an empty list to store responses. The class has 
methods to print the survey question 2, add a new response to the response list 3, and print all the responses stored in the list 4. To create an 
instance from this class, all you. have to provide is a question. Once you have an instance representing a particular survey, you display 
the survey question with show_question(), store a response using store_response(), and show results with show_results(). To show that the 
AnonymousSurvey class works, let’s write a program that uses the class: """

# FILE NAME IS CALLED # languages_survey.py #

# from trash import AnonymousSurvey
# Define a question, and make a survey.
# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)
#
# Show the question, and store responses to the question.
# language_survey.show_question()
# print("Enter 'q' at any time to quit. \n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     language_survey.store_response(response)

# Show the survey results.
# print("\nThank you to everyone who participated in the survey!")
# language_survey.show_results()

# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)

"""question: A string that holds the survey question: "What language did you first learn to speak?".
language_survey = AnonymousSurvey(question):
This line creates an instance of the AnonymousSurvey class, and stores it in the language_survey variable. The survey object now holds the 
question you just defined. The __init__ method is called automatically when you create the object. It sets self.question to "What language did 
you first learn to speak?" and initializes an empty list self.responses to store responses. """

# language_survey.show_question()

"""This calls the show_question() method from the AnonymousSurvey class. It prints the survey question "What language did you first learn 
to speak?" to the screen using the print() function. """

"""FROM BOOK This program defines a question ("What language did you first learn to speak?") and creates an AnonymousSurvey object with 
that question. The program calls show_question() to display the question and then prompts for responses. Each response is stored as it is 
received. When all responses have been entered (the user inputs q to quit), show_results() prints the survey results:"""

# TESTING THE ANONYMOUSSURVEY CLASS #

# FILE NAME IS # test_survey.py #

# from trash import AnonymousSurvey
#
# def test_store_single_response():
#     """Test that a single response is stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses

# 2. Defining a Test Function
# def test_store_single_response():
    """Test that a single response is stored properly."""
"""What this does: This defines a function named test_store_single_response().
Purpose: The function is a test, specifically designed to check if the store_response() method correctly stores a single response in the 
responses list of the AnonymousSurvey class."""

# question = "What language did you first learn to speak?"
# language_survey = AnonymousSurvey(question)

"""question: The string "What language did you first learn to speak?" is stored in the variable question.
language_survey = AnonymousSurvey(question):
An instance (object) of the AnonymousSurvey class is created, and it's named language_survey.
The __init__() method is called when the object is created, initializing self.question to store the survey question, and self.responses to an 
empty list for storing responses."""

# 4. Storing a Single Response

# language_survey.store_response('English')

"""This line calls the store_response() method of the language_survey object. How this works: The method appends the string 'English' to the 
responses list inside the language_survey object. After this line runs, language_survey.responses will contain ['English']."""

# 5. Asserting the Result
# assert 'English' in language_survey.responses

"""What it does: This is an assertion that checks if 'English' is in the responses list.
How it works:
The assert statement checks whether the condition 'English' in language_survey.responses is True.
If the condition is True, the test passes and nothing happens (no output is shown).
If the condition is False, an AssertionError is raised, which means the test has failed. """

"""FROM BOOK We start by importing the class we want to test, AnonymousSurvey. The first test function will verify that when we store a response 
to the survey question, the response will end up in the survey’s list of responses. A good descriptive name for this function is 
test_store_single_response() . If this test fails, we’ll know from the function name in the test summary that there was a problem storing a 
single response to the survey. To test the behavior of a class, we need to make an instance of the class. We create an instance called 
language_survey  with the question "What language did you first learn to speak?" We store a single response, English, using the store_response() 
method. Then we verify that the response was stored correctly by asserting that English is in the list language_survey .responses"""

"""This is a good start, but a survey is useful only if it generates more than one response. Let’s verify that three responses can be stored
correctly. To do this, we add another method to TestAnonymousSurvey:"""

# def test_store_three_responses():
#     """Test that three individual responses are stored properly."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     responses = ['English', 'spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_response(response)
#
#     for response in responses:
#         assert response in language_survey.responses

# USING FIXTURES #

"""In test_survey.py, we created a new instance of AnonymousSurvey in each test function. This is fine in the short example we’re working with, 
but in a realworld project with tens or hundreds of tests, this would be problematic. In testing, a fixture helps set up a test environment. 
Often, this means creating a resource that’s used by more than one test. We create a fixture in pytest by writing a function with the decorator 
@pytest.fixture. A decorator is a directive placed just before a function definition; Python applies this directive to the function before it 
runs, to alter how the function code behaves. Don’t worry if this sounds complicated; you can start to use decorators from third-party packages 
before learning to write them yourself. Let’s use a fixture to create a single survey instance that can be used in 
both test functions in test_survey.py:"""

# import pytest
# from trash import AnonymousSurvey
#
# @pytest.fixture
# def language_survey():
#     """A survey that will be available to all test functions."""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     return language_survey  # Fix: Removed '()' from return statement
#
# def test_store_single_response(language_survey):
#     """Test that a single response is stored properly."""
#     language_survey.store_response('English')
#     assert 'English' in language_survey.responses
#
# def test_store_three_responses(language_survey):
#     """Test that three individual responses are stored properly."""
#     responses = ['English', 'Spanish', 'Mandarin']
#     for response in responses:
#         language_survey.store_response(response)
#
#     for response in responses:
#         assert response in language_survey.responses

"""We need to import pytest now, because we’re using a decorator that’s defined in pytest. We apply the @pytest.fixture decorator to the new 
function language_survey() . This function builds an AnonymousSurvey  object and returns the new survey. Notice that the definitions of both 
test functions have changed ; each test function now has a parameter called language_survey. When a parameter in a test function matches the name 
of a function with the @pytest.fixture decorator, the fixture will be run automatically and the return value will be passed to the test function. 
In this example, the function language_survey() supplies both test_store_single_response() and test_store_three_responses() with a language_survey 
instance. There’s no new code in either of the test functions, but notice that two lines have been removed from each function: the line that defined 
a question and the line that created an AnonymousSurvey object. When we run the test file again, both tests still pass. These tests would
be particularly useful when trying to expand AnonymousSurvey to handle multiple responses for each person. After modifying the code to accept
multiple responses, you could run these tests and make sure you haven’t affected the ability to store a single response or a series of individual
responses. The structure above will almost certainly look complicated; it contains some of the most abstract code you’ve seen so far. You don’t 
need to use fixtures right away; it’s better to write tests that have a lot of repetitive code than to write no tests at all. Just know that when 
you’ve written enough tests that the repetition is getting in the way, there’s a well-established way to deal with the repetition. Also, fixtures 
in simple examples like this one don’t really make the code any shorter or simpler to follow. But in projects with many tests, or in situations 
where it takes many lines to build a resource that’s used in multiple tests, fixtures can drastically improve your test code. When you want to 
write a fixture, write a function that generates the resource that’s used by multiple test functions. Add the @pytest.fixture. decorator to the 
new function, and add the name of this function as a parameter for each test function that uses this resource. Your tests will be shorter and easier 
to write and maintain from that point forward."""
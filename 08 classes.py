"""Object-oriented programming (OOP) is one of the most effective approaches to writing software. In object-oriented programming,
you write classes that represent real-world things and situations, and you create objects based on these classes
Making an object from a class is called instantiation, and you work with instances of a class."""

# CREATING AND USING A CLASS #

"""You can model almost anything using classes. Let’s start by writing a simple class, Dog, that represents a dog—not one dog in
particular, but any dog. What do we know about most pet dogs? Well, they all have a name and an age. We also know that most dogs sit 
and roll over. Those two pieces of information (name and age) and those two behaviors (sit and roll over) will go in our Dog class because 
they’re common to most dogs. This class will tell Python how to make an object representing a dog. After our class is written, we’ll use it to
make individual instances, each of which represents one specific dog"""

# CREATING THE DOG CLASS #

# Each instance created from the Dog class will store a name and an age, and we’ll give each dog the ability to sit() and roll_over():
# class Dog:
#     """A simple attempt to model a dog"""
#     def __init__(self, name, age):
#         """Initialize the name and attributes"""
#         self.name = name               # NAME AND AGE ARE VARIABLE SELF IS NOT VARIABLE IT IS PREFIX #
#         self.age = age
#     def sit(self):                    # SIT IS A METHOD AND ALSO ROLL_OVER IS ALSO A METHOD NOT FUNCTIONS #
#         """Simulate a dog sitting in response to a command"""
#         print(f'{self.name} is now sitting.')
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f'{self.name} rolled over!')

"""There’s a lot to notice here, but don’t worry. You’ll see this structure throughout this chapter and have lots of time to get 
used to it. We first define a class called Dog . By convention, capitalized names refer to classes in Python. There are no parentheses
in the class definition because we’re creating this class from scratch. We then write a docstring describing what
this class does."""

# THE --INIT--() METHOD #

"""A function that’s part of a class is a method. Everything you learned about functions applies to methods as well; the only practical 
difference for now is the way we’ll call methods. The __init__() method is a special method that Python runs automatically whenever 
we create a new instance based on the Dog class. This method has two leading underscores and two trailing underscores, a convention
that helps prevent Python’s default method names from conflicting with your method names. Make sure to use two underscores on each side
 of __init__(). If you use just one on each side, the method won’t be called automatically when you use your class, which can
result in errors that are difficult to identify. We define the __init__() method to have three parameters: self, name,
and age. The self parameter is required in the method definition, and it must come first, before the other parameters. It must be included
in the definition because when Python calls this method later (to create an instance of Dog), the method call will automatically pass the 
self argument. Every method call associated with an instance automatically passes self, which is a reference to the instance itself; 
it gives the individual instance access to the attributes and methods in the class. When we make an
instance of Dog, Python will call the __init__() method from the Dog class. We’ll pass Dog() a name and an age as arguments; 
self is passed automatically, so we don’t need to pass it. Whenever we want to make an instance from the Dog class, we’ll provide values 
for only the last two parameters, name and age The two variables defined in the body of the __init__() method each have the prefix self .
Any variable prefixed with self is available to every method in the class, and we’ll also be able to access these variables through
any instance created from the class. The line self.name = name takes the value associated with the parameter name and assigns it to the
variable name, which is then attached to the instance being created. The same process happens with self.age = age. Variables that are 
accessible through instances like this are called attributes. The Dog class has two other methods defined: sit() and roll_over().
Because these methods don’t need additional information to run, we just define them to have one parameter, self. The instances we create
later will have access to these methods. In other words, they’ll be able to sit and roll over. For now, sit() and roll_over() don’t do much. 
They simply print a message saying the dog is sitting or rolling over. But the concept can be extended to realistic situations: if this 
class were part of a computer game, these methods would contain code to make an animated dog sit and roll over. If this class was written
to control a robot, these methods would direct movements that cause a robotic dog to sit and roll over.
he __init__ method is a special method in Python called a constructor. It is automatically called when you create an instance of the 
class. Its role is to initialize the object's attributes (variables that hold data about the object). self: A reference to the current
instance of the class. It allows the method to access and modify the attributes and methods of the object being created."""

# MAKING AN INSTANCE FROM A CLASS #
# REMEMBER OBJECT AND INSTANCE BOTH ARE SAME YOU REMEMBER OBJECT WHILE READING WHEN INSTANCE OR INSTANCES ARE APPEAR #


# class Dog:
#     """A simple attempt to model a dog"""
#     def __init__(self, name, age):
#         """Initialize the name and attributes"""
#         self.name = name
#         self.age = age
#     def sit(self):
#         """Simulate a dog sitting in response to a command"""
#         print(f'{self.name} is now sitting.')
#     def roll_over(self):
#         """Simulate rolling over in response to a command"""
#         print(f'{self.name} is now sitting.')

# Creating an object, which automatically calls __init__
# my_dog = Dog('willie', 6)      # MY DOG IS A VARIABLE, OBJECT, ALSO INSTANCE #
# print(f'My dog\'s name is {my_dog.name}')
# print(f'My dog is {my_dog.age} years old.')
# You need to explicitly call the methods to execute them.

# my_dog.sit()  # This will execute the sit() method.
# my_dog.roll_over()  # This will execute the roll_over() method

"""Python automatically calls and executes the entire block of code inside the __init__ method whenever you create a new object from
the class. This process is also referred to as initialization.
 # Here’s what happens: #
Object Creation: When you create an object (instance) of the class (e.g., my_dog = Dog('willie', 6)), Python detects 
that you're calling the class.Automatic Call to __init__: At that point, Python automatically calls the __init__ method of
the class for the new object. You don't need to explicitly call __init__—it just happens automatically.
Code Execution Inside __init__:
Python will execute the code inside the __init__ method line by line.
It takes the arguments you passed when creating the object (e.g., 'willie' and 6 in the example) and assigns them to the 
object's attributes (self.name and self.age).
Execution:
When you write my_dog = Dog('willie', 6), Python automatically: Calls Dog.__init__ method. Executes everything in the __init__ method,
so it runs all the code inside the method.
Why is self needed?
When you create multiple objects from the same class, each object needs to store its own unique data. self is what makes 
it possible for each object to keep track of its own data.
When you call my_dog.sit(), Python automatically passes the my_dog object as the first argument to the sit method. Inside the
method, self refers to my_dog, so self.name is the same as my_dog.name, which prints "Willie is now sitting.".
The same happens with roll_over(). The method receives the object via self, and prints "Willie rolled over!"

#  MY_DOG IS A VARIABLE OR WHAT #
 
 my_dog is an instance of the Dog class, also known as an object. It is not just a regular variable; instead, 
it is an object that has been created based on the Dog class blueprint. So, my_dog is an instance of the Dog class, which means
it has access to the attributes name and age as well as the methods like sit() and roll_over().
my_dog is an object (instance of the Dog class), not a simple variable. It holds the data specific to that instance, like the name
'Willie' and the age 6, and can call methods defined in the class, such as sit() and roll_over().
my_dog behaves like a variable because it stores a reference to the object created from the Dog class. You can think of it as 
a special kind of variable that points to an object rather than just holding simple data like an integer or string.
Example Comparison:
Regular variable: x = 10
Object reference: my_dog = Dog('Willie', 6)
In both cases, you're assigning something to a name, but my_dog holds an object with attributes and methods rather
than just a simple value like 10.

# ATTRIBUTES #

In your code, attributes are the variables that belong to an object. They store information about the object
Attributes in This Code:
self.name and self.age are the attributes of the Dog class.
self.name stores the dog's name.
self.age stores the dog's age.
Are Attributes and Variables the Same?
Attributes are specific to objects (or instances) of a class. They describe the state or characteristics of an object.
Variables is a more general term. Variables can exist anywhere in a program (inside functions, globally, etc.), whereas 
attributes specifically belong to objects and clas
In this case, name and age are attributes of the my_dog object (which is an instance of the Dog class), 
and they are also variables that store the values assigned to them."""

 """PYTHON BOOK _ DEFINITION FOR THIS CODE Think of a class as a set of instructions for how to make an instance. The Dog class is
a set of instructions that tells Python how to make individual instances representing specific dogs.The Dog class we’re using here is the
one we just wrote in the previous example. Here, we tell Python to create a dog whose name is 'Willie' and whose age is  1. When Python reads
this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. The __init__() method creates an instance representing
this particular dog and sets the name and age attributes using the values we provided. Python then returns an instance representing this dog.
We assign that instance to the variable my_dog. The naming convention is helpful here; we can usually assume that a capitalized name like Dog
refers to a class, and a lowercase name like my_dog refers to a single instance created from a class."""

 # ACCESSING ATTRIBUTES #

# To access the attributes of an instance, you use dot notation. We access the value of my_dog’s attribute name.
my_dog.name
"""Dot notation is used often in Python. This syntax demonstrates how Python finds an attribute’s value. Here, Python looks at the
instance my_dog and then finds the attribute name associated with my_dog. This is the same attribute referred to as self.name in the 
class Dog. We use the same approach to work with the attribute age . The output is a summary of what we know about my_dog"""

# CALLING METHODS #

# After we create an instance from the class Dog, we can use dot notation to call any method defined in Dog.
# my_dog = Dog('Willie', 6)
# my_dog.sit()
# my_dog.roll_over()
"""To call a method, give the name of the instance (in this case, my_dog) and the method you want to call, separated by a dot.
When Python reads my_dog.sit(), it looks for the method sit() in the class Dog and runs that code. Python interprets the line
my_dog.roll_over() in the same way"""

# CREATING MULTIPLE INSTANCES #

# class Dog:
#     --snip--
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('Lucy', 3)
# print(f'My dog\'s name is {my_dog.name}')
# print(f'My dog is {my_dog.age} years old.')
# my_dog.sit()
#
# print(f'Your dog\'s name is {your_dog.name}')
# print(f'Your dog is {your_dog.age} years old.')
# your_dog.sit()

"""You can create as many instances from a class as you need. Let’s create a second dog called your_dog In this example we create a dog
named Willie and a dog named Lucy. Each dog is a separate instance with its own set of attributes, capable of the same set of actions:
Even if we used the same name and age for the second dog, Python would still create a separate instance from the Dog class. You can make
as many instances from one class as you need, as long as you give each instance a unique variable name or it occupies a unique spot in 
a list or dictionary"""

# WORKING WITH CLASSES AND INSTANCES #

"""You can use classes to represent many real-world situations. Once you write a class, you’ll spend most of your time working with 
instances created from that class. One of the first tasks you’ll want to do is modify the attributes associated with a particular instance.
You can modify the attributes of an instance directly or write methods that update attributes in specific ways."""

# THE CAR CLASS #

# class Car:
#  """A simple attempt to represent a car"""
#
#  def __init__(self, make, model, year):
#   """Initialize attributes to describe a car."""
#   self.make = make
#   self.model = model
#   self.year = year
#
#  def get_descriptive_name(self):
#   """Return a neatly formatted descriptive name."""
#   long_name = f'{self.year} {self.make} {self.model}'    # IN THIS CODE long_name IS A VARIABLE #
#   return long_name.title()
#
#
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name()) # The caller in this context is the print() function. It calls the get_descriptive_name()
                                              # method on the my_new_car object and receives the value returned by this method.

"""my_new_car.get_descriptive_name(): This is the method call that triggers the get_descriptive_name method of the Car class.
return long_name.title(): This line inside the get_descriptive_name method sends the formatted string back to the caller
How Data is Assigned:
get_descriptive_name() Method:
When get_descriptive_name() is called, it executes and computes the value long_name.title(), which is '2024 Audi A4'.
The return statement then sends this value back to the caller.
Print Statement:
print(my_new_car.get_descriptive_name()) is the caller. It receives the returned value '2024 Audi A4' from the 
get_descriptive_name() method and prints it.
Summary:
get_descriptive_name() Method: Executes the return statement to provide the computed value.
print(my_new_car.get_descriptive_name()): This statement receives the returned value and handles its output (printing in this case).
So, get_descriptive_name() is the code where return provides the value, and print() is where this returned value is assigned 
and used (for displaying the output).

# print(my_new_car.get_descriptive_name()) # in this print call my should we use # my_new_car.#

get_descriptive_name() is a method defined within the Car class. To call this method, you need to call it on an instance of 
the Car class. In this case, my_new_car is an instance of the Car class, so you need to use it to call the method.
The method get_descriptive_name() uses instance-specific attributes (self.make, self.model, self.year). When you call my_new_car.
get_descriptive_name(), it uses these attributes from the my_new_car instance to generate the descriptive name. If you don't specify
the instance (my_new_car), Python won't know which instance's data to use.

# Why you should use return: #
The return statement specifies what value you want the method to send back to the caller. Without it, the method  does not provide
any meaningful output and defaults to None. With return, you are telling Python to give back the long_name string as the result of 
calling get_descriptive_name()

# my_new_car = Car('audi', 'a4', 2024)#   IN THIS CODE WHAT SHOULD WE CALL TO MY_NEW_CAR  #
Object: my_new_car is primarily an object because it is an instance of the Car class. In object-oriented programming (OOP), 
when you create an instance of a class, that instance is called an object.
Instance: my_new_car is also referred to as an instance of the Car class because it is a specific realization of the Car class. 
Every time you create a new car using the Car class, it creates a new instance (object).
Variable: Technically, my_new_car is also a variable because it holds a reference to the Car object in memory. In this sense, 
my_new_car is a variable that refers to an object of the Car class.

# SETTING A DEFAULT VALUE FOR AN ATTRIBUTE #
 




"""
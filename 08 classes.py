    # 08 CLASSES,  08 CLASSES,  08 CLASSES,  08 CLASSES,  08 CLASSES,  08 CLASSES,  08 CLASSES #

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

 # """PYTHON BOOK _ DEFINITION FOR THIS CODE Think of a class as a set of instructions for how to make an instance. The Dog class is
# a set of instructions that tells Python how to make individual instances representing specific dogs.The Dog class we’re using here is the
# one we just wrote in the previous example. Here, we tell Python to create a dog whose name is 'Willie' and whose age is  1. When Python reads
# this line, it calls the __init__() method in Dog with the arguments 'Willie' and 6. The __init__() method creates an instance representing
# this particular dog and sets the name and age attributes using the values we provided. Python then returns an instance representing this dog.
# We assign that instance to the variable my_dog. The naming convention is helpful here; we can usually assume that a capitalized name like Dog
# refers to a class, and a lowercase name like my_dog refers to a single instance created from a class."""

 # ACCESSING ATTRIBUTES #

# To access the attributes of an instance, you use dot notation. We access the value of my_dog’s attribute name.
# my_dog.name
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
my_new_car is a variable that refers to an object of the Car class."""

# SETTING A DEFAULT VALUE FOR AN ATTRIBUTE #
# class Car:
#  """A simple attempt to represent a car"""
#
#  def __init__(self, make, model, year):
#   """Initialize attributes to describe a car"""
#   self.make = make
#   self.model = model
#   self.year = year
#   self.odometer_reading = 0
#
#  def get_descriptive_name(self):
#   """Return a neatly formeted descriptive name"""
#   long_name = f'{self.year} {self.make} {self.model}'
#   return long_name.title()
#
#  def read_odometer(self):
#   """Print a statement showing the car's mileage"""
#   print(f'This car has {self.odometer_reading} miles on it.')
#
#
# my_new_car = Car('audi', 'a4', 1994)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()

"""make, model, and year: These attributes are defined as required parameters. You must provide values for them when creating an 
instance of Car. odometer_reading: This attribute is defined inside the __init__() method but is not passed as a parameter.
Instead, it is automatically assigned a default value of 0. This means that every car object created will start with an odometer_reading 
of 0 unless explicitly modified later."""

""" when you create a new object using my_new_car = Car('audi', 'a4', 1994), the __init__ method of the Car class is executed automatically.
 During this execution, all the attributes defined within the __init__ method—including odometer_reading—are automatically assigned to the
my_new_car instance.  WHAT HAPPENS When you create my_new_car = Car('audi', 'a4', 1994), the __init__ method is called automatically.
Inside __init__, the make, model, and year attributes are assigned the values 'audi', 'a4', and 1994, respectively. The odometer_reading 
attribute is also automatically set to 0 by default for the my_new_car instance. """


"""PYTHON FROM BOOK This time, when Python calls the __init__() method to create a new instance, it stores the make, model, and year
values as attributes, like it did in the previous example. Then Python creates a new attribute called odometer_reading and sets its initial
value to 0 1. We also have a new method called read_odometer() 2 that makes it easy to read a car’s mileage.
Not many cars are sold with exactly 0 miles on the odometer, so we need a way to change the value of this attribute"""

# MODIFYING ATTRIBUTE VALUE #

"""You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through a 
method, or increment the value (add a certain amount to it) through a method. Let’s look at each of these approaches."""

# MODIFYING AN ATTRIBUTE'S VALUE DIRECTLY #

# class Car:
#     -- snip --
#
# my_new_car = Car('audi', 'a4', 1994)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

"""We use dot notation to access the car’s odometer_reading attribute, and set its value directly. This line tells Python to take the instance
my_new_car, find the attribute odometer_reading associated with it, and set the value of that attribute to 23, Sometimes you’ll want to access 
attributes directly like this, but other times you’ll want to write a method that updates the value for you"""

# MODIFYING AN ATTRIBUTE'S VALUE THROUGH A METHOD #

# class Car:
#     --snip--
#
#     def update_odometer(self, mileage):
#         """Set the odometer reading to given value."""
#         self.odometer_reading = mileage
#
#
# my_new_car = Car('audi', 'a4', 1994)
# print(f'{my_new_car.get_descriptive_name()}\n')    # IF YOU WANT TO ADD A NEW LINE #
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

"""When you create an instance of the Car class with my_new_car = Car('audi', 'a4', 1994), the __init__ method sets up several
attributes for this instance, including self.odometer_reading, which is initially set to 0.
                    # my_new_car.update_odometer(23) #
This line calls the update_odometer method on the my_new_car instance, passing 23 as the mileage argument. The method executes 
self.odometer_reading = 23, which sets the odometer_reading attribute of my_new_car to 23

#   WHY SHOULD I MENTION THE INSTANCE NAME TO UPDATE ATTRIBUTE VALUE THROUGH METHOD #
Why Mention the Instance Name?
Identifying the Object: In object-oriented programming, you can have multiple instances (objects) of the same class. Each instance 
has its own set of attributes. By using the instance name (like my_new_car), you're telling Python exactly which object's attributes you 
want to modify. Calling the Method: The method is defined within the class, but it is executed in the context of a particular instance. 
When you call my_new_car.update_odometer(23), Python uses my_new_car to access the self.odometer_reading attribute specifically 
for that instance.

IMP +++ When you create a new instance of a class, only the __init__ method runs automatically. Other Methods: Do Not Run Automatically: 
Other methods in the class, such as get_descriptive_name, read_odometer, and update_odometer, do not run automatically when an instance 
is created. You need to call these methods explicitly if you want them to execute. """

"""Explanation:
self Parameter:
The self parameter in Python is a reference to the current instance of the class. It allows you to access attributes and methods 
associated with that particular instance. When you define an attribute in the __init__ method (or any method) using self, it becomes 
part of the instance, meaning that any method within the class can access it

How self Works:
When you define self.odometer_reading = 0 in the __init__ method, you are saying that the instance of the class (represented by self) will have an attribute called odometer_reading with an initial value of 0.
Later, when you call self.odometer_reading = mileage inside the update_odometer method, you are updating the same odometer_reading attribute that was defined in __init__.
The self prefix is what connects all these references to the same instance's attributes.

Accessing Attributes Across Methods:
Once you define an attribute using self in any method, that attribute is accessible from any other method within the class using self.attribute_name.
It doesn't matter how many methods you have; as long as you reference the attribute with self, you're accessing the same value that belongs to that specific instance.

Universal Access: If you define an attribute with self in any method, it can be accessed or modified in any other method 
within the class, regardless of the number of methods. The prefix self ensures that it's always referring to the instance's attributes."""

# A SIMPLE CODE FOR UNDERSTANDING IN DEPTH FROM CHAT GPT #

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def update_odometer(self, mileage):
#         self.odometer_reading = mileage
#
#     def read_odometer(self):
#         print(f'This car has {self.odometer_reading} miles on it.')
#
# Creating two separate instances
# my_new_car = Car('audi', 'a4', 1994)
# your_new_car = Car('toyota', 'corolla', 2020)
#
# Updating and reading odometer for my_new_car
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()  # Output: This car has 23 miles on it.
#
# Updating and reading odometer for your_new_car
# your_new_car.update_odometer(100)
# your_new_car.read_odometer()  # Output: This car has 100 miles on it.

    # OR #
# class Car:
#     --snip--
# my_new_car = Car('audi', 'a4', 1994)
# your_new_car = Car('subaru', 'ch500463', 19999)
# print(my_new_car.get_descriptive_name())
# print(f'{your_new_car.get_descriptive_name()}\n')
#
# my_new_car.update_odometer(25)
# your_new_car.update_odometer(400)
#
# my_new_car.read_odometer()
# your_new_car.read_odometer()

""""Summary:
Each instance has its own set of attributes. You cannot use my_new_car's attributes directly with your_new_car because they belong to 
different instances. self ensures that each instance handles its own attributes, keeping them separate from other instances.
No sharing: your_new_car cannot access or use my_new_car's attributes without explicitly copying or passing them between instances. """

#  WE CAN EXTEND THE METHOD UPDATE_ODOMETER() TO DO ADDITIONAL WORK #
# class Car:
#     --snip--
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject change it it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('you can\'t roll back an odometer!')
#
# my_new_car = Car('audi', 'a4', 1994)
# print(my_new_car.get_descriptive_name())
#
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()

""" IF YOU USE # MY_NEW_CAR.UPDATE_ODOMETER(-1)# YOU DON'T GET EXPECTING RESULT WHY: WANT YOU PRINT -1 USE LESS THAN OR EQUAL TO:

if mileage >= self.odometer_reading: ensures that only mileage values that are greater than or equal to the current reading are accepted.
If mileage is less than self.odometer_reading, the method prints an error message and does not change the odometer reading.
"""

"""Now update_odometer() checks that the new reading makes sense before modifying the attribute. If the value provided for mileage is 
greater than or equal to the existing mileage, self.odometer_reading, you can update the odometer reading to the new mileage . If the new 
mileage is less than the existing mileage, you’ll get a warning that you can’t roll back an odometer """

# INCREMENT AN ATTRIBUTE'S VALUE THROUGH A METHOD #

"""Sometimes you’ll want to increment an attribute’s value by a certain amount, rather than set an entirely new value. Say we buy a used car 
and put 100 miles on it between the time we buy it and the time we register."""

# class Car:
#     --snip--
#
#     def update_odometer(self, mileage):
#         --snip--
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

"""The new method increment_odometer() takes in a number of miles, and adds this value to self.odometer_reading. First, we create a used car, 
my_used_car . We set its odometer to 23,500 by calling update_odometer() and passing it 23_500 . Finally, we call increment_odometer() and pass 
it 100 to add the 100 miles that we drove between buying the car and registering it:"""

"""self.odometer_reading += miles
The += operator is shorthand in Python for adding a value to an existing variable.
What it does:
self.odometer_reading += miles is equivalent to self.odometer_reading = self.odometer_reading + miles.
It takes the current value of self.odometer_reading and adds miles to it.
The result is then stored back in self.odometer_reading"""

"""23_500 is the same as writing 23500. The underscore has no effect on the numeric value; it's just for readability.

IF YOU WANT TO PRINT WITH COMMAS CHANGE READ_ODOMETER METHOD PRINT CALL # print(f'This car has {self.odometer_reading:,} miles on it.') #
AND CALL WITHOUT UNDERSCORE LIKE # my_used_car.update_odometer(23500) #
he reason the code prints a comma and not a semicolon is because the comma inside the curly braces {self.odometer_reading:,} is part 
of Python's string formatting syntax The format specifier :, automatically places commas as thousand separators in a number when used 
inside {} in an f-string or str.format(), STR.FORMAT() MEANS  Converts the number to a string: str(number). """

# INHERITANCE #

"""You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another class 
you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes and methods of the first class. 
The original class is called the parent class, and the new class is the child class. The child class can inherit any or all of the attributes 
and methods of its parent class, but it’s also free to define new attributes and methods of its own."""

# THE __INTI__ METHOD FOR A CHILD CLASS #

"""When you’re writing a new class based on an existing class, you’ll often want to call the __init__() method from the parent class. 
This will initialize any attributes that were defined in the parent __init__() method and make them available in the child class.
As an example, let’s model an electric car. An electric car is just a specific kind of car, so we can base our new ElectricCar class on 
the Car class we wrote earlier. Then we’ll only have to write code for the attributes and behaviors specific to electric cars.
Let’s start by making a simple version of the ElectricCar class, which does everything the Car class does:"""

# class Car:
#     """A simple attempt to represent a car"""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formated descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f'This car has {self.odometer_reading:,} miles on it.')
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject change it it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('you can\'t roll back an odometer!')
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self,make, model,year):
#         """Initialize attributs of the parent class"""
#         super(). __init__(make, model, year)   # ALSO SELF.ODOMETER_READING = 0 ALSO EXECUTE BECAUSE IT IS PART OF __INIT__ #
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name()) # in this print statement it will execute parent class method get_descriptive_name inside all the code.

"""__init__ Method
The __init__ method in the ElectricCar class is used to initialize an instance of ElectricCar.
super().__init__(make, model, year) is called inside the __init__ method of ElectricCar to initialize the attributes of the parent 
class (Car). The super() function is used to call the parent class's __init__ method, passing make, model, and year to it. This ensures 
that the ElectricCar instance is properly initialized with the attributes from the Car class (make, model, year, and odometer_reading).

Inheritance
Since ElectricCar inherits from Car, it automatically has access to all the methods defined in the Car class. For example, ElectricCar 
can use the get_descriptive_name(), read_odometer(), update_odometer(), and increment_odometer() methods without having to redefine them.

Calling Methods
When print(my_leaf.get_descriptive_name()) is executed, it calls the get_descriptive_name() method from the Car class, because 
ElectricCar doesn't have its own get_descriptive_name() method. The method returns a formatted string describing the car.

IF YOU USE LIKE THIS # def __init__(self,ma, mo,ye): # IN CHILD CLASS YOU WILL GET ERROR WHY #

Parameter Names in __init__ Method: In the ElectricCar class, you used parameters ma, mo, and ye in the __init__ method. However, you need 
to use the same parameter names in the super().__init__ call that the parent class (Car) expects. In the parent class Car, these parameters 
are make, model, and year.
Incorrect Argument Names in super().__init__: When calling super().__init__, you need to pass the parameters that the parent class expects. 
If you use different parameter names in the ElectricCar class, you need to pass those parameters correctly when calling super()."""

"""make, model, and year are parameters.
When you create an instance like ElectricCar('nissan', 'leaf', 2024), 'nissan', 'leaf', and 2024 are arguments.
In Python, when calling methods from a parent class using super(), you do not need to explicitly pass the self parameter. Here’s why:
When you use super(), you are referring to the parent class and calling its method. Python automatically handles passing the current instance (self) to the method in the parent class.
You only need to provide the arguments for the parameters defined in the parent class’s method signature."""

"""FROM PYTHON BOOK: We start with Car . When you create a child class, the parent class must be part of the current file and must appear 
before the child class in the file. We then define the child class, ElectricCar . The name of the parent class must be included in 
parentheses in the definition of a child class. The __init__() method takes in the information required to make a Car instance .
The super() function  is a special function that allows you to call a method from the parent class. This line tells Python to call the __init__()
method from Car, which gives an ElectricCar instance all the attributes defined in that method. The name super comes from a convention of calling
the parent class a superclass and the child class a subclass. We test whether inheritance is working properly by trying to create
an electric car with the same kind of information we’d provide when making a regular car. We make an instance of the ElectricCar class and
assign it to my_leaf . This line calls the __init__() method defined in ElectricCar, which in turn tells Python to call the __init__() method
defined in the parent class Car. We provide the arguments 'nissan', 'leaf', and 2024. Aside from __init__(), there are no attributes or methods 
yet that are particular to an electric car. At this point we’re just making sure the electric car has the appropriate Car behaviors:
he ElectricCar instance works just like an instance of Car, so now we
can begin defining attributes and methods specific to electric cars."""

# DEFINING ATTRIBUTES AND METHODS FOR THE CHILD CLASS #

"""Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to differentiate the 
child class from the parent class. Let’s add an attribute that’s specific to electric cars (a battery, for example)
and a method to report on this attribute. We’ll store the battery size and write a method that prints a description of the battery"""

# class Car:
#     --snip--
#
# class ElectricCar(Car):
#     """Represents aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model,year)
#         self.battery_size = 40
#
#     def describe_battery(self):
#         """Prints a statement describing the battery size"""
#         print(f'This car has a {self.battery_size} -KWh battery.')
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.describe_battery()

""" We add a new attribute self.battery_size and set its initial value to 40 . This attribute will be associated with all instances 
created from the ElectricCar class but won’t be associated with any instances of Car. We also add a method called describe_battery() that 
prints information about the battery There’s no limit to how much you can specialize the ElectricCar class. You can add as many attributes 
and methods as you need to model an electric car to whatever degree of accuracy you need. An attribute or method that could belong to any car, 
rather than one that’s specific to an electric car, should be added to the Car class instead of the ElectricCar class. Then anyone who uses 
the Car class will have that functionality available as well, and the ElectricCar class will only contain code for the information
and behavior specific to electric vehicles."""

# OVERRIDING METHODS FROM THE PARENT CLASS # OVERRIDE MEANS REPLACE NOT DELETE #

"""You can override any method from the parent class that doesn’t fit what you’re trying to model with the child class. To do this, you 
define a method in the child class with the same name as the method you want to override in the parent class. Python will disregard the 
parent class method and only pay attention to the method you define in the child class. Say the class Car had a method called fill_gas_tank(). 
This method is meaningless for an all-electric vehicle, so you might want to override this method"""

class Car:
    --snip--

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

# class ElectricCar(Car):
#     --snip--
#
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks."""
#         print("This car doesn't have a gas tank!")
#
# Create instances and test the methods
# my_car = Car('Toyota', 'Corolla', 2020)
# my_electric_car = ElectricCar('Tesla', 'Model S', 2023)
#
# print(my_car.get_descriptive_name())
# my_car.fill_gas_tank()

# print(my_electric_car.get_descriptive_name())
# my_electric_car.fill_gas_tank()

"""The Concept of Overriding in Python
For method overriding to happen, the method must exist in both the parent and the child class. If the method exists in the parent class 
and you redefine it in the child class, Python will use the child class's version when that method is called on a child class instance.
When you call fill_gas_tank on an instance of Car, the method in the Car class is executed. When you call fill_gas_tank on an instance of 
ElectricCar, the overridden method in the ElectricCar class is executed, demonstrating how method overriding works.

FROM BOOK Now if someone tries to call fill_gas_tank() with an electric car, Python will ignore the method fill_gas_tank() in Car and run 
this code instead. When you use inheritance, you can make your child classes retain what you need and override anything you don’t need 
from the parent class."""

# INSTANCES AS ATTRIBUTES # COMPOSITION #

"""When modeling something from the real world in code, you may find that you’re adding more and more detail to a class. You’ll find that 
you have a growing list of attributes and methods and that your files are becoming lengthy. In these situations, you might recognize that 
part of one class can be written as a separate class You can break your large class into smaller classes that work together; this approach 
is called composition"""

# class Car:
#     --snip--
#
# class Battery: # WE DEFINE A NEW CLASS CALLED BATTERY THAT DOESN'T INHERIT FROM ANY OTHER CLASS NO PARENTHESES THERE THIS IS FROM SCRATCH #
#     """A simple attempt to model a battery for an electric car"""
#     def __init__(self, battery_size = 40):     # DEFAULT VALUE IS 40 IF NO VALUE IS PROVIDED #
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f'This car has a {self.battery_size}-KWh battery.')
# class ElectricCar(Car):
#     """Represent a statement that describing the battery size"""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()   # THIS SELF.BATTERY ATTRIBUTE BELONGS TO ELECTRICCAR() CLASS #

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()

""" self.battery = Battery()
This line is crucial for understanding composition. It creates an instance of the Battery class and assigns it to the battery 
attribute of the ElectricCar instance.  
How It Works Step by Step # my_leaf = ElectricCar('nissan', 'leaf', 2024) #
When you create an instance of ElectricCar, Python calls the __init__ method in the ElectricCar class.
Inside this __init__ method, super().__init__(make, model, year) is called, which initializes the attributes inherited from the Car  class
(make, model, year, and odometer_reading). After initializing the parent class attributes, the line self.battery = Battery() is executed.

self.battery = Battery():
This line creates a new instance of the Battery class.
The Battery instance is stored in the battery attribute of the ElectricCar instance. This means my_leaf.battery now refers to this 
Battery instance.

Understanding the Implicit Instance Creation
When you see the line self.battery = Battery(), Python does indeed create an instance of the Battery class, even though you don't 
explicitly create and name this instance in the code like you did with my_leaf for the ElectricCar class.

How It Works:
Instance Creation:
When you write Battery(), Python creates a new instance of the Battery class. This instance is created "on the fly" without you needing 
to explicitly name it or store it in a separate variable. Assigning the Instance:
The newly created instance of Battery is immediately assigned to the battery attribute of the ElectricCar instance (my_leaf in your case).
This means that my_leaf.battery now refers to that Battery instance.

"Hidden" Instance:
You're correct in thinking that the instance of Battery is created behind the scenes. It's not "hidden" per se; rather, it's created 
and immediately stored in the battery attribute, so you don't see the creation process as a separate step.
The instance isn't named (like my_leaf or my_new_car), but it still exists and is accessible via my_leaf.battery
Battery() creates a new instance of Battery."""

 # ADDING ARGUMENTS TO THE BATTERY CLASS FROM CHAT GPT #

# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#     def __init__(self, battery_size=40, car_name='Default Name', model_name='Default Model', year=2000):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#         self.car_name = car_name
#         self.model_name = model_name
#         self.year = year
#
#     def describe_battery(self):
#         """Print a statement describing the battery size and car details."""
#         print(f'This car has a {self.battery_size}-KWh battery.')
#         print(f'Car Name: {self.car_name}, Model: {self.model_name}, Year: {self.year}')

# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery(car_name=make, model_name=model, year=year)
#
# Create an instance of ElectricCar
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()

"""FROM BOOK , but now we can describe the battery in as much detail as we want without cluttering the ElectricCar class"""
# class Car:
#     --snip--
#
# class Battery:
#     --snip--
#
#     def get_range(self):
#         """Prints a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f'This car can go about {range} miles on a full charge:')
#
# class ElectricCar(Car):
#     --snip--

# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# MODELING REAL- WORLD OBJECTS # CHECK IN BOOK #

# IMPORTING CLASSES #

"""As you add more functionality to your classes, your files can get long, even when you use inheritance and composition properly. 
In keeping with the overall philosophy of Python, you’ll want to keep your files as uncluttered as possible"""

# IMPORTING A SINGLE CLASS #

# MAKE A SEPARATE FILE CALLED car.py IN THIS SAME PYTHON FOLDER #
                        # car.py #
"""A class that can be used to represent a car.""" # THIS IS A MODULE LEVEL DOCSTRING BRIEFLY DESCRIBES THE CONTENTS OF THE MODULE #

# class Car:
#     """A simple attempt to represent a car"""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f'This car has {self.odometer_reading:,} miles on it.')
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles


  # my_car.py # THIS IS OUR CURRENT WORKING FILE #

# from car import Car
# my_new_car = Car('audi', 'a4', 2024)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

""" When you instead move the class to a module and import the module, you still get all the same functionality, but you keep your main program 
file clean and easy to read. """

# STORING MULTIPLE CLASSES IN A MODULE #

"""You can store as many classes as you need in a single module, although each class in a module should be related somehow. The classes 
Battery and ElectricCar both help represent cars, so let’s add them to the module car2.py."""
 # IN car2.py MODULE THERE ARE THREE CLASSES # Car AND Battery AND ElectricCar #

                    # car2.py #
# """A set of classes used to represent gas and electric cars. """
# """A class that can be used to represent a car.""" # THIS IS A MODULE LEVEL DOCSTRING BRIEFLY DESCRIBES THE CONTENTS OF THE MODULE #
# class Car:
#     """A simple attempt to represent a car"""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name"""
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
#     def read_odometer(self):
#         """Print a statement showing the car's mileage"""
#         print(f'This car has {self.odometer_reading:,} miles on it.')
#
#     def update_odometer(self, mileage):
#         """
#         Set the odometer reading to the given value.
#         Reject change if it attempts to roll the odometer back.
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('You can\'t roll back an odometer!')
#
#     def increment_odometer(self, miles):
#         """Add the given amount to the odometer reading."""
#         self.odometer_reading += miles
#
# class Battery:
#     """A simple attempt to model a battery for an electric car"""
#     def __init__(self, battery_size = 40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f'This car has a {self.battery_size}-KWh battery.')
#
#     def get_range(self):
#         """Prints a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f'This car can go about {range} miles on a full charge:')
#
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#

 # my_electric_car.py #  THIS IS OUR CURRENT WORKING FILE #

# from car2 import ElectricCar
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()

# IMPORTING MULTIPLE CLASSES FROM A MODULE #

"""You can import as many classes as you need into a program file. If we want to make a regular car and an electric car in the same 
file, we need to import both classes, Car and ElectricCar:"""

# from car2 import Car, ElectricCar
#
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

"""You import multiple classes from a module by separating each class with a comma. Once you’ve imported the necessary classes, 
you’re free to make as many instances of each class as you need."""

# IMPORTING AN ENTIRE MODULE #

"""You can also import an entire module and then access the classes you need using dot notation. This approach is simple and results in 
code that is easy to read. Because every call that creates an instance of a class includes the module name, you won’t have naming conflicts 
with any names used in the current file"""

# import car2
#
# my_mustang = car2.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
#
# my_leaf = car2.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# First we import the entire car module . We then access the classes we need through the module_name.ClassName syntax.

# IMPORTING ALL CLASSES FROM A MODULE #

# You can import every class from a module using the following syntax:
# from module_name import * #
"""This method is not recommended for two reasons. First, it’s helpful to be able to read the import statements at the top of a file and get 
a clear sense of which classes a program uses. With this approach it’s unclear which classes you’re using from the module. This approach 
can also lead to confusion with names in the file. If you accidentally import a class with the same name as something else in your program 
file, you can create errors that are hard to diagnose If you need to import many classes from a module, you’re better off importing the  entire 
module and using the module_name.ClassName syntax. You won’t see all the classes used at the top of the file, but you’ll see clearly  where 
the module is used in the program. You’ll also avoid the potential naming conflicts that can arise when you import every class in a module"""

# IMPORTING A MODULE INTO A MODULE #

""" Sometimes you’ll want to spread out your classes over several modules to keep any one file from growing too large and avoid storing 
unrelated classes in the same module. When you store your classes in several modules, you may find that a class in one module depends on a 
class in another module. When this happens, you can import the required class into the first module. For example, let’s store the Car 
class in one module and the ElectricCar and Battery classes in a separate module"""

# WE CREATE A FILE CALLED car3.py IN THAT FILE WE MENTION # from car import Car # IN FROM CAR WE MENTION ONLY CAR CODE ENDING WITH
# def increment_odometer(), AND IN THE SAME CAR3.PY FILE WE MENTION Battery CLASS CODE AND ElectricCar CLASS CODE NOT MODULE

     # car3.py #
# """A set of classes that can be used to represent electric cars."""
# from car import Car
#
# class Battery:
#     """A simple attempt to model a battery for an electric car"""
#     def __init__(self, battery_size = 40):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print(f'This car has a {self.battery_size}-KWh battery.')
#
#     def get_range(self):
#         """Prints a statement about the range this battery provides."""
#         if self.battery_size == 40:
#             range = 150
#         elif self.battery_size == 65:
#             range = 225
#         print(f'This car can go about {range} miles on a full charge:')
#
# class ElectricCar(Car):
#     """Models aspects of a car, specific to electric vehicles."""
#     def __init__(self, make, model, year):
#         """
#         Initialize attributes of the parent class.
#         Then initialize attributes specific to an electric car.
#         """
#         super().__init__(make, model, year)
#         self.battery = Battery()
#
#
"""The class ElectricCar needs access to its parent class Car, so we import ( car module it contains only car code into car3.py module) 
Car directly into the module. If we forget this line,  Python  will raise an error when we try to import the electric_car module. 
We also need to update the Car module so it contains only the Car class:"""

# trash.py #  THIS IS OUR CURRENT WORKING FILE #
# from car import Car
# from car3 import ElectricCar
#
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
#
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# USING ALIASES #

"""consider a program where you want to make a bunch of electric cars. It might get tedious to type (and read) ElectricCar over and
over again. You can give ElectricCar an alias in the import statement:"""

# from car3 import ElectricCar as EC
# my_leaf = EC('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# You can also give a module an alias
# import car3 as ca
# my_leaf = ca.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# THE PYTHON STANDARD LIBRARY #

"""The Python standard library is a set of modules included with every Python installation. Now that you have a basic understanding 
of how functions and classes work, you can start to use modules like these that other programmers have written. You can use any function 
or class in the standard library by including a simple import statement at the top of your file. Let’s look at one
module, random, which can be useful in modeling many real-world situations. One interesting function from the random module is randint(). 
This function takes two integer arguments and returns a randomly selected integer between (and including) those numbers.
Here’s how to generate a random number between 1 and 6:"""

# >> from random import randint
# >>> randint(1,6)
# 1

"""random Module: The random module contains a variety of functions for generating random numbers and performing random operations.
randint Function: randint is specifically a function (not a class) within the random module, and it returns a randomly selected integer 
between the two arguments provided."""

"""Another useful function is choice(). This function takes in a list or tuple and returns a randomly chosen element:"""
# >>> from random import choice   # CHOICE IS A FUNCTION #
# >>> players = ['pradeep kumar', 'rakesh', 'sharath', 'sai kumar']
# >>> first_up = choice(players)
# >>> first_up
# 'rakesh'
# >>>
 # HOW WE ARE SAYING CHOICE IS A FUNCTION #

""" Naming Convention:
In Python, functions are typically named using lowercase letters with underscores (_) separating words, if needed 
(e.g., choice, get_random_number). Classes, on the other hand, are typically named using CamelCase (e.g., Random, Car, ElectricCar).
Functions are called using parentheses and they perform an action. For example, choice(players) is a call to the choice function, 
which performs the action of selecting a random item from the list players. choice(players) is clearly performing an action 
(selecting a random item), which is characteristic of a function, not a class."""

# IN IMPORT STATEMENT HOW TO RECOGNIZE FUNCTIONS AND CLASSES #
# Functions
"""Functions are called using parentheses (). Example: randint(1, 6) — randint is a function, as indicated by the parentheses 
following its name. 

Classes:
Definition: A class is a blueprint for creating objects (a particular data structure). It defines attributes (data) and methods 
(functions) that the objects created from the class will have.
By convention, class names start with an uppercase letter. Functions: Recognized by their lowercase naming convention and the parentheses () 
used when they are called. They are often imported  like from module import function_name. Classes: Recognized by their capitalized 
naming convention. They are also imported like from module import ClassName."""

# STYLING YOUR CODE #

""" Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, and don’t use underscores. 
Instance and module names should be written in lowercase, with underscores between words. Every class should have a docstring immediately 
following the class definition. The docstring should be a brief description of what the class does, and you should follow the same formatting 
conventions you used for writing docstrings in functions. Each module should also have a docstring describing what the classes in a module 
can be used for. You can use blank lines to organize code, but don’t use them excessively. Within a class you can use one blank line between 
methods, and within a module you can use two blank lines to separate classes. If you need to import a module from the standard library and 
a module that you wrote, place the import statement for the standard library module first. Then add a blank line and the import statement for 
the module you wrote. In programs with multiple import statements, this convention makes it easier to see where the different modules used 
in the program come from."""
# Week 4
# Introduction to Object-Oriented Programming (OOP) Concepts

# Create a Class
# Create a class named MyClass, with a property named x:
class MyClass:
  x = 5 

# Create an object of MyClass called p1:
class MyClass:
  x = 5
p1 = MyClass()

# Create Object
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x) 

# The __init__() Function
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age) 

# The __str__() Function
# The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1) 

# The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 

# Object Methods
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

# The self Parameter
# Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc() 

# Modify Object Properties
# Set the age of p1 to 40:
p1.age = 40 

# Delete Object Properties
# Delete the age property from the p1 object:
del p1.age 

# Delete Objects
# Delete the p1 object:
del p1 

# The pass Statement
class Person:
  pass 


# Python Inheritance
# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname() 

# Create a Child Class
# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname() 

# Add the __init__() Function
# Add the __init__() function to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) 

# Use the super() Function
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname) 

# Add Properties
# Add a property called graduationyear to the Student class:
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019 

# Add Methods
# Add a method called welcome to the Student class:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear) 

# Polymorphism
#String
# For strings len() returns the number of characters:
x = "Hello World!"
print(len(x)) 

# Tuple
# For tuples len() returns the number of items in the tuple:
mytuple = ("apple", "banana", "cherry")
print(len(mytuple)) 

# Dictionary
# For dictionaries len() returns the number of key/value pairs in the dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict)) 

# Class Polymorphism
#For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
# Different classes with the same method:
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()

# Inheritance Class Polymorphism
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()

# Module
# To create a module just save the code you want in a file with the file extension .py:
# Save this code in a file named mymodule.py
def greeting(name):
  print("Hello, " + name)

# Use a Module
# Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")

# correct syntax for creating an alias for a module?
import mymodule as mx

# correct syntax of printing all variables and function names of the "mymodule" module?
import mymodule
print(dir(mymodule))

# correct syntax of importing only the person1 dictionary of the "mymodule" module?
from mymodule import person1

# Variables in Module
# Save this code in the file mymodule.py
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a) 

# Re-naming a Module
# Create an alias for mymodule called mx:
import mymodule as mx

a = mx.person1["age"]
print(a) 

# Built-in Modules
# Import and use the platform module:
import platform

x = platform.system()
print(x) 


# Using the dir() Function
# List all the defined names belonging to the platform module:
import platform

x = dir(platform)
print(x) 

# Import From Module
# The module named mymodule has one function and one dictionary:
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"])

# Python PIP - Package
# Using a Package
# Import and use "camelcase":
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt)) 

# Remove a Package
# Uninstall the package named "camelcase":
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip uninstall camelcase

# List Packages
# List installed packages:
C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>pip list


# Build a simple command-line application using Python Month 2: Data Analysis with Python
import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def analyze_data(data):
    """
    Perform basic analysis on the loaded data.
    """
    if data is None:
        return

    print("Data Analysis:")
    print("--------------")
    print("1. Summary Statistics")
    print("2. Data Head")
    print("3. Data Tail")
    print("4. Column Information")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("Summary Statistics:")
        print(data.describe())
    elif choice == '2':
        print("Data Head:")
        print(data.head())
    elif choice == '3':
        print("Data Tail:")
        print(data.tail())
    elif choice == '4':
        print("Column Information:")
        print(data.info())
    elif choice == '5':
        print("Exiting...")
        return
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

def main():
    print("Welcome to Simple Data Analysis Tool!")

    file_path = input("Enter the path to the CSV file: ")
    data = load_data(file_path)

    if data is not None:
        while True:
            analyze_data(data)
            continue_or_quit = input("Do you want to perform another analysis? (yes/no): ")
            if continue_or_quit.lower() != 'yes':
                break

    print("Thank you for using Simple Data Analysis Tool!")

if __name__ == "__main__":
    main()


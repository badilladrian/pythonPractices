# The areas in which Data Structures are applied:
# Compiler design
# Operating system
# Database Management System
# Statistical Analysis Package
# Numerical Analysis
# Graphics
# Artificial Intelligence
# Simulations
# Data structures used in the following areas:
# Network data model: Graph
# Hierarchical Data model: Trees
# Types of Data Structures:
# Python3 program to change the
# directory of file using os.chdir() method

# import os library
import os
import array as arr
from datetime import date

# change the current directory
# to specified directory
# os.chdir(r"C:\Users\Usuario\Documents\Adrian\Work\Python Practices\NewFolder")

# print("Directory changed")

# change the current working directory
# to specified path
# os.chdir('c:\\gfg_dir')

# varify the path using getcwd()
cwd = os.getcwd()

# print the current directory
print("Current working directory is:", cwd)


def message(msg):
    print(msg)


def messageData(data1, data2, description):
    print(description + "are in example: " + str(data1) + " " + str(data2))


message("Primitive Data Structures: ")

# Integer: It is used to represent numeric data, more specifically whole numbers
# from negative infinity to infinity
# Example:
a = 4
b = 5
c = -1
messageData(a, b, "Integers")

# Float: It stands for floating point number
# Example:
d = 1.1
e = 2.3
f = 9.3
messageData(d, e, "Floats")

# String: It is a collection of Alphabets, words or other characters.
# In python it can be created by using a pair of single or double quotes for the sequence
# Example:
x = 'Cake'
y = "Cookie"
messageData(x, y, "Strings")


# Certain operations can be performed on a string:
# We can use * to repeat the string for a specific number of times
# Example:
x*2
messageData(x, "", "String multiplied")

# String can be sliced, that is to select parts of the string
# Example:

# From Cookie to Coke
z1 = x[2:]
print(z1)

# Slicing
z2 = y[0] + y[1]
print(z2)

messageData(z1, z2, "Cookie Sliced")

# To capitalize the strings
# Example:
str.capitalize('cookie')

# To retrieve the length of the strings
# Example:
str1 = "Cake 4 U"
str2 = "404"
len(str1)

# To replace parts of a string with another string
# Example:
str1.replace('4 U', str2)

# Boolean: It is a built-in data type that can take the values TRUE or FALSE
message("Non - Primitive Data Structures:")

# Array: It is a compact way of collecting data types where all entries must be of the same data type.
# Syntax of writing an array in python:
a = arr.array("I", [3, 6, 9])
messageData(a, a[1], "This is an Array")
type(a)

# Linked list: List in Python is used to store collection
# of heterogeneous items. It is described using the square brackets[] and hold elements separated by comma
# Example:
x = []  # Empty list
type(x)
message("This is a List which is dif from an Array")
# The list can be classified into linear and non-linear data structures
# Linear data structures contain Stacks and queues
# Non-linear data structures contain Graphs and Trees

# Stack: It is a container of objects that can be inserted or
# removed according to LIFO(Last in First Out) pop() method is used during disposal in Python
# Example:
message("Stacks come alltogether in Python we can use pop append and other functions")
myStack = [1, 2, 3, 4, 5]
myStack.pop()  # Bottom -> 1 -> 2 -> 3 -> 4 -> 5 (Top)
myStack.pop()  # Bottom -> 1 -> 2 -> 3 -> 4 (Top)
print(myStack)

# Queue: It is a container of objects that can be inserted
# or removed according to FIFO(First in First Out)

# Graph: It is a data structure that consists of a finite set
# of vertices called nodes, and a finite set of ordered pair(u, v) called edges.

# It can be classified as direction and weight

# Binary Tree: Tree is a hierarchical data structure.
# Here each node has at most two children
# Binary Search Tree: It provides moderate access / search and moderate insertion / deletion

# Heap: It is a complete tree and is suitable to be stored in an array, it is either MIN or Max
# Hashing: Collection of items that are stored in a way that it becomes easy to find them is hashing

# Types of Data Structures
# Lists and tuples(In Python):
# Ordered sequence of values indexed by integer numbers. Tuples are immutable

# To initialize empty list / tuple:
# Syntax:
message("Lists and tuples(In Python): ")
message("Lists:")
myList = []

message("Tuples:")
myTuple = ("x", "y", "z")

message("To specify size of tuple/list:")
message("len(myList)")
len(myList)

# To get an element in position x in list/tuple:
# Syntax:
"x" in myTuple

message("myLis­tOr­Tup­le.i­nd­ex(­x)")
myTuple.index("x")
# - - If not found, throws a Value­Error exception")
# Number of occurrences of X in list/tuple:
# Syntax:

myList.count(x)
# Update an item of List/tuple:
# Syntax:

# Lists:
myList = ["o", "e", "f"]
message("Tuples: tuples are immutable!")
message("Remove element in position X of list/tuple:")
# Syntax:
message("Lists: del myList[x]")
message("Tuples: tuples are immutable!")
message("Concatenate two lists/tuples:")
message("Lists: myList1 + myList2")
message("Tuples: myTuple1 + myTuple2")
message("Concatenating a List and a Tuple will produce a TypeError exception")
# Insert element in position x of a list/tuple
# Syntax:
message("Lists: myLis­t.i­nse­rt(x, value)")
message("Tuples: tuples are immutable!")

message("Append “­x” to a list/tuple:")

myList.append("x")

message("Convert a list/tuple to tuple/list:")

# Syntax: List to Tuple: tuple(myList)

message("Tuple to List: ")
list(myTuple)

# Python3 code to demonstrate the
# working of set() on list and tuple

# initializing list
lis1 = [3, 4, 1, 4, 5]

# initializing tuple
tup1 = (3, 4, 1, 4, 5)

# Printing iterables before conversion
print("The list before conversion is : " + str(lis1))
print("The tuple before conversion is : " + str(tup1))

# Iterables after conversion are
# notice distinct and sorted elements
print("The list after conversion is : " + str(set(lis1)))
print("The tuple after conversion is : " + str(set(tup1)))


message("Now we enter to Data Collections: Sets! ")

message("It is an unordered collection with no duplicate elements." +
        "It supports mathematical operations like union, intersection, difference and symmetric difference.")
# To initialize an empty set:
mySet = set()
# Initialize a non-empty set
mySet.add("element1")
mySet.add("element2")
mySet.add("element3")
# To add element X to the set
mySet.add("element4")

# Remove element “­x” from a set:
mySet.remove("element3")
# - - If "­x" is not present, raises a KeyError
mySet.discard("element2")
# - - Removes the element, if present

# Remove every element from the set
mySet.clear()
# Check if “­x” is in the set
"x" in mySet


mySet1 = {'b', 'e', 'a'}
mySet2 = {'b', 'd', 'c', 'a'}

# Union of two sets
mySet1.union(mySet2)
mySet1 | mySet2

# Same elements of two sets
mySet1.intersection(mySet2)
mySet1 & mySet2

# Different of two sets
mySet1.difference(mySet2)
mySet1 - mySet2

# Equivalation  of two sets
mySet1.symmetric_difference(mySet2)
mySet1 ^ mySet2

# Set length
len(mySet2)

# Dictionaries
message("Now we have Dictionaries: ")

# It is an unordered set of key value pairs
myDict = {}
myDict["k"] = 4
myDict["k"] = 6
myDict["k"]
# - - If the key is not present, a KeyError is raised
# Check if the dictionary has key “­k” returns boolean
value = "k" in myDict
print(value)
# Get the list of keys. Keys are the primaryColumn of each value at dictionary
myDict.keys()

# size of dictionaries
len(myDict)

print(myDict)
# Delete element with key “­k” from the dictionary
del myDict["k"]

# Delete all the elements in the dictionary
myDict.clear()

# Python3 code to demonstrate the
# working of set() on dictionary

# initializing list
dic1 = {4: 'geeks', 1: 'for', 3: 'geeks'}

# Printing dictionary before conversion
# internally sorted
print("Dictionary before conversion is : " + str(dic1))

# Dictionary after conversion are
# notice lost keys
print("Dictionary after conversion is : " + str(set(dic1)))


# Python deletes unneeded objects (built-in types or class instances)
# automatically to free the memory space. The process by which Python
# periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.

# Python's garbage collector runs during program execution and is triggered when an object's
# reference count reaches zero. An object's reference count changes as the number of aliases
# that point to it changes.

# An object's reference count increases when it is assigned a new name or placed in a container
# (list, tuple, or dictionary). The object's reference count decreases when it's
# deleted with del, its reference is reassigned, or its reference goes out of scope.
# When an object's reference count reaches zero, Python collects it automatically.

a = 40      # Create object <40>
b = a       # Increase ref. count  of <40>
c = [b]     # Increase ref. count  of <40>
message("a=40, b=a. c=[b] This are their value in memory:")
print(id(a), id(b), id(c))

del a       # Decrease ref. count  of <40>
b = 100     # Decrease ref. count  of <40>
c[0] = -1   # Decrease ref. count  of <40>
message("del a, b=100, c[0]=-1")

print("A is now delete")
print(id(b), id(c))

# -|-*

# consider this scenario when creating functions about the return statement


def hello():
    return("hello")
# with return there is a string type out


def hello_noreturn():
    print("Hello World")


# here there is no return type, is none
whatDoIhavehere = hello()
print(whatDoIhavehere)
hello_noreturn()

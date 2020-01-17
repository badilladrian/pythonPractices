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

import array as arr


def message(msg):
    print(msg)


def message(data1, data2, description):
    print(description + "are in example: " + data1 + " " + data2)


message("Primitive Data Structures: ")

# Integer: It is used to represent numeric data, more specifically whole numbers
# from negative infinity to infinity
# Example:
a = 4
b = 5
c = -1
message(a, b, "Integers")

# Float: It stands for floating point number
# Example:
d = 1.1
e = 2.3
f = 9.3
message(d, e, "Floats")

# String: It is a collection of Alphabets, words or other characters.
# In python it can be created by using a pair of single or double quotes for the sequence
# Example:
x = 'Cake'
y = "Cookie"
message(x, y, "Strings")


# Certain operations can be performed on a string:
# We can use * to repeat the string for a specific number of times
# Example:
x*2
message(x, "", "String multiplied")

# String can be sliced, that is to select parts of the string
# Example:

# From Cookie to Coke
z1 = x[2:]
print(z1)

# Slicing
z2 = y[0] + y[1]
print(z2)

message(z1, z2, "Cookie Sliced")

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
message(a, a[1], "This is an Array")
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
myStack = []
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
myTuple = ()

message("To specify size of tuple/list:")
message("len(myList)")
len(myList)

# To get an element in position x in list/tuple:
# Syntax:
"x" in myTuple

message("myLis­tOr­Tup­le.i­nd­ex(­x) - - If not found, throws a Value­Error exception")
# Number of occurrences of X in list/tuple:
# Syntax:

myList.count(x)
# Update an item of List/tuple:
# Syntax:

# Lists:
myList[x] = "x"
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

message("Now we enter to Data Collections: Sets! ")

message("It is an unordered collection with no duplicate elements." +
        "It supports mathematical operations like union, intersection, difference and symmetric differ­ence.")
# To initialize an empty set:
mySet = set()
# Initialize a non-empty set
mySet = set("el­ement1", "elemen­t")
# To add element X to the set
mySet.add("x­")

# Remove element “­x” from a set:
mySet.remove("x­")
# - - If "­x" is not present, raises a KeyErorr
mySet.discard("x­")
# - - Removes the element, if present

# Remove every element from the set
mySet.clear()
# Check if “­x” is in the set
"x" in mySet



# Set length
len(mySet)

# Dictionaries
message("Now we have Dictionaries: ")

# It is an unordered set of key value pairs
myDict = {}
myDict["k­"] = 1
myDict["k­"] = 5
myDict["k­"]
# - - If the key is not present, a KeyError is raised
# Check if the dictionary has key “­k”
"k" in myDict

# Get the list of keys. Keys are the primaryColumn of each value at dictionary
myDict.keys()

# size of dictionaries
len(myDict)

# Delete element with key “­k” from the dictionary
del myDict["k­"]

# Delete all the elements in the dictionary
myDict.clear()

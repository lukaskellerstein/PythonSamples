# ----------------------------------
# ----------------------------------
# TUPLE (IMMUTABLE SEQUENCE) - In Python, tuples are immutable, meaning they cannot be modified after creation.
# Tuples are faster than lists and are used for fixed collections of items.
# ----------------------------------
# ----------------------------------
tuple1 = ("aaa", "bbb", "ccc")

# Access by index - O(1)
some_item = tuple1[2]

# Access by key (dictionary-style)
# Not possible with tuples

# ----------------------------------
# CREATING TUPLES
# ----------------------------------

# Empty tuple
empty_tuple = ()

# Single-element tuple (note the comma!)
single_element = ("aaa",)

# Tuple packing (without parentheses)
packed_tuple = "aaa", "bbb", "ccc"

# Tuple unpacking
a, b, c = tuple1

# ----------------------------------
# IMMUTABILITY - Tuples cannot be modified
# ----------------------------------

# The following operations are NOT possible with tuples:
# tuple1.append("ddd")     # AttributeError: 'tuple' object has no attribute 'append'
# tuple1.insert(1, "new")  # AttributeError: 'tuple' object has no attribute 'insert'
# tuple1.pop(0)            # AttributeError: 'tuple' object has no attribute 'pop'
# tuple1.remove("bbb")     # AttributeError: 'tuple' object has no attribute 'remove'
# tuple1[2] = "eee"        # TypeError: 'tuple' object does not support item assignment

# ----------------------------------
# WORKAROUNDS FOR "MODIFYING" TUPLES
# ----------------------------------

# If you need to "modify" a tuple, you must create a new one

# Add an element - O(n), creates a new tuple
tuple2 = tuple1 + ("ddd",)

# Insert at a specific position - O(n), creates a new tuple
tuple3 = tuple1[:1] + ("new_value",) + tuple1[1:]

# Remove by index - O(n), creates a new tuple
tuple4 = tuple1[:0] + tuple1[1:]  # Remove first item

# Remove by value - O(n), creates a new tuple
tuple5 = tuple(item for item in tuple1 if item != "bbb")

# Update (replace an element by index) - O(n), creates a new tuple
tuple6 = tuple1[:2] + ("eee",) + tuple1[3:]

# Convert to list, modify, convert back - O(n)
temp_list = list(tuple1)
temp_list[0] = "zzz"
tuple7 = tuple(temp_list)

# ----------------------------------
# OPERATIONS (READ-ONLY)
# ----------------------------------

# Count occurrences - O(n)
count = tuple1.count("aaa")

# Find index of element - O(n), raises ValueError if not found
index = tuple1.index("bbb")

# Length - O(1)
length = len(tuple1)

# Membership test - O(n)
exists = "ccc" in tuple1

# Concatenation - O(n+m), creates a new tuple
combined = tuple1 + ("xxx", "yyy")

# Repetition - O(n*k), creates a new tuple
repeated = tuple1 * 2  # ("aaa", "bbb", "ccc", "aaa", "bbb", "ccc")

# Slicing - O(k), creates a new tuple
sub_tuple = tuple1[1:3]  # ("bbb", "ccc")

# ----------------------------------
# SORT (Creates a sorted list, not tuple)
# ----------------------------------

# Tuples don't have a sort method, but you can create a sorted list
sorted_list = sorted(tuple1)  # O(n log n), returns a list

# To get a sorted tuple, convert back
sorted_tuple = tuple(sorted(tuple1))  # O(n log n)

# ----------------------------------
# SEARCH
# ----------------------------------

# 1 - For-loop - Brute-force search - O(n)
result = ""
for item in tuple1:
    if item == "bbb":
        result = item
        break

# 2 - Find - O(n), can use a generator expression
aaa = next((x for x in tuple1 if x == "bbb"), None)

# 3 - Filter - O(n), returns a list with all matching elements
bbb = [x for x in tuple1 if x == "bbb"]

# To get a tuple result from filter
bbb_tuple = tuple(x for x in tuple1 if x == "bbb")

# ----------------------------------
# NESTED TUPLES
# ----------------------------------

# Tuples can contain other tuples
nested = (("a", "b"), ("c", "d"), ("e", "f"))

# Access nested elements
first_inner = nested[0]  # ("a", "b")
element = nested[0][1]   # "b"

# ----------------------------------
# NAMED TUPLES (More readable alternative)
# ----------------------------------

from collections import namedtuple

# Define a named tuple type
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
person1 = Person("Alice", 30, "New York")
person2 = Person(name="Bob", age=25, city="Los Angeles")

# Access by index (like regular tuples)
name = person1[0]  # "Alice"

# Access by name (more readable)
age = person1.age  # 30

# Named tuples are still immutable
# person1.age = 31  # AttributeError: can't set attribute

# ----------------------------------
# USE CASES FOR TUPLES
# ----------------------------------

# 1. Returning multiple values from functions
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()

# 2. Dictionary keys (tuples are hashable, lists are not)
location_data = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles"
}

# 3. Protecting data from modification
immutable_config = ("production", "https://api.example.com", 443)

# 4. Slight performance advantage over lists for fixed data
# Tuples are faster to create and iterate over

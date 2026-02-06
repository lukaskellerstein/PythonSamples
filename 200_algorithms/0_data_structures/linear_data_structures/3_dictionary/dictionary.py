# ----------------------------------
# ----------------------------------
# DICTIONARY (HASH MAP / ASSOCIATIVE ARRAY)
# Dictionaries store key-value pairs and are implemented using hash tables.
# Keys must be immutable (hashable) types. Values can be any type.
# Since Python 3.7+, dictionaries maintain insertion order.
# ----------------------------------
# ----------------------------------
dict1 = {"name": "Alice", "age": 30, "city": "New York"}

# Access by index - NOT POSSIBLE (use keys instead)
# some_value = dict1[0]  # KeyError

# Access by key - O(1) average case, O(n) worst case due to hash collisions
name = dict1["name"]

# Safe access with get (returns None if key doesn't exist) - O(1) average case
age = dict1.get("age")
country = dict1.get("country")  # Returns None
country_default = dict1.get("country", "USA")  # Returns "USA" if key doesn't exist

# ----------------------------------
# CREATING DICTIONARIES
# ----------------------------------

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()

# Dictionary with curly braces
person = {"name": "Bob", "age": 25}

# Dictionary from list of tuples
pairs = [("a", 1), ("b", 2), ("c", 3)]
dict_from_pairs = dict(pairs)

# Dictionary comprehension
squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Using keyword arguments (keys must be valid identifiers)
person2 = dict(name="Charlie", age=35, city="Boston")

# From two lists (zip them together)
keys = ["a", "b", "c"]
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))

# Using dict.fromkeys (all values set to same default)
default_dict = dict.fromkeys(["a", "b", "c"], 0)  # {'a': 0, 'b': 0, 'c': 0}

# ----------------------------------
# CRUD OPERATIONS
# ----------------------------------

# Add / Update (same syntax for both) - O(1) average case
dict1["email"] = "alice@example.com"  # Add new key
dict1["age"] = 31  # Update existing key

# Update multiple key-value pairs - O(len(other_dict))
dict1.update({"phone": "123-456-7890", "country": "USA"})
dict1.update([("zip", "10001")])  # Can also use list of tuples
dict1.update(state="NY")  # Can also use keyword arguments

# Add key only if it doesn't exist (setdefault) - O(1) average case
# Returns the value if key exists, otherwise sets it to default and returns default
dict1.setdefault("salary", 50000)  # Adds "salary": 50000
dict1.setdefault("age", 40)  # Returns 31 (doesn't change existing value)

# Remove by key (raises KeyError if key doesn't exist) - O(1) average case
del dict1["zip"]

# Pop (remove and return value, can provide default) - O(1) average case
email = dict1.pop("email")  # Removes and returns "alice@example.com"
middle_name = dict1.pop("middle_name", "N/A")  # Returns "N/A" (key doesn't exist)

# Pop arbitrary key-value pair (LIFO since Python 3.7+) - O(1)
last_item = dict1.popitem()  # Removes and returns last inserted key-value pair

# Clear all items - O(n)
dict_copy = dict1.copy()
dict_copy.clear()

# ----------------------------------
# ACCESSING KEYS, VALUES, AND ITEMS
# ----------------------------------

sample_dict = {"a": 1, "b": 2, "c": 3}

# Get all keys - O(1) to create view, O(n) to iterate
keys = sample_dict.keys()  # dict_keys(['a', 'b', 'c'])
keys_list = list(sample_dict.keys())

# Get all values - O(1) to create view, O(n) to iterate
values = sample_dict.values()  # dict_values([1, 2, 3])
values_list = list(sample_dict.values())

# Get all key-value pairs - O(1) to create view, O(n) to iterate
items = sample_dict.items()  # dict_items([('a', 1), ('b', 2), ('c', 3)])
items_list = list(sample_dict.items())

# Note: keys(), values(), and items() return views that reflect changes to the dictionary

# ----------------------------------
# MEMBERSHIP TESTING
# ----------------------------------

# Check if key exists - O(1) average case
has_key = "a" in sample_dict  # True
not_has_key = "z" not in sample_dict  # True

# Check if value exists (slower) - O(n)
has_value = 2 in sample_dict.values()

# ----------------------------------
# ITERATION
# ----------------------------------

person_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Iterate over keys (default)
for key in person_dict:
    print(key)

# Iterate over keys (explicit)
for key in person_dict.keys():
    print(key)

# Iterate over values
for value in person_dict.values():
    print(value)

# Iterate over key-value pairs
for key, value in person_dict.items():
    print(f"{key}: {value}")

# ----------------------------------
# DICTIONARY COMPREHENSIONS
# ----------------------------------

# Create dictionary from range
squares_dict = {x: x**2 for x in range(1, 6)}  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter while creating
evens = {x: x**2 for x in range(10) if x % 2 == 0}

# Transform existing dictionary
original = {"a": 1, "b": 2, "c": 3}
doubled = {k: v * 2 for k, v in original.items()}

# Swap keys and values
swapped = {v: k for k, v in original.items()}

# Conditional values
conditional = {k: "even" if v % 2 == 0 else "odd" for k, v in original.items()}

# ----------------------------------
# MERGING DICTIONARIES
# ----------------------------------

dict_a = {"a": 1, "b": 2}
dict_b = {"b": 3, "c": 4}

# Using update (modifies dict_a in place)
dict_a_copy = dict_a.copy()
dict_a_copy.update(dict_b)  # {'a': 1, 'b': 3, 'c': 4} - dict_b values overwrite

# Using unpacking (Python 3.5+)
merged1 = {**dict_a, **dict_b}  # {'a': 1, 'b': 3, 'c': 4}

# Using union operator (Python 3.9+)
merged2 = dict_a | dict_b  # {'a': 1, 'b': 3, 'c': 4}

# In-place union (Python 3.9+)
dict_a_copy = dict_a.copy()
dict_a_copy |= dict_b  # Modifies dict_a_copy in place

# ----------------------------------
# NESTED DICTIONARIES
# ----------------------------------

# Dictionary of dictionaries
users = {
    "user1": {"name": "Alice", "age": 30},
    "user2": {"name": "Bob", "age": 25},
    "user3": {"name": "Charlie", "age": 35}
}

# Access nested values
alice_name = users["user1"]["name"]

# Add to nested dictionary
users["user1"]["email"] = "alice@example.com"

# Iterate over nested dictionaries
for user_id, user_info in users.items():
    print(f"{user_id}: {user_info['name']}, age {user_info['age']}")

# ----------------------------------
# SORTING DICTIONARIES
# ----------------------------------

unsorted_dict = {"c": 3, "a": 1, "b": 2}

# Sort by keys - O(n log n)
sorted_by_keys = dict(sorted(unsorted_dict.items()))  # {'a': 1, 'b': 2, 'c': 3}

# Sort by values - O(n log n)
sorted_by_values = dict(sorted(unsorted_dict.items(), key=lambda item: item[1]))

# Sort in reverse
reverse_sorted = dict(sorted(unsorted_dict.items(), reverse=True))

# Get sorted keys only
sorted_keys = sorted(unsorted_dict.keys())

# Get sorted values only
sorted_values = sorted(unsorted_dict.values())

# ----------------------------------
# SEARCH / FILTER
# ----------------------------------

data = {"apple": 5, "banana": 3, "cherry": 8, "date": 2}

# 1 - Find key by value (first match) - O(n)
key_for_value = next((k for k, v in data.items() if v == 8), None)

# 2 - Find all keys matching condition - O(n)
keys_above_3 = [k for k, v in data.items() if v > 3]

# 3 - Filter dictionary - O(n)
filtered = {k: v for k, v in data.items() if v > 3}

# 4 - Find if any key starts with certain letter
starts_with_c = any(k.startswith("c") for k in data.keys())

# 5 - Find maximum value and its key - O(n)
max_key = max(data, key=data.get)  # 'cherry'
max_value = max(data.values())  # 8
max_item = max(data.items(), key=lambda x: x[1])  # ('cherry', 8)

# ----------------------------------
# DEFAULTDICT (FROM COLLECTIONS)
# ----------------------------------

from collections import defaultdict

# Regular dict raises KeyError for missing keys
# defaultdict provides default values for missing keys

# defaultdict with int (default value is 0)
counter = defaultdict(int)
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    counter[word] += 1  # No need to check if key exists
# Result: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})

# defaultdict with list (default value is [])
groups = defaultdict(list)
pairs = [("fruit", "apple"), ("vegetable", "carrot"), ("fruit", "banana")]
for category, item in pairs:
    groups[category].append(item)
# Result: defaultdict(<class 'list'>, {'fruit': ['apple', 'banana'], 'vegetable': ['carrot']})

# defaultdict with custom function
def default_value():
    return "N/A"

custom_default = defaultdict(default_value)
custom_default["key1"]  # Returns "N/A"

# ----------------------------------
# ORDEREDDICT (FROM COLLECTIONS)
# ----------------------------------

from collections import OrderedDict

# Note: Since Python 3.7+, regular dicts maintain insertion order
# OrderedDict is mainly useful for:
# 1. Backwards compatibility
# 2. Equality comparison considers order
# 3. move_to_end() method

ordered = OrderedDict([("a", 1), ("b", 2), ("c", 3)])

# Move key to end
ordered.move_to_end("a")  # OrderedDict([('b', 2), ('c', 3), ('a', 1)])

# Move key to beginning
ordered.move_to_end("c", last=False)  # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# Equality comparison considers order (unlike regular dicts in Python 3.8+)
dict1 = OrderedDict([("a", 1), ("b", 2)])
dict2 = OrderedDict([("b", 2), ("a", 1)])
are_equal = dict1 == dict2  # False (different order)

# ----------------------------------
# COUNTER (FROM COLLECTIONS)
# ----------------------------------

from collections import Counter

# Counter is a dict subclass for counting hashable objects
words_list = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_counts = Counter(words_list)  # Counter({'apple': 3, 'banana': 2, 'cherry': 1})

# Count characters in a string
char_counts = Counter("hello world")  # Counter({'l': 3, 'o': 2, 'h': 1, ...})

# Most common elements - O(n log k) where k is the number of elements requested
most_common = word_counts.most_common(2)  # [('apple', 3), ('banana', 2)]

# Arithmetic operations
counter1 = Counter({"a": 3, "b": 1})
counter2 = Counter({"a": 1, "b": 2})

add = counter1 + counter2  # Counter({'a': 4, 'b': 3})
subtract = counter1 - counter2  # Counter({'a': 2}) - only positive counts
intersection = counter1 & counter2  # Counter({'a': 1, 'b': 1}) - minimum
union = counter1 | counter2  # Counter({'a': 3, 'b': 2}) - maximum

# ----------------------------------
# COMMON OPERATIONS
# ----------------------------------

sample = {"a": 1, "b": 2, "c": 3}

# Length (number of key-value pairs) - O(1)
length = len(sample)

# Copy (shallow copy) - O(n)
shallow_copy = sample.copy()
shallow_copy2 = dict(sample)

# Deep copy (for nested dictionaries)
import copy
nested = {"a": {"b": 1}}
deep_copy = copy.deepcopy(nested)

# Check if dictionary is empty - O(1)
is_empty = len(sample) == 0
is_empty2 = not bool(sample)

# Get all unique values - O(n)
unique_values = set(sample.values())

# Invert dictionary (swap keys and values) - O(n)
# Only works if all values are unique and hashable
inverted = {v: k for k, v in sample.items()}

# ----------------------------------
# PRACTICAL USE CASES
# ----------------------------------

# 1. Counting occurrences
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1

# 2. Grouping data
students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob", "grade": "B"},
    {"name": "Charlie", "grade": "A"}
]
by_grade = {}
for student in students:
    grade = student["grade"]
    if grade not in by_grade:
        by_grade[grade] = []
    by_grade[grade].append(student["name"])

# 3. Caching / Memoization
cache = {}
def expensive_function(n):
    if n in cache:
        return cache[n]
    result = n ** 2  # Expensive computation
    cache[n] = result
    return result

# 4. Configuration settings
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "mydb"
    },
    "api": {
        "timeout": 30,
        "max_retries": 3
    }
}

# 5. JSON-like data structures
user_data = {
    "id": 123,
    "username": "alice",
    "profile": {
        "age": 30,
        "interests": ["reading", "coding", "hiking"]
    }
}

# ----------------------------------
# PERFORMANCE NOTES
# ----------------------------------

# Dictionaries are ideal when you need:
# - O(1) key-based access (average case)
# - Key-value associations
# - Fast membership testing for keys
# - Maintaining insertion order (Python 3.7+)

# Use dictionaries instead of lists when:
# - You need to look up values by meaningful keys (not indices)
# - You need fast membership testing
# - You want to associate data (key-value pairs)

# Dictionary keys must be:
# - Immutable (hashable): strings, numbers, tuples (of immutable elements)
# - NOT lists, sets, or other dictionaries

# Valid keys:
valid_keys = {
    "string": 1,
    42: 2,
    (1, 2): 3,
    frozenset([1, 2]): 4
}

# Invalid keys (will raise TypeError):
# invalid = {
#     [1, 2]: "value",  # Lists are not hashable
#     {1, 2}: "value"   # Sets are not hashable
# }

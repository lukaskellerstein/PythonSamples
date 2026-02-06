# ----------------------------------
# ----------------------------------
# SET (UNORDERED COLLECTION OF UNIQUE ELEMENTS)
# Sets are mutable, unordered, and do not allow duplicate values.
# Sets are implemented using hash tables, providing fast membership testing.
# ----------------------------------
# ----------------------------------
set1 = {"aaa", "bbb", "ccc"}

# Access by index - NOT POSSIBLE (sets are unordered)
# some_item = set1[0]  # TypeError: 'set' object is not subscriptable

# Access by key (dictionary-style) - NOT POSSIBLE
# Sets don't support indexing or key-based access

# ----------------------------------
# CREATING SETS
# ----------------------------------

# Empty set (Note: {} creates an empty dict, not a set!)
empty_set = set()

# Set from list (automatically removes duplicates)
set2 = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set with curly braces
set3 = {1, 2, 3}

# Set from string (each character becomes an element)
char_set = set("hello")  # {'h', 'e', 'l', 'o'}

# Set from other iterables
tuple_set = set((1, 2, 3))
range_set = set(range(5))  # {0, 1, 2, 3, 4}

# ----------------------------------
# CRUD OPERATIONS
# ----------------------------------

# Add (single element) - O(1) average case, O(n) worst case due to hash collisions
set1.add("ddd")

# Add duplicates are ignored
set1.add("aaa")  # No change, "aaa" already exists

# Update (add multiple elements) - O(len(iterable)) average case
set1.update(["eee", "fff"])
set1.update({"ggg", "hhh"})

# Remove (raises KeyError if element doesn't exist) - O(1) average case
set1.remove("bbb")

# Discard (no error if element doesn't exist) - O(1) average case
set1.discard("zzz")  # No error even though "zzz" doesn't exist

# Pop (removes and returns arbitrary element) - O(1)
# Note: Since sets are unordered, you can't predict which element will be removed
removed_item = set1.pop()

# Clear (remove all elements) - O(n)
set_copy = set1.copy()
set_copy.clear()

# ----------------------------------
# NO INDEXING OR UPDATING BY POSITION
# ----------------------------------

# Sets are unordered, so you can't:
# - Access elements by index
# - Update elements by index
# - Slice sets

# To "update" an element, you must remove the old one and add a new one
if "ccc" in set1:
    set1.remove("ccc")
    set1.add("ccc_updated")

# ----------------------------------
# MEMBERSHIP TESTING
# ----------------------------------

# Check if element exists - O(1) average case (This is the main advantage of sets!)
exists = "aaa" in set1
not_exists = "zzz" not in set1

# ----------------------------------
# SET OPERATIONS (MATHEMATICAL SET THEORY)
# ----------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (all elements from both sets) - O(len(set_a) + len(set_b))
union1 = set_a | set_b  # {1, 2, 3, 4, 5, 6, 7, 8}
union2 = set_a.union(set_b)

# Intersection (elements common to both sets) - O(min(len(set_a), len(set_b)))
intersection1 = set_a & set_b  # {4, 5}
intersection2 = set_a.intersection(set_b)

# Difference (elements in set_a but not in set_b) - O(len(set_a))
difference1 = set_a - set_b  # {1, 2, 3}
difference2 = set_a.difference(set_b)

# Symmetric Difference (elements in either set but not both) - O(len(set_a) + len(set_b))
sym_diff1 = set_a ^ set_b  # {1, 2, 3, 6, 7, 8}
sym_diff2 = set_a.symmetric_difference(set_b)

# ----------------------------------
# IN-PLACE SET OPERATIONS (MODIFY ORIGINAL SET)
# ----------------------------------

set_c = {1, 2, 3}
set_d = {3, 4, 5}

# In-place union
set_c_copy = set_c.copy()
set_c_copy |= set_d  # or set_c_copy.update(set_d)

# In-place intersection
set_c_copy = set_c.copy()
set_c_copy &= set_d  # or set_c_copy.intersection_update(set_d)

# In-place difference
set_c_copy = set_c.copy()
set_c_copy -= set_d  # or set_c_copy.difference_update(set_d)

# In-place symmetric difference
set_c_copy = set_c.copy()
set_c_copy ^= set_d  # or set_c_copy.symmetric_difference_update(set_d)

# ----------------------------------
# SET COMPARISONS
# ----------------------------------

set_x = {1, 2, 3}
set_y = {1, 2, 3, 4, 5}
set_z = {1, 2, 3}

# Subset (all elements of set_x are in set_y) - O(len(set_x))
is_subset = set_x <= set_y  # True
is_subset2 = set_x.issubset(set_y)  # True

# Proper subset (subset but not equal) - O(len(set_x))
is_proper_subset = set_x < set_y  # True

# Superset (set_y contains all elements of set_x) - O(len(set_y))
is_superset = set_y >= set_x  # True
is_superset2 = set_y.issuperset(set_x)  # True

# Proper superset (superset but not equal) - O(len(set_y))
is_proper_superset = set_y > set_x  # True

# Disjoint (no common elements) - O(min(len(set_x), len(set_y)))
are_disjoint = set_x.isdisjoint({6, 7, 8})  # True

# Equality - O(len(set_x))
are_equal = set_x == set_z  # True

# ----------------------------------
# ITERATION
# ----------------------------------

# For-loop (order is not guaranteed)
for item in set1:
    print(item)

# List comprehension
uppercase = {item.upper() for item in set1 if isinstance(item, str)}

# ----------------------------------
# SORT (Sets are unordered, but you can create a sorted list)
# ----------------------------------

set_numbers = {5, 2, 8, 1, 9}

# Get sorted list from set - O(n log n)
sorted_list = sorted(set_numbers)  # [1, 2, 5, 8, 9]

# Reverse sorted
reverse_sorted = sorted(set_numbers, reverse=True)  # [9, 8, 5, 2, 1]

# ----------------------------------
# SEARCH
# ----------------------------------

set_example = {"apple", "banana", "cherry", "date"}

# 1 - Membership test (fastest) - O(1) average case
exists = "banana" in set_example

# 2 - For-loop search (when you need to perform operations) - O(n)
result = None
for item in set_example:
    if item.startswith("b"):
        result = item
        break

# 3 - Filter with comprehension - O(n)
filtered = {x for x in set_example if len(x) > 5}

# 4 - Convert to list and use list methods - O(n)
as_list = list(set_example)
first_match = next((x for x in as_list if "e" in x), None)

# ----------------------------------
# FROZEN SETS (IMMUTABLE SETS)
# ----------------------------------

# Frozen sets are immutable versions of sets
# They can be used as dictionary keys or elements of other sets

frozen = frozenset([1, 2, 3, 4])

# Can't modify frozen sets
# frozen.add(5)  # AttributeError: 'frozenset' object has no attribute 'add'

# Can use frozen sets as dictionary keys
dict_with_frozen_keys = {
    frozenset([1, 2]): "value1",
    frozenset([3, 4]): "value2"
}

# Can use frozen sets as elements in other sets
set_of_frozen_sets = {
    frozenset([1, 2]),
    frozenset([3, 4])
}

# All read-only operations work on frozen sets
frozen_union = frozen | frozenset([5, 6])
is_in_frozen = 2 in frozen

# ----------------------------------
# COMMON OPERATIONS
# ----------------------------------

set_misc = {1, 2, 3, 4, 5}

# Length - O(1)
length = len(set_misc)

# Copy (shallow copy) - O(n)
set_copy = set_misc.copy()

# Convert to list - O(n)
list_from_set = list(set_misc)

# Convert to tuple - O(n)
tuple_from_set = tuple(set_misc)

# Min and Max (only for comparable elements) - O(n)
minimum = min(set_misc)
maximum = max(set_misc)

# Sum (only for numeric elements) - O(n)
total = sum(set_misc)

# ----------------------------------
# PRACTICAL USE CASES
# ----------------------------------

# 1. Remove duplicates from a list
list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_list = list(set(list_with_dupes))

# 2. Fast membership testing
valid_usernames = {"alice", "bob", "charlie"}
if "alice" in valid_usernames:  # O(1) instead of O(n) with list
    print("Valid user")

# 3. Finding unique characters in a string
text = "hello world"
unique_chars = set(text)  # {'h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'}

# 4. Set operations for data analysis
customers_a = {"alice", "bob", "charlie"}
customers_b = {"bob", "charlie", "david"}

# Customers in both stores
both_stores = customers_a & customers_b

# Customers in only one store
exclusive_customers = customers_a ^ customers_b

# All unique customers
all_customers = customers_a | customers_b

# 5. Removing unwanted values efficiently
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
remove_these = {2, 4, 6, 8}
result_set = numbers - remove_these  # {1, 3, 5, 7, 9, 10}

# ----------------------------------
# PERFORMANCE NOTES
# ----------------------------------

# Sets are ideal when you need:
# - O(1) membership testing (vs O(n) for lists)
# - Automatic duplicate removal
# - Mathematical set operations
# - No need for ordering or indexing

# Use lists instead when you need:
# - Ordered elements
# - Index-based access
# - Duplicate values
# - Specific iteration order

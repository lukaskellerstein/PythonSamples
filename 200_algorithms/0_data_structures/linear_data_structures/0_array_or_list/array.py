# ----------------------------------
# ----------------------------------
# LIST (DYNAMIC ARRAY) - In Python, lists can grow dynamically.
# Don't confuse Python's list with a fixed-size array in languages like C# or Java.
# ----------------------------------
# ----------------------------------
arr1 = ["aaa", "bbb", "ccc"]

# Access by index - O(1)
some_item = arr1[2]

# Access by key (dictionary-style)
# Not possible with lists

# ----------------------------------
# CRUD OPERATIONS
# ----------------------------------

# Add (to the end) - O(1) or O(n) if resizing occurs due to capacity limits
arr1.append("ddd")

# Insert (at index) - O(n) because elements after the insertion point must be shifted
arr1.insert(1, "new_value")

# Remove by index - O(n), elements after the removal point are shifted
# Example: Remove the first item (index 0)
arr1.pop(0)

# Remove by value - O(n), requires a linear search to find the element
arr1.remove("bbb")  

# Update (replace an element by index) - O(1)
arr1[2] = "eee"

# ----------------------------------
# SORT
# ----------------------------------

# Sort - In Python, this uses Timsort, which has a time complexity of O(n log n) on average.
# Timsort is stable and optimized for real-world data patterns.
arr1.sort()

# ----------------------------------
# SEARCH
# ----------------------------------

# 1 - For-loop - Brute-force search - O(n)
result = ""
for item in arr1:
    if item == "ddd":
        result = item
        break

# 2 - Find - O(n), can use a list comprehension or generator expression
aaa = next((x for x in arr1 if x == "ddd"), None)

# 3 - Filter - O(n), returns a new list with all matching elements
bbb = [x for x in arr1 if x == "ddd"]

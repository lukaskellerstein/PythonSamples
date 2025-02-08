# Create a dictionary
ht = {}

# Add elements (similar to `set` method)
ht["Canada"] = 300
ht["France"] = 100
ht["Spain"] = 110

# Get elements (similar to `get` method)
print(ht.get("Canada"))  # Output: 300
print(ht.get("France"))  # Output: 100
print(ht.get("Spain"))   # Output: 110

# Remove an element (similar to `remove` method)
ht.pop("Spain", None)  # Remove "Spain" from the dictionary

# Try to get the removed element
print(ht.get("Spain"))  # Output: None

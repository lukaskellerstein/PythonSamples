from collections import defaultdict

# -----------------------------------------------------
# Dictionary with default value (None)
# -----------------------------------------------------
table = defaultdict(lambda: 0)
print(table)

# Get value
a = table["BLABLABLA"]
print(a)  # -< will return the default value

# Assign values
table["A"] = 1
table["B"] = 2

# iteration
for k1, v1 in table.items():
    print(k1)
    print(v1)

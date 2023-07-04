from collections import defaultdict

# -----------------------------------------------------
# Dictionary with multi index
# -----------------------------------------------------
table = defaultdict(lambda: defaultdict(list))

print(table)

# Assign values
table["CL"]["CLX0"].extend([0, 0, 0, 0])
table["CL"]["CLX1"].append(1)
table["CA"]["A"] = [0, 0, 0, 0]


# iteration
for k1, v1 in table.items():
    print(k1)
    for k2, v2 in v1.items():
        print(f"{k2} - {v2}")

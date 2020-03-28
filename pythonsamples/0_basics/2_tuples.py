# --------------------------------------------------
# TUPLES -> are immutable
#
# Tuples are faster and consume less memory
# --------------------------------------------------

myTuple = (1, 2, 3, 4)
myTupleStrings = ("a", "b", "c")


# ------------------------------------
# Iterate
# ------------------------------------

for item in myTupleStrings:
    print(item)

# ------------------------------------
# Operations
# ------------------------------------

# add
# CANNOT

# get
myValue1 = myTuple[0]

# slice
mySlice1 = myTuple[:2]
print(mySlice1)
mySlice2 = myTuple[2:]
print(mySlice2)

# remove
# CANNOT


# ------------------------------------
# Packing vs. Unpacking
# ------------------------------------

# packing into tuple
a = "A"
b = "B"
c = "C"

t = (a, b, c)
print(t)

# unpacking from tuple
(d, e, f) = t
print(d)
print(e)
print(f)

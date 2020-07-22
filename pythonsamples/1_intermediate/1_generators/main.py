
# -----------------------------------------------------
# GENERATORS = memory effective iterator 
# -----------------------------------------------------

# generator version ----------------------------------
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(firstn(1000000).__sizeof__()) # ------> 96
print(type(firstn(1000000)))





# non-generator version ----------------------------------
# will consume huge amount of resources
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


print(firstn(1000000).__sizeof__()) # ------> 8697440
print(type(firstn(1000000)))
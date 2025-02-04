def are_same(arr1, arr2):
    # Check if the arrays have the same length
    if len(arr1) != len(arr2):
        return False

    # Compare each element in both arrays
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False  # Early exit on mismatch

    return True  # Arrays are the same if no mismatches were found


# Test cases
arr1 = ["aaa", "bbb", "ccc", "ddd", "eee"]
arr2 = ["aaa", "bbb", "ccc", "ddd", "eee"]
arr3 = ["aaa", "bbb", "ccc", "ddd", "eee", "fff"]

print(are_same(arr1, arr2))  # Output: True
print(are_same(arr1, arr3))  # Output: False

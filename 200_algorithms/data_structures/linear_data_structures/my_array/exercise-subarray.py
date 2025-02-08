# ----------------------------------
# IS one array a subarray of another array ?
#
# Subarray is a contiguous sequence of elements within an array.
# order matters
# ----------------------------------
def is_subarray(arr1, arr2):
    # Step 1: Get the lengths of both arrays
    length1 = len(arr1)
    length2 = len(arr2)

    # Step 2: Handle edge cases
    if length1 == 0:
        # An empty array is considered a subarray of any array
        return True

    if length1 > length2:
        # If arr1 is longer than arr2, it cannot be a subarray
        return False

    # Step 3: Loop through arr2 to find a potential starting point for arr1
    for i in range(length2 - length1 + 1):
        # Assume arr1 might be a subarray starting from this position
        is_match = True

        # Step 4: Compare each element of arr1 with the corresponding element in arr2
        for j in range(length1):
            if arr2[i + j] != arr1[j]:
                # If any element doesn't match, arr1 is not a subarray at this position
                is_match = False
                break

        # Step 5: If we found a complete match, return True
        if is_match:
            return True

    # Step 6: If no match was found after checking all positions, return False
    return False


arr1 = ["ccc", "ddd"]
arr2 = ["aaa", "bbb", "ccc", "ddd", "eee"]
arr3 = ["aaa", "bbb", "ccc"]

print(is_subarray(arr1, arr2))
print(is_subarray(arr1, arr3))

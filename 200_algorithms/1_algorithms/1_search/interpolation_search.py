# ----------------------------------
# ----------------------------------
# INTERPOLATION SEARCH
#
# Time complexity: O(log log n)
#
# SORTED Array/List !!!!
#
# https://www.geeksforgeeks.org/interpolation-search/
# ----------------------------------
# ----------------------------------

# --------------------------------------------
# RECURSIVE VERSION
# --------------------------------------------

def interpolation_search(array_to_search, value_to_search, low, high):
    if (
        low <= high and
        value_to_search >= array_to_search[low] and
        value_to_search <= array_to_search[high]
    ):
        # Handle division by zero
        if array_to_search[high] == array_to_search[low]:
            if array_to_search[low] == value_to_search:
                return low
            return -1

        # Calculate position using interpolation formula
        delta = (value_to_search - array_to_search[low]) / (array_to_search[high] - array_to_search[low])
        position = low + int((high - low) * delta)

        # Check if the value is at the estimated position
        if array_to_search[position] == value_to_search:
            return position

        # Recur for the appropriate section of the array
        if array_to_search[position] < value_to_search:
            return interpolation_search(array_to_search, value_to_search, position + 1, high)
        else:
            return interpolation_search(array_to_search, value_to_search, low, position - 1)

    return -1

# ----------------------------------
# ----------------------------------
# TEST CODE
search_value = 22
arr = [2, 5, 6, 7, 9, 14, 22, 34, 46, 50]
length = len(arr)
low = 0
high = length - 1

position = interpolation_search(arr, search_value, low, high)
if position != -1:
    print("Found at position:", position)
else:
    print("Value not found")

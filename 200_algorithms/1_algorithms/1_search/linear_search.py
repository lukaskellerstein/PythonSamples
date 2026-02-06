# ----------------------------------
# ----------------------------------
# LINEAR SEARCH
#
# Time complexity: O(n)
#
# Unsorted Array/List
#
# https://www.geeksforgeeks.org/linear-search/
# ----------------------------------
# ----------------------------------

search_value = 22
arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

# FOR loop
for i in range(len(arr)):
    if arr[i] == search_value:
        print("Value found")
        break  # Optional: Stops the loop after finding the value

# FOR EACH equivalent (using a for loop)
for item in arr:
    if item == search_value:
        print("Value found")
        break  # Optional: Stops the loop after finding the value


# -----------------------
# Subsets (LeetCode 78)
# -----------------------

# Difficulty: Medium (but the simplest backtracking template — start here)

# Problem: Given an integer array nums of unique elements, return all possible
# subsets (the power set). The solution set must not contain duplicate subsets.
# Return the solution in any order.

# -----------------------

# For given array [1,2,3], return all subsets.
nums = [1, 2, 3]

# ----------------------------------------------------
# Backtracking solution
#
# time complexity = O(n * 2^n) - 2^n subsets, each takes O(n) to copy
# space complexity = O(n) - recursion depth + path (excluding output)
# ----------------------------------------------------


def subsets(nums):
    res = []
    path = []

    def backtrack(start):
        # Every node in the recursion tree is a valid subset — add it
        res.append(path[:])

        for i in range(start, len(nums)):
            # Choose
            path.append(nums[i])
            # Explore — move to next index to avoid duplicates
            backtrack(i + 1)
            # Undo (backtrack)
            path.pop()

    backtrack(0)
    return res


# Example
print(subsets(nums))  # [[], [1], [1,2], [1,2,3], [1,3], [2], [2,3], [3]]


# ----------------------------------------------------
# Brute Force solution (iterative / cascading)
#
# time complexity = O(n * 2^n) - same total work
# space complexity = O(n * 2^n) - all subsets stored
# ----------------------------------------------------


def subsets_brute_force(nums):
    # Start with empty subset, for each num extend every existing subset
    result = [[]]

    for num in nums:
        result += [subset + [num] for subset in result]

    return result


# Example
print(subsets_brute_force(nums))  # [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]

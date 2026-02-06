
# -----------------------
# Permutations (LeetCode 46)
# -----------------------

# Difficulty: Medium

# Problem: Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order.

# -----------------------

# For given array [1,2,3], return all permutations.
nums = [1, 2, 3]

# ----------------------------------------------------
# Backtracking solution (with used set)
#
# time complexity = O(n * n!) - n! permutations, each takes O(n) to copy
# space complexity = O(n) - recursion depth + used set
# ----------------------------------------------------


def permute(nums):
    res = []
    path = []
    used = set()

    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if i in used:
                continue
            # Choose
            path.append(nums[i])
            used.add(i)
            # Explore
            backtrack()
            # Undo (backtrack)
            path.pop()
            used.remove(i)

    backtrack()
    return res


# Example
print(permute(nums))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# ----------------------------------------------------
# Brute Force solution (shrinking remaining list)
#
# time complexity = O(n * n!) - same
# space complexity = O(n^2) - slicing creates new lists at each level
# ----------------------------------------------------


def permute_brute_force(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            res.append(path[:])
            return
        for i in range(len(remaining)):
            # Pick element i, pass the rest as a new list
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i + 1 :])

    backtrack([], nums)
    return res


# Example
print(permute_brute_force(nums))  # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


# -----------------------
# Combination Sum (LeetCode 39)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of distinct integers candidates and a target integer
# target, return a list of all unique combinations of candidates where the chosen
# numbers sum to target. The same number may be chosen unlimited number of times.

# -----------------------

# For given candidates [2,3,6,7] and target 7, find all combinations summing to 7.
candidates = [2, 3, 6, 7]
target = 7

# ----------------------------------------------------
# Backtracking solution (with pruning)
#
# time complexity = O(n^(t/m)) - n = candidates, t = target, m = min candidate
# space complexity = O(t/m) - max recursion depth
# ----------------------------------------------------


def combination_sum(candidates, target):
    res = []
    path = []

    # Sort to enable early termination pruning
    candidates.sort()

    def backtrack(start, remain):
        if remain == 0:
            res.append(path[:])
            return

        for i in range(start, len(candidates)):
            # Pruning: if current candidate exceeds remaining, skip the rest
            if candidates[i] > remain:
                break

            # Choose
            path.append(candidates[i])
            # Explore — pass i (not i+1) because we can reuse the same element
            backtrack(i, remain - candidates[i])
            # Undo (backtrack)
            path.pop()

    backtrack(0, target)
    return res


# Example
print(combination_sum(candidates, target))  # [[2,2,3], [7]]


# ----------------------------------------------------
# Brute Force solution (no pruning)
#
# time complexity = O(n^(t/m)) - explores all branches without early termination
# space complexity = O(t/m) - max recursion depth
# ----------------------------------------------------


def combination_sum_brute_force(candidates, target):
    res = []

    def backtrack(start, path, remain):
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0:
            return

        for i in range(start, len(candidates)):
            backtrack(i, path + [candidates[i]], remain - candidates[i])

    backtrack(0, [], target)
    return res


# Example
print(combination_sum_brute_force(candidates, target))  # [[2,2,3], [7]]

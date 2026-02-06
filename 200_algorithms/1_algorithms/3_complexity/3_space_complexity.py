# ============================================================
# SPACE COMPLEXITY - COMPLETE GUIDE
# ============================================================
# Space complexity = how much EXTRA memory your algorithm uses
# (not counting the input itself)
#
# Two things consume memory:
#   1. Data structures you create (arrays, dicts, sets, etc.)
#   2. Call stack frames from recursion
# ============================================================


# ============================================================
# O(1) SPACE - CONSTANT
# Pattern: Only use a fixed number of variables.
#          No arrays, no hash maps, no recursion.
# ============================================================

def find_max(arr):
    """O(1) space - just one variable 'best'"""
    best = arr[0]                # 1 variable
    for x in arr:
        best = max(best, x)
    return best

def reverse_in_place(arr):
    """O(1) space - swap with two pointers, no new array"""
    lo, hi = 0, len(arr) - 1    # 2 variables
    while lo < hi:
        arr[lo], arr[hi] = arr[hi], arr[lo]
        lo += 1
        hi -= 1

def dutch_national_flag(arr):
    """O(1) space - sort 0s, 1s, 2s in one pass"""
    lo, mid, hi = 0, 0, len(arr) - 1  # 3 variables
    while mid <= hi:
        if arr[mid] == 0:
            arr[lo], arr[mid] = arr[mid], arr[lo]
            lo += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[hi] = arr[hi], arr[mid]
            hi -= 1


# ============================================================
# O(log n) SPACE
# Pattern: Recursion that halves the problem each time.
#          Call stack depth = log n.
# ============================================================

def binary_search_recursive(arr, target, lo=0, hi=None):
    """O(log n) space from recursive call stack"""
    if hi is None:
        hi = len(arr) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, hi)  # stack frame
    else:
        return binary_search_recursive(arr, target, lo, mid - 1)  # stack frame
    # Max depth = log n -> O(log n) space

def binary_search_iterative(arr, target):
    """O(1) space - same algorithm, no recursion!"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
    # KEY: Converting recursion to iteration often saves O(log n) or O(n) space!


# ============================================================
# O(n) SPACE - LINEAR
# Pattern: Create a new array/dict/set of size proportional to n.
#          OR: recursion with depth n.
# ============================================================

# --- Extra data structure ---

def count_frequencies(arr):
    """O(n) space - hash map can have up to n entries"""
    freq = {}                       # <-- this grows to O(n)
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

def remove_duplicates(arr):
    """O(n) space - set stores up to n unique values"""
    seen = set()                    # <-- O(n) space
    result = []                     # <-- O(n) space
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def prefix_sum(arr):
    """O(n) space - new array of same size"""
    n = len(arr)
    sums = [0] * n                  # <-- O(n) space
    sums[0] = arr[0]
    for i in range(1, n):
        sums[i] = sums[i - 1] + arr[i]
    return sums

# --- Recursion stack ---

def factorial(n):
    """O(n) space - recursion depth = n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)
    # Each call adds a frame to the stack:
    #   factorial(5) -> factorial(4) -> factorial(3) -> ... -> factorial(1)
    #   That's n frames = O(n) space

def factorial_iterative(n):
    """O(1) space - same result, no recursion"""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# ============================================================
# O(n) SPACE FROM RECURSION - THE TRICKY PART
# ============================================================

def fibonacci_naive(n):
    """
    Time:  O(2^n) - exponential!
    Space: O(n)   - only n! NOT 2^n!

    WHY? The call tree looks like:
                    f(5)
                  /      \\
               f(4)      f(3)
              /    \\    /    \\
           f(3)  f(2) f(2)  f(1)
          /   \\
        f(2) f(1)

    The tree has 2^n nodes BUT they're not all alive at once.
    Python executes depth-first: it goes all the way down the LEFT
    branch first, then comes back up and goes right.

    Maximum depth = n -> maximum stack frames at once = n -> O(n) space.
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# ============================================================
# O(n^2) SPACE - QUADRATIC
# Pattern: 2D matrix or storing all pairs.
# ============================================================

def create_adjacency_matrix(n, edges):
    """O(n^2) space - n x n matrix"""
    matrix = [[0] * n for _ in range(n)]   # <-- n*n cells
    for u, v in edges:
        matrix[u][v] = 1
        matrix[v][u] = 1
    return matrix

def dp_longest_common_subsequence(s1, s2):
    """O(n*m) space - 2D DP table"""
    n, m = len(s1), len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # <-- (n+1)*(m+1) cells
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][m]

def dp_lcs_optimized(s1, s2):
    """O(min(n,m)) space - only keep 2 rows of DP table!"""
    n, m = len(s1), len(s2)
    if n < m:
        s1, s2 = s2, s1
        n, m = m, n
    prev = [0] * (m + 1)           # <-- only 2 rows = O(m) space
    curr = [0] * (m + 1)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (m + 1)
    return prev[m]
    # KEY TECHNIQUE: If DP only looks at previous row, keep 2 rows instead of n.


# ============================================================
# SPACE OPTIMIZATION TECHNIQUES (CHEAT SHEET)
# ============================================================
#
# 1. CONVERT RECURSION TO ITERATION
#    Recursive binary search: O(log n) space
#    Iterative binary search: O(1) space
#
# 2. MODIFY INPUT IN-PLACE (if allowed)
#    New reversed array: O(n) space
#    Reverse in-place:   O(1) space
#
# 3. USE BIT MANIPULATION
#    Visited set:        O(n) space
#    Bitmask:            O(1) space (for n <= 32 or 64)
#
# 4. ROLLING ARRAY FOR DP
#    Full 2D DP table:   O(n*m) space
#    Two rows only:      O(m) space
#
# 5. TWO POINTERS INSTEAD OF HASH SET
#    Hash set approach:  O(n) space
#    Sort + two pointers: O(1) extra space (if sorting in-place)
#
# ============================================================
#
# SUMMARY TABLE
# ============================================================
#
#  Pattern                                    Space
#  -------                                    -----
#  Fixed number of variables                  O(1)
#  Recursion halving problem                  O(log n)
#  One array/dict/set of size n               O(n)
#  Recursion with depth n                     O(n)
#  2D matrix n x n                            O(n^2)
#  Storing all subsets of n items             O(2^n)
#  Storing all permutations of n items        O(n * n!)
#
# ============================================================

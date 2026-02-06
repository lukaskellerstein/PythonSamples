# ============================================================
# RECOGNIZE COMPLEXITY BY CODE PATTERN
# ============================================================
# The fastest way to determine complexity:
# Look at the SHAPE of the code, not the details.
# ============================================================


# ============================================================
# O(1) - CONSTANT
# Pattern: No loops, no recursion. Direct access or math.
# "If I double the input, runtime stays the same."
# ============================================================

def get_first(arr):
    """Array access by index = O(1)"""
    return arr[0]

def get_from_dict(d, key):
    """Hash map lookup = O(1) average"""
    return d[key]

def is_even(n):
    """Simple math = O(1)"""
    return n % 2 == 0

def swap(arr, i, j):
    """Swap two elements = O(1)"""
    arr[i], arr[j] = arr[j], arr[i]

def push_pop_stack(stack, val):
    """Stack push/pop = O(1)"""
    stack.append(val)
    stack.pop()


# ============================================================
# O(log n) - LOGARITHMIC
# Pattern: Cut problem in HALF each step.
# "If I double the input, I need just ONE more step."
# ============================================================

def binary_search(arr, target):
    """Classic halving pattern -> O(log n)"""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2       # Look at middle
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1            # Throw away left half
        else:
            hi = mid - 1            # Throw away right half
    return -1

def count_digits(n):
    """Dividing by constant each step -> O(log n)"""
    count = 0
    while n > 0:
        n //= 10                    # Problem shrinks by factor of 10
        count += 1
    return count

def power_fast(base, exp):
    """Exponentiation by squaring -> O(log n)"""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result *= base
        base *= base
        exp //= 2                   # Halving exponent each step
    return result


# ============================================================
# O(n) - LINEAR
# Pattern: Single loop from 0 to n. Touch each element once.
# "If I double the input, runtime doubles."
# ============================================================

def find_max(arr):
    """One pass through array -> O(n)"""
    max_val = arr[0]
    for x in arr:                   # n iterations
        if x > max_val:
            max_val = x
    return max_val

def linear_search(arr, target):
    """Check every element -> O(n)"""
    for i, x in enumerate(arr):     # Up to n iterations
        if x == target:
            return i
    return -1

def sum_list(arr):
    """Touch each element once -> O(n)"""
    total = 0
    for x in arr:                   # n iterations
        total += x
    return total

def two_sum_hashmap(arr, target):
    """Hash map approach -> O(n) time, O(n) space"""
    seen = {}
    for i, x in enumerate(arr):     # n iterations, O(1) per lookup
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []


# ============================================================
# O(n log n) - LINEARITHMIC
# Pattern: Divide into halves (log n levels), do O(n) work per level.
#          OR: Sort the array first, then do O(n) work.
# "Slightly more than doubled when input doubles."
# ============================================================

def merge_sort(arr):
    """Split in half + merge = O(n log n)"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])        # Split: log n levels
    right = merge_sort(arr[mid:])       # Split: log n levels
    return merge(left, right)           # Merge: O(n) per level

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def has_duplicates_sort(arr):
    """Sort first (n log n) + one pass (n) = O(n log n)"""
    arr.sort()                          # O(n log n) dominates
    for i in range(len(arr) - 1):       # O(n)
        if arr[i] == arr[i + 1]:
            return True
    return False


# ============================================================
# O(n^2) - QUADRATIC
# Pattern: Nested loops, BOTH go up to n.
# "If I double the input, runtime quadruples (4x)."
# ============================================================

def bubble_sort(arr):
    """Two nested loops over n -> O(n^2)"""
    n = len(arr)
    for i in range(n):                  # n times
        for j in range(n - 1 - i):     # ~n times
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def two_sum_brute(arr, target):
    """Check all pairs -> O(n^2)"""
    n = len(arr)
    for i in range(n):                  # n times
        for j in range(i + 1, n):       # ~n times
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

def print_all_pairs(arr):
    """All pairs = n * n -> O(n^2)"""
    for i in arr:                       # n times
        for j in arr:                   # n times
            print(i, j)


# ============================================================
# O(m * n) - TWO INDEPENDENT INPUTS
# Pattern: Nested loops where each loop iterates over a
#          DIFFERENT input (not the same one twice).
#
# KEY INSIGHT:
#   O(n^2) = nested loops over the SAME input (n * n)
#   O(m*n) = nested loops over TWO DIFFERENT inputs (m * n)
#   O(n^2) is just O(m*n) where m happens to equal n!
#
# When do you use m*n instead of n^2?
#   -> When the two dimensions can be DIFFERENT sizes.
#      A 1000x3 grid is very different from a 1000x1000 grid.
#      Calling both "n^2" would hide that difference.
# ============================================================

def traverse_grid(grid):
    """
    Grid with m rows and n columns -> O(m * n)

    m = number of rows (could be 5)
    n = number of columns (could be 1000)
    These are INDEPENDENT - one doesn't determine the other.
    """
    m = len(grid)           # rows
    n = len(grid[0])        # columns
    for i in range(m):              # m iterations
        for j in range(n):          # n iterations
            print(grid[i][j])
    # Total: m * n operations

def search_in_grid(grid, target):
    """
    Visit every cell in m x n grid -> O(m * n) time, O(1) space
    """
    for i in range(len(grid)):          # m rows
        for j in range(len(grid[0])):   # n cols
            if grid[i][j] == target:
                return (i, j)
    return None

def longest_common_subsequence(text1, text2):
    """
    Compare two strings of DIFFERENT lengths -> O(m * n)

    text1 has length m, text2 has length n.
    We build an m x n DP table -> O(m * n) time AND space.

    WHY NOT O(n^2)?
    Because m and n are independent. If text1 = "hi" (m=2)
    and text2 = "abcdefghij" (n=10), it's 2*10 = 20 operations,
    NOT 10^2 = 100 or 2^2 = 4.
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # O(m*n) space

    for i in range(1, m + 1):           # m iterations
        for j in range(1, n + 1):       # n iterations
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

def flood_fill(grid, r, c, new_color):
    """
    Visit every cell at most once -> O(m * n) time, O(m * n) space

    Space is O(m*n) because recursion can go through ALL cells
    in worst case (call stack depth = m*n).
    """
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return
    old_color = grid[r][c]
    if old_color == new_color:
        return
    grid[r][c] = new_color
    flood_fill(grid, r+1, c, new_color)  # down
    flood_fill(grid, r-1, c, new_color)  # up
    flood_fill(grid, r, c+1, new_color)  # right
    flood_fill(grid, r, c-1, new_color)  # left

def multiply_matrices(A, B):
    """
    A is (m x p), B is (p x n) -> result is (m x n)
    Time: O(m * n * p) -- three different dimensions!
    """
    m = len(A)
    p = len(A[0])
    n = len(B[0])
    C = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C

# ============================================================
# WHEN TO USE WHICH NOTATION:
#
#   Situation                          Write as
#   ----------------------------------  --------
#   Nested loop, same array            O(n^2)
#   Grid traversal (rows x cols)       O(m * n)
#   Compare two strings                O(m * n)
#   DP on two sequences                O(m * n)
#   Graph traversal (vertices, edges)  O(V + E)
#   Matrix multiply (m x p) * (p x n) O(m * n * p)
#
# RULE OF THUMB:
#   If the two loop bounds come from DIFFERENT inputs -> use m * n
#   If both come from the SAME input                  -> use n^2
# ============================================================


# ============================================================
# O(n^3) - CUBIC
# Pattern: Triple nested loops, ALL go up to n.
# ============================================================

def matrix_multiply_naive(A, B):
    """Triple nested loop -> O(n^3)"""
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):                  # n
        for j in range(n):              # n
            for k in range(n):          # n
                C[i][j] += A[i][k] * B[k][j]
    return C

def three_sum_brute(arr, target):
    """Check all triples -> O(n^3)"""
    n = len(arr)
    results = []
    for i in range(n):                  # n
        for j in range(i + 1, n):       # n
            for k in range(j + 1, n):   # n
                if arr[i] + arr[j] + arr[k] == target:
                    results.append([arr[i], arr[j], arr[k]])
    return results


# ============================================================
# O(2^n) - EXPONENTIAL
# Pattern: Recursion that branches into 2 calls, depth n.
# Formula: O(branches ^ depth)
# ============================================================

def fibonacci_naive(n):
    """2 branches, depth n -> O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)  # 2 branches!

def all_subsets(arr):
    """Each element: include or exclude (2 choices) -> O(2^n)"""
    result = []
    def backtrack(index, current):
        if index == len(arr):
            result.append(current[:])
            return
        # Choice 1: include arr[index]
        current.append(arr[index])
        backtrack(index + 1, current)
        current.pop()
        # Choice 2: exclude arr[index]
        backtrack(index + 1, current)
    backtrack(0, [])
    return result


# ============================================================
# O(n!) - FACTORIAL
# Pattern: Generate all permutations / orderings.
# ============================================================

def all_permutations(arr):
    """n choices, then n-1, then n-2... = n! -> O(n!)"""
    result = []
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):    # Shrinking choices
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]
    backtrack(0)
    return result


# ============================================================
# SUMMARY: Pattern -> Complexity Lookup
# ============================================================
#
# Direct access / math / hash lookup         -> O(1)
# Halving the problem each step               -> O(log n)
# Single loop over n                          -> O(n)
# Sort + one pass                             -> O(n log n)
# Divide & conquer (split + merge)            -> O(n log n)
# Nested loops, SAME input                    -> O(n^2)
# Nested loops, TWO DIFFERENT inputs          -> O(m * n)
# Three nested loops over n                   -> O(n^3)
# Recursion: 2 branches, depth n              -> O(2^n)
# All permutations                            -> O(n!)
# ============================================================

# ============================================================
# ANSWER KEY - Exercises 1-15
# ============================================================
# DO NOT READ THIS BEFORE COMPLETING THE EXERCISES!
# This file is for Claude to evaluate your answers against.
# ============================================================


# --- EX 01 ---
# TIME = "O(n)"       single loop over n elements
# SPACE = "O(1)"      only one variable 'total'

# --- EX 02 ---
# TIME = "O(n^2)"     two nested loops, both go up to n
# SPACE = "O(1)"      no extra data structures

# --- EX 03 ---
# TIME = "O(n)"       single loop, set lookup is O(1)
# SPACE = "O(n)"      set can grow to n elements
#
# BONUS: Ex 2 vs Ex 3 = classic TIME vs SPACE trade-off
#   Ex 2: O(n^2) time, O(1) space  (brute force)
#   Ex 3: O(n) time, O(n) space    (hash set)

# --- EX 04 ---
# TIME = "O(n)"       n recursive calls, each does O(1) work
# SPACE = "O(n)"      n frames on the call stack

# --- EX 05 ---
# TIME = "O(n log^2 n)"   log n levels, but sorted() is O(n log n) per level
#                          not O(n) like a proper merge. Total: O(n log n * log n)
# SPACE = "O(n log n)"    new arrays at each level
#
# ALSO ACCEPT: "O(n (log n)^2)" for time

# --- EX 06 ---
# TIME = "O(log n)"   i doubles each step: 1,2,4,8...n => log n steps
# SPACE = "O(1)"      just one variable

# --- EX 07 ---
# TIME = "O(n log n)" outer loop O(n), inner loop j*=2 is O(log n)
# SPACE = "O(1)"      just loop variables

# --- EX 08 ---
# TIME = "O(n log n)" sort is O(n log n), two-pointer is O(n). Sort dominates.
# SPACE = "O(1)"      in-place sort + two pointers
#
# ALSO ACCEPT: "O(n)" for space (Python's Timsort uses O(n) auxiliary space)

# --- EX 09 ---
# TIME = "O(n^2)"     two nested loops, each goes to n (square grid)
# SPACE = "O(1)"      just the total variable
#
# ALSO ACCEPT: "O(m*n)" if student notes grid could be m x n

# --- EX 10 ---
# TIME = "O(n * n!)"  n! permutations, each takes O(n) to build
# SPACE = "O(n * n!)"  storing n! permutations of length n, plus O(n) stack

# --- EX 11 ---
# TIME = "O(n)"       loop runs n/2 times. O(n/2) = O(n). Drop the constant.
# SPACE = "O(1)"      modifying in place

# --- EX 12 ---
# TIME = "O(nm * log(nm))"  flatten is O(nm), sort is O(nm * log(nm)). Sort dominates.
# SPACE = "O(nm)"           flat list holds all n*m elements
#
# ALSO ACCEPT: "O(k log k)" where k = n*m

# --- EX 13 ---
# TIME = "O(2^n)"     2 branches at each level, depth n
#                      Total nodes: 2^0 + 2^1 + ... + 2^n = O(2^n)
# SPACE = "O(n)"      max recursion depth = n (only one branch active at a time!)
#
# KEY INSIGHT: Time is exponential but space is only the MAX DEPTH

# --- EX 14 ---
# TIME = "O(n^2)"     inner loop runs 1 + 2 + 3 + ... + n = n(n+1)/2 = O(n^2)
# SPACE = "O(n^2)"    storing n^2/2 elements total in result

# --- EX 15 ---
# TIME = "O(n)"       with memoization, each value 0..n computed only once
# SPACE = "O(n)"      memo dict stores n values + O(n) call stack

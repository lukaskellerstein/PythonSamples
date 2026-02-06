# ============================================================
# ANSWER KEY - Speedrun Q1-Q30
# ============================================================
# DO NOT READ THIS BEFORE COMPLETING THE SPEEDRUN!
# This file is for Claude to evaluate your answers against.
# ============================================================
#
# Format: Q#: Time | Space -- explanation
#
# Q1:  O(1)        | O(1)        -- direct index access
# Q2:  O(n)        | O(1)        -- single loop
# Q3:  O(n^2)      | O(1)        -- nested loops
# Q4:  O(log n)    | O(1)        -- halving
# Q5:  O(n log n)  | O(1)        -- sort dominates  (also accept O(n) space for Timsort)
# Q6:  O(n)        | O(n)        -- linear recursion, n stack frames
# Q7:  O(2^n)      | O(n)        -- 2 branches, depth n
# Q8:  O(n)        | O(n)        -- iterate all + store in set
# Q9:  O(n log n)  | O(1)        -- outer O(n), inner j*=2 is O(log n)
# Q10: O(n)        | O(n)        -- s[::-1] creates a copy of the string
# Q11: O(n)        | O(n)        -- one pass + set of size n
# Q12: O(n^2)      | O(1)        -- 0+1+2+...+(n-1) = n^2/2 = O(n^2)
# Q13: O(n^2)      | O(n)        -- string concat trap! each += copies entire string
# Q14: O(n)        | O(n)        -- memoized: each subproblem computed once
# Q15: O(m*n)      | O(1)        -- iterate all cells (m rows, n cols per row)
#                                   also accept O(n) if n = total elements
# Q16: O(log n)    | O(1)        -- binary search, iterative
# Q17: O(n)        | O(n)        -- each element pushed AND popped at most once (amortized)
# Q18: O(n^2)      | O(n^2)      -- create n*n matrix
# Q19: O(k)        | O(k)        -- loop runs k times, appends k elements
# Q20: O(n)        | O(n)        -- Counter iterates all, stores freq dict
# Q21: O(n^3)      | O(1)        -- triple nested loops
# Q22: O(n log n)  | O(n)        -- merge sort
# Q23: O(n * n!)   | O(n * n!)   -- generate all permutations
# Q24: O(n)        | O(n)        -- single pass, prefix array of size n+1
# Q25: O(n)        | O(1)        -- fast/slow pointer, one pass, no extra structures
# Q26: O(m*n)      | O(m*n)      -- visit each cell once, recursion stack up to m*n
# Q27: O(n)        | O(n)        -- iterative DP, array of size n+1
# Q28: O(n log n)  | O(1)        -- sort dominates, two pointers is O(n)
#                                   also accept O(n) space for Timsort
# Q29: O(n)        | O(n)        -- two sequential passes, output array of size n
# Q30: O(n * n!)   | O(n * n!)   -- generate all n! permutations
#
# ============================================================
# SCORING
# ============================================================
# Each question is worth 1 point (both time AND space must be correct).
# Partial credit: 0.5 if only one of time/space is correct.
#
#   28-30: Expert level
#   24-27: Strong
#   18-23: Good foundation, review tricky ones
#   Below 18: Re-study the patterns
# ============================================================

# ============================================================
# EXERCISE 15 - Fibonacci with memoization
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: Compare this to a naive fibonacci (no memo).
#       How many unique subproblems are there?

def exercise_15(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = exercise_15(n - 1, memo) + exercise_15(n - 2, memo)
    return memo[n]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

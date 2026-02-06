# ============================================================
# EXERCISE 4 - Recursive sum
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: Think about what happens on the call stack.

def exercise_4(n):
    if n <= 0:
        return 0
    return n + exercise_4(n - 1)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

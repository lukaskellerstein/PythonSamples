# ============================================================
# EXERCISE 13 - Double recursive call
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: Draw the recursion tree. How many nodes does it have?
#       How deep does it go? Time and space are DIFFERENT here.

def exercise_13(n):
    if n <= 1:
        return 1
    return exercise_13(n - 1) + exercise_13(n - 1)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

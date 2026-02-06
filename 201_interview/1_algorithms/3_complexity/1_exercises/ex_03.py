# ============================================================
# EXERCISE 3 - Find duplicate (hash set)
# ============================================================
# What is the time and space complexity of this function?
#
# BONUS: Compare this to exercise 2. Both solve the same problem.
# What is the trade-off?

def exercise_3(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

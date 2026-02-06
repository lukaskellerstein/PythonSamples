# ============================================================
# EXERCISE 11 - Step-by-2 loop
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: Does the step size change the Big-O?

def exercise_11(arr):
    n = len(arr)
    for i in range(0, n, 2):  # step by 2
        arr[i] = arr[i] * 2
    return arr

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

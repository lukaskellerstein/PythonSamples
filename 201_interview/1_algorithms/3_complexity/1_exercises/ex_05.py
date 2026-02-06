# ============================================================
# EXERCISE 5 - Broken merge sort
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: This looks like merge sort, but the merge step
#       is implemented differently. Look carefully at how
#       left and right are combined.

def exercise_5(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = exercise_5(arr[:mid])
    right = exercise_5(arr[mid:])
    return sorted(left + right)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

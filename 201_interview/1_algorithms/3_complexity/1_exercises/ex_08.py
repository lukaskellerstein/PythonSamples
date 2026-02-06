# ============================================================
# EXERCISE 8 - Sort + two pointers
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: Multiple steps. Which one dominates?

def exercise_8(arr, target):
    arr.sort()
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        s = arr[lo] + arr[hi]
        if s == target:
            return [lo, hi]
        elif s < target:
            lo += 1
        else:
            hi -= 1
    return []

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

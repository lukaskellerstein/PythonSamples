# ============================================================
# EXERCISE 14 - Triangular nested loop
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: The inner loop does NOT always run n times.
#       Count the total work: how many times does the inner
#       loop body execute across ALL iterations?

def exercise_14(arr):
    n = len(arr)
    result = []
    for i in range(n):
        row = []
        for j in range(i + 1):   # NOTE: j goes to i, not n!
            row.append(arr[j])
        result.append(row)
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

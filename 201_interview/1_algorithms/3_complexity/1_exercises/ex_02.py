# ============================================================
# EXERCISE 2 - Find duplicate (brute force)
# ============================================================
# What is the time and space complexity of this function?

def exercise_2(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j] and i != j:
                return True
    return False

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

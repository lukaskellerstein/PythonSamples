# ============================================================
# EXERCISE 10 - Generate all permutations
# ============================================================
# What is the time and space complexity of this function?

def exercise_10(s):
    """s is a string of length n"""
    result = []
    def backtrack(current, remaining):
        if not remaining:
            result.append(current)
            return
        for i in range(len(remaining)):
            backtrack(current + remaining[i],
                      remaining[:i] + remaining[i+1:])
    backtrack("", s)
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

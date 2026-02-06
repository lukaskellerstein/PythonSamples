# ============================================================
# EXERCISE 12 - Flatten and sort a matrix
# ============================================================
# What is the time and space complexity of this function?
#
# HINT: The matrix has n rows and m columns (not necessarily square).
#       Think about the total number of elements.

def exercise_12(matrix):
    """matrix is n x m"""
    n = len(matrix)
    m = len(matrix[0])
    flat = []
    for i in range(n):
        for j in range(m):
            flat.append(matrix[i][j])
    flat.sort()
    return flat

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

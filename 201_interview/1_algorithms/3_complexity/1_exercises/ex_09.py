# ============================================================
# EXERCISE 9 - Sum a square grid
# ============================================================
# What is the time and space complexity of this function?

def exercise_9(grid):
    """grid is n x n"""
    n = len(grid)
    total = 0
    for i in range(n):
        for j in range(n):
            total += grid[i][j]
    return total

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
EXPLANATION = """???"""
# ===== END ANSWER =====

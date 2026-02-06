# ============================================================
# SPEEDRUN - 30 Questions, Target: Under 5 Minutes
# ============================================================
# Fill in TIME and SPACE for each question.
# Use Big-O notation: "O(1)", "O(n)", "O(n^2)", "O(n log n)", etc.
# Do NOT look at _answers/ until you're done!
#
# START YOUR TIMER NOW!
# ============================================================


# --- Q1 ---
def q1(arr):
    return arr[0] + arr[-1]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q2 ---
def q2(arr):
    for x in arr:
        print(x)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q3 ---
def q3(arr):
    for x in arr:
        for y in arr:
            print(x, y)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q4 ---
def q4(n):
    while n > 1:
        n //= 2

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q5 ---
def q5(arr):
    arr.sort()
    return arr[0]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q6 ---
def q6(n):
    if n <= 0: return
    q6(n - 1)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q7 ---
def q7(n):
    if n <= 0: return
    q7(n - 1)
    q7(n - 1)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q8 ---
def q8(arr):
    return set(arr)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q9 ---
def q9(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q10 ---
def q10(s):
    return s[::-1] == s

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q11 ---
def q11(arr):
    seen = set()
    for x in arr:
        seen.add(x)
    return len(seen) == len(arr)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q12 ---
def q12(n):
    for i in range(n):
        for j in range(i):
            pass

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q13 ---
def q13(arr):
    result = ""
    for s in arr:
        result += s
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q14 ---
def q14(n, memo={}):
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = q14(n-1, memo) + q14(n-2, memo)
    return memo[n]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q15 ---
def q15(matrix):
    for row in matrix:
        for val in row:
            print(val)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q16 ---
def q16(arr):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == 0:
            return mid
        elif arr[mid] < 0:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q17 ---
def q17(arr):
    stack = []
    for x in arr:
        while stack and stack[-1] < x:
            stack.pop()
        stack.append(x)
    return stack

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q18 ---
def q18(n):
    return [[0]*n for _ in range(n)]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q19 ---
def q19(arr, k):
    for i in range(k):
        arr.append(arr[i])
    return arr

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q20 ---
def q20(arr):
    from collections import Counter
    return Counter(arr).most_common(1)[0]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q21 ---
def q21(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q22 ---
def q22(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left = q22(arr[:mid])
    right = q22(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    return result + left[i:] + right[j:]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q23 ---
def q23(s):
    result = []
    def bt(curr, rem):
        if not rem:
            result.append(curr)
            return
        for i in range(len(rem)):
            bt(curr + rem[i], rem[:i] + rem[i+1:])
    bt("", s)
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q24 ---
def q24(arr):
    n = len(arr)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q25 ---
def q25(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q26 ---
def q26(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return
    if grid[i][j] == 0:
        return
    grid[i][j] = 0
    q26(grid, i+1, j)
    q26(grid, i-1, j)
    q26(grid, i, j+1)
    q26(grid, i, j-1)

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q27 ---
def q27(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q28 ---
def q28(arr):
    arr.sort()
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        if arr[lo] + arr[hi] == 0:
            return True
        elif arr[lo] + arr[hi] < 0:
            lo += 1
        else:
            hi -= 1
    return False

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q29 ---
def q29(arr):
    n = len(arr)
    result = [1] * n
    left = 1
    for i in range(n):
        result[i] = left
        left *= arr[i]
    right = 1
    for i in range(n - 1, -1, -1):
        result[i] *= right
        right *= arr[i]
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# --- Q30 ---
def q30(n):
    if n <= 1: return [[]]
    smaller = q30(n - 1)
    result = []
    for perm in smaller:
        for i in range(len(perm) + 1):
            result.append(perm[:i] + [n] + perm[i:])
    return result

# ===== YOUR ANSWER =====
TIME = "???"
SPACE = "???"
# ===== END ANSWER =====


# ============================================================
# STOP YOUR TIMER!
# Time taken: _____ minutes
#
# Now ask Claude to evaluate your answers.
# ============================================================

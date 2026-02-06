# ============================================================
# TRICKY CASES - Gotchas That Trip People Up
# ============================================================
# These are the cases where the obvious answer is WRONG.
# Memorize these patterns to avoid mistakes in interviews.
# ============================================================


# ============================================================
# TRICK 1: Hidden Loop Inside a Loop
# "It looks like O(n) but it's actually O(n^2)"
# ============================================================

def trick_1_string_concat(arr):
    """
    LOOKS LIKE O(n) -- single loop, right?
    ACTUALLY O(n^2) -- because string concatenation creates a NEW string!

    Each += copies the entire string so far:
      iteration 1: copy 1 char
      iteration 2: copy 2 chars
      iteration 3: copy 3 chars
      ...
      iteration n: copy n chars
      Total: 1 + 2 + 3 + ... + n = O(n^2)
    """
    result = ""
    for s in arr:
        result += s        # <-- Creates a new string each time!
    return result

def trick_1_fixed(arr):
    """O(n) - join is implemented efficiently"""
    return "".join(arr)


# ============================================================
# TRICK 2: Loop That Doesn't Run n Times
# "It has a nested loop but it's NOT O(n^2)"
# ============================================================

def trick_2_two_pointer(arr):
    """
    LOOKS LIKE O(n^2) -- there's a while inside a for?
    ACTUALLY O(n) -- 'j' only moves forward, never resets!

    'j' advances from 0 to n across ALL iterations of the outer loop.
    Total work: j moves n times total, not n times PER outer iteration.
    """
    n = len(arr)
    j = 0
    for i in range(n):
        while j < n and arr[j] < arr[i]:
            j += 1         # j only moves forward, total n steps

def trick_2_amortized(stack_ops, n):
    """
    LOOKS LIKE O(n^2) -- while loop pops inside a for loop?
    ACTUALLY O(n) -- each element is pushed AND popped at most once.

    Total pushes: n
    Total pops: at most n
    Total work: O(2n) = O(n)
    This is "amortized O(1) per operation".
    """
    stack = []
    for i in range(n):
        while stack and stack[-1] > i:
            stack.pop()    # Each element popped at most once total
        stack.append(i)


# ============================================================
# TRICK 3: Log n Is Not Always "Halving"
# ============================================================

def trick_3a_multiply(n):
    """O(log n) -- i doubles each step (reaches n in log n steps)"""
    i = 1
    while i < n:
        i *= 2             # 1, 2, 4, 8, 16... log n steps

def trick_3b_sqrt(n):
    """
    O(log log n) -- TRICKY!
    i goes: n, sqrt(n), sqrt(sqrt(n)), ...
    Number of times you can take sqrt before reaching ~1: log log n
    """
    while n > 1:
        n = int(n ** 0.5)

def trick_3c_log_inside_loop(n):
    """
    O(n log n) -- not O(n)!
    Outer: n iterations
    Inner: log n iterations (j doubles each time)
    """
    for i in range(n):                 # O(n)
        j = 1
        while j < n:
            j *= 2                     # O(log n)


# ============================================================
# TRICK 4: The Triangular Sum Pattern
# "Inner loop depends on outer loop variable"
# ============================================================

def trick_4a(n):
    """
    Inner loop runs: n + (n-1) + (n-2) + ... + 1 = n(n+1)/2
    STILL O(n^2) -- the constant 1/2 is dropped.
    """
    for i in range(n):
        for j in range(i, n):         # j starts at i, not 0
            pass                       # Still O(n^2)!

def trick_4b(n):
    """
    Same thing reversed:
    Inner loop runs: 1 + 2 + 3 + ... + n = n(n+1)/2 = O(n^2)
    """
    for i in range(n):
        for j in range(i + 1):        # j goes from 0 to i
            pass


# ============================================================
# TRICK 5: String/List Operations Have Hidden Costs
# ============================================================

def trick_5a_list_insert(arr, values):
    """
    LOOKS LIKE O(n)
    ACTUALLY O(n^2) -- insert(0, x) shifts all elements!

    Each insert at position 0 costs O(n) to shift everything right.
    n inserts * O(n) each = O(n^2)
    """
    for x in values:
        arr.insert(0, x)   # O(n) shift each time!

def trick_5a_fixed(arr, values):
    """O(n) - use deque for O(1) left insertion"""
    from collections import deque
    d = deque(arr)
    for x in values:
        d.appendleft(x)    # O(1)

def trick_5b_slice(arr):
    """
    LOOKS LIKE O(n)
    ACTUALLY O(n^2) -- slicing creates a COPY each time!

    arr[1:] copies n-1 elements.
    If done n times: (n-1) + (n-2) + ... + 1 = O(n^2)
    """
    while len(arr) > 1:
        arr = arr[1:]      # Creates new list, copies n-1 elements

def trick_5c_in_list(arr, targets):
    """
    'x in list' is O(n), NOT O(1)!
    'x in set' is O(1).
    'x in dict' is O(1).

    If targets has m elements:
      Using list: O(m * n)
      Using set:  O(m + n)  -- O(n) to build set, O(m) * O(1) to check
    """
    for t in targets:          # m iterations
        if t in arr:           # O(n) for list!
            print("found")


# ============================================================
# TRICK 6: Recursion Complexity Is Not Always Obvious
# ============================================================

def trick_6a(n):
    """
    Time: O(n), NOT O(2^n)!
    Only ONE recursive call each time -> linear chain, not tree.
    """
    if n <= 0:
        return
    trick_6a(n - 1)            # One branch only = O(n)

def trick_6b(n):
    """
    Time: O(2^n) -- TWO recursive calls = binary tree.
    """
    if n <= 0:
        return
    trick_6b(n - 1)            # Branch 1
    trick_6b(n - 1)            # Branch 2

def trick_6c(n):
    """
    Time: O(3^n) -- THREE recursive calls = ternary tree.
    Formula: O(branches ^ depth)
    """
    if n <= 0:
        return
    trick_6c(n - 1)
    trick_6c(n - 1)
    trick_6c(n - 1)

def trick_6d(n):
    """
    Time: O(n * 2^n), NOT just O(2^n)!
    Each node does O(n) work (the loop), and there are 2^n nodes.
    """
    if n <= 0:
        return
    for i in range(n):         # O(n) work at each node
        pass
    trick_6d(n - 1)
    trick_6d(n - 1)


# ============================================================
# TRICK 7: Sorting Hides in Many Solutions
# "Any solution that sorts first is at LEAST O(n log n)"
# ============================================================

def trick_7_median(arr):
    """
    LOOKS LIKE O(n) -- just one access after sort?
    ACTUALLY O(n log n) -- the sort dominates!

    Sort: O(n log n)
    Access middle: O(1)
    Total: O(n log n)
    """
    arr.sort()
    return arr[len(arr) // 2]


# ============================================================
# TRICK 8: Hash Map Operations - Average vs Worst Case
# ============================================================

def trick_8_hashmap():
    """
    dict/set operations in Python:
      - Average case: O(1) for get, set, in, delete
      - Worst case:   O(n) due to hash collisions

    In interviews, assume O(1) unless asked about worst case.
    Worst case happens with pathological inputs (all same hash).
    """
    d = {}
    d["key"] = "value"     # O(1) average
    _ = "key" in d         # O(1) average
    del d["key"]           # O(1) average


# ============================================================
# TRICK 9: Don't Forget the Output Size
# ============================================================

def trick_9_all_subsets(arr):
    """
    Time:  O(n * 2^n) -- 2^n subsets, each up to length n
    Space: O(n * 2^n) -- storing all subsets!

    Even if your algorithm is "efficient", if the output itself
    is 2^n items, your solution CANNOT be better than O(2^n).
    """
    if not arr:
        return [[]]
    rest = trick_9_all_subsets(arr[1:])
    return rest + [[arr[0]] + subset for subset in rest]


# ============================================================
# QUICK REFERENCE: TRICKY PATTERNS
# ============================================================
#
#  What you see                    | What it actually is
#  --------------------------------|------------------------
#  str += str in loop              | O(n^2) not O(n)
#  while j < n (j never resets)    | O(n) not O(n^2)
#  list.insert(0, x) in loop       | O(n^2) not O(n)
#  arr[1:] in loop                 | O(n^2) not O(n)
#  x in list                       | O(n) not O(1)
#  x in set/dict                   | O(1) average
#  1 recursive call                | O(n) not O(2^n)
#  2 recursive calls               | O(2^n)
#  sort + O(n) work                | O(n log n) not O(n)
#  inner loop 1+2+...+n            | O(n^2) not O(n)
#  j *= 2 inside loop              | O(log n) not O(n)
#
# ============================================================

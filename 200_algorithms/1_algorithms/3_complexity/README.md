# Algorithm Complexity - Quick Recognition Guide

## The ONE Rule: Count How Work Scales With Input Size (n)

> Don't count exact operations. Ask: **"If I double n, what happens to the runtime?"**

---

## Cheat Sheet: Recognize Complexity by Code Shape

| Complexity | Name | Doubles n -> Runtime... | Code Pattern | Real Example |
|---|---|---|---|---|
| **O(1)** | Constant | Stays same | Direct access, math | `arr[5]`, `hashmap["key"]` |
| **O(log n)** | Logarithmic | +1 step | Halving each step | Binary search |
| **O(n)** | Linear | Doubles | Single loop over n | Find max in array |
| **O(n log n)** | Linearithmic | Slightly > doubles | Divide + merge all | Merge sort, heap sort |
| **O(m * n)** | Two inputs | Depends on both | Nested loops over DIFFERENT inputs | Grid traversal, DP on 2 strings |
| **O(n^2)** | Quadratic | Quadruples (4x) | Nested loops over SAME input | Bubble sort, 2-sum brute force |
| **O(n^3)** | Cubic | 8x | Triple nested loops | Matrix multiplication (naive) |
| **O(2^n)** | Exponential | Squares | Recursion with 2 branches per call | Subsets, fibonacci (naive) |
| **O(n!)** | Factorial | Explodes | Permutations | Traveling salesman (brute force) |

---

## The 5 Golden Rules for Quick Recognition

### Rule 1: Count the Nested Loops

```
1 loop over n         -> O(n)
2 nested loops over n -> O(n^2)
3 nested loops over n -> O(n^3)
```

**BUT** only if each loop runs ~n times. A loop that runs a constant number of times (e.g., 26 for alphabet) is O(1).

### Rule 2: Halving = O(log n)

If in each step you **cut the problem in half**, it's O(log n).

```
while n > 0:
    n = n // 2      -> O(log n)
```

Binary search, balanced BST lookup, exponentiation by squaring.

### Rule 3: Divide and Conquer = O(n log n)

Split into halves (log n levels) + do O(n) work at each level = O(n log n).

Merge sort, quicksort (average), heap sort.

### Rule 4: Recursion with Multiple Branches = Exponential

```
f(n) = f(n-1) + f(n-1)    -> O(2^n)  (2 branches, depth n)
f(n) = f(n-1) + f(n-2)    -> O(2^n)  (fibonacci, ~1.618^n)
f(n) = 3 * f(n-1)         -> O(3^n)  (3 branches, depth n)
```

**Formula**: O(branches^depth)

### Rule 5: Drop Constants and Lower Terms

```
O(2n)       -> O(n)
O(n^2 + n)  -> O(n^2)
O(n/2)      -> O(n)
O(500)      -> O(1)
```

---

## O(m * n) vs O(n^2) - Two Inputs vs One Input

This confuses many people. The rule is simple:

- **O(n^2)**: Both loops iterate over the **same** input
- **O(m * n)**: Each loop iterates over a **different** input

```
# O(n^2) - same array used for both loops
for i in range(len(arr)):        # n
    for j in range(len(arr)):    # n  (same arr!)

# O(m * n) - two DIFFERENT dimensions
for i in range(rows):            # m
    for j in range(cols):        # n  (different from m!)
```

**When you see O(m * n), ask: what are m and n?**

| Problem | m | n | Complexity |
|---|---|---|---|
| Traverse a grid | rows | columns | O(m * n) |
| DP on two strings | len(string1) | len(string2) | O(m * n) |
| Flood fill / BFS on grid | rows | columns | O(m * n) |
| Graph traversal | vertices (V) | edges (E) | O(V + E) |

**O(n^2) is just O(m * n) where m = n.** If a grid is n x n (square), then O(m * n) = O(n * n) = O(n^2).

---

## Space Complexity Quick Rules

| Pattern | Space |
|---|---|
| Fixed variables only | O(1) |
| Array/list of size n | O(n) |
| 2D matrix n x n | O(n^2) |
| Recursion depth d | O(d) on call stack |
| Hash map with up to n entries | O(n) |

**Key insight**: Recursion uses stack space! Depth of recursion = space used.

```
Recursive binary search:  O(log n) space (depth = log n)
Recursive fibonacci:      O(n) space (depth = n, even though time is 2^n)
Iterative binary search:  O(1) space
```

---

## Speed Comparison (n = 1,000,000)

| Complexity | Operations | Feasible? |
|---|---|---|
| O(1) | 1 | Instant |
| O(log n) | ~20 | Instant |
| O(n) | 1,000,000 | ~1 second |
| O(n log n) | ~20,000,000 | ~few seconds |
| O(n^2) | 1,000,000,000,000 | ~hours/days |
| O(2^n) | ...incomprehensible | Heat death of universe |

---

## Files in This Directory (Study Materials)

| File | What You Learn |
|---|---|
| `1_recognize_by_code_pattern.py` | See code -> instantly know the complexity |
| `3_space_complexity.py` | Space complexity patterns with examples |
| `4_tricky_cases.py` | The gotchas that trip people up in interviews |

## Practice & Testing (separate directory)

Practice exercises and speedrun drills are in:
`201_interview/1_algorithms/3_complexity/`

Go there after studying the materials above.

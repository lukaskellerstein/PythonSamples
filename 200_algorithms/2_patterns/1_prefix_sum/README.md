

# INFO

Works on linear data structures.


Prefix sums are not limited to linear structures. Let me break it down.

---

### Where prefix sums work

The core idea — **precompute cumulative values so you can answer range queries fast** — applies anywhere you can define a meaningful "range."

---

### 1. Linear (1D arrays) ← what we've covered

```
Sum of subarray [i..j] = prefix[j+1] - prefix[i]
```

---

### 2. 2D Grids / Matrices

Sum of any rectangle in O(1). This shows up in image processing, game boards, and interview problems like LeetCode 304.

```
Original:          Prefix sum:
1  2  3            1   3   6
4  5  6            5  12  21
7  8  9           12  27  45
```

To get the sum of any rectangle, you use inclusion-exclusion — add and subtract overlapping regions.

---

### 3. Trees (Prefix sums on paths)

Very common in competitive programming. You compute cumulative sums from the root down to each node.

```
        5
       / \
      3    2
     / \
    1    4
```

The prefix sum from root to node `4` is `5 + 3 + 4 = 12`. If you want the sum of any path between two nodes, you use prefix sums combined with **Lowest Common Ancestor (LCA)**.

---

### 4. Graphs

Less common, but prefix sums apply on any path in a DAG (directed acyclic graph) where you can define a consistent traversal order.

---

### 5. Strings

Prefix sums on character frequencies. For example, to quickly answer "how many times does 'a' appear between index i and j?"

```
string:     "a b a a c b a"
prefix_a:  0  1  1  2  3  3  3  4

count of 'a' in range [2..6] = prefix_a[7] - prefix_a[2] = 4 - 1 = 3
```

---

### The general rule

Prefix sums work whenever you have an **associative operation** (addition, XOR, multiplication, min/max with special structures) over a sequence where you can define a cumulative order.

The key question is always the same: **"Can I precompute cumulative values so that the difference between two of them gives me the answer for a range?"**

---

Want to try a 2D prefix sum problem next, or continue with more 1D problems like LeetCode 525 (Contiguous Array)?
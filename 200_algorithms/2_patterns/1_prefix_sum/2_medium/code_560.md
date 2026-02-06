# Task

Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7


# Step 1

cumulativeSum = []
cumulativeSum.append(0)

for num in nums:
    cumulativeSum.append(cumulativeSum[-1] + num)
```

What this does, iteration by iteration:
```
Start:          cumulativeSum = [0]

num=3:  0 + 3  = 3    cumulativeSum = [0, 3]
num=4:  3 + 4  = 7    cumulativeSum = [0, 3, 7]
num=7:  7 + 7  = 14   cumulativeSum = [0, 3, 7, 14]
num=2:  14 + 2 = 16   cumulativeSum = [0, 3, 7, 14, 16]
num=-3: 16 - 3 = 13   cumulativeSum = [0, 3, 7, 14, 16, 13]
num=1:  13 + 1 = 14   cumulativeSum = [0, 3, 7, 14, 16, 13, 14]
num=4:  14 + 4 = 18   cumulativeSum = [0, 3, 7, 14, 16, 13, 14, 18]
num=2:  18 + 2 = 20   cumulativeSum = [0, 3, 7, 14, 16, 13, 14, 18, 20]
```

Each value represents the total sum from the start up to that point:
```
index:          0   1   2    3    4    5    6    7    8
cumulativeSum: [0,  3,  7,  14,  16,  13,  14,  18,  20]
                ↑
                empty prefix (no elements yet)
```

---

### Step 2: The core idea

If two positions in `cumulativeSum` differ by exactly `k`, the elements **between** them sum to `k`.
```
cumulativeSum[6] - cumulativeSum[2] = 14 - 7 = 7 = k ✅

This means nums[2] + nums[3] + nums[4] + nums[5] = 7 + 2 + (-3) + 1 = 7

# Step 2

count = 0
seen = {}

for cs in cumulativeSum:
    target = cs - k

    if target in seen:
        count += seen[target]

    seen[cs] = seen.get(cs, 0) + 1
```

Let's trace every iteration:

---

**Iteration 1: `cs = 0`**
```
target = 0 - 7 = -7
Is -7 in seen? NO         → count stays 0
Record: seen = {0: 1}
```

---

**Iteration 2: `cs = 3`**
```
target = 3 - 7 = -4
Is -4 in seen? NO         → count stays 0
Record: seen = {0: 1, 3: 1}
```

---

**Iteration 3: `cs = 7`**
```
target = 7 - 7 = 0
Is 0 in seen? YES, seen[0] = 1  → count = 0 + 1 = 1
                                   found: [3, 4] sums to 7
Record: seen = {0: 1, 3: 1, 7: 1}
```

Why does this work? `cumulativeSum = 7` at current position, `cumulativeSum = 0` existed earlier. The difference is 7 = k, so everything between those two positions sums to k. That's `nums[0] + nums[1]` = `3 + 4` = `7`.

---

**Iteration 4: `cs = 14`**
```
target = 14 - 7 = 7
Is 7 in seen? YES, seen[7] = 1  → count = 1 + 1 = 2
                                   found: [7] sums to 7
Record: seen = {0: 1, 3: 1, 7: 1, 14: 1}
```

---

**Iteration 5: `cs = 16`**
```
target = 16 - 7 = 9
Is 9 in seen? NO           → count stays 2
Record: seen = {0: 1, 3: 1, 7: 1, 14: 1, 16: 1}
```

---

**Iteration 6: `cs = 13`**
```
target = 13 - 7 = 6
Is 6 in seen? NO           → count stays 2
Record: seen = {0: 1, 3: 1, 7: 1, 14: 1, 16: 1, 13: 1}
```

---

**Iteration 7: `cs = 14`**
```
target = 14 - 7 = 7
Is 7 in seen? YES, seen[7] = 1  → count = 2 + 1 = 3
                                   found: [7, 2, -3, 1] sums to 7
Record: seen = {0: 1, 3: 1, 7: 1, 14: 2, 16: 1, 13: 1}
                                      ↑ now 2, because we've seen 14 twice
```

---

**Iteration 8: `cs = 18`**
```
target = 18 - 7 = 11
Is 11 in seen? NO          → count stays 3
Record: seen = {..., 18: 1}
```

---

**Iteration 9: `cs = 20`**
```
target = 20 - 7 = 13
Is 13 in seen? YES, seen[13] = 1  → count = 3 + 1 = 4
                                     found: [1, 4, 2] sums to 7
Record: seen = {..., 20: 1}

# -----------------------
# Daily Temperatures (LeetCode 739)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Monotonic Decreasing Stack (Next Greater Element)

# Problem: Given an array of integers temperatures represents the daily
# temperatures, return an array answer such that answer[i] is the number of
# days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0.

# -----------------------

# For temperatures [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]
# Day 0 (73): next warmer is day 1 (74) → wait 1
# Day 2 (75): next warmer is day 6 (76) → wait 4
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]

# ----------------------------------------------------
# Monotonic Stack solution
#
# Maintain a decreasing stack of indices. When current temp is warmer
# than the top of stack, pop and record the distance.
#
# time complexity = O(n) - each index pushed and popped at most once
# space complexity = O(n) - stack + result array
# ----------------------------------------------------


def daily_temperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices, temps at these indices are in decreasing order

    for i in range(n):
        # Pop all indices whose temperature is less than current
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_idx = stack.pop()
            answer[prev_idx] = i - prev_idx
        stack.append(i)

    return answer


# Example
print(daily_temperatures(temperatures))  # [1, 1, 4, 2, 1, 1, 0, 0]


# ----------------------------------------------------
# Brute Force solution
#
# For each day, scan forward to find the next warmer day.
#
# time complexity = O(n^2) - nested scan for each element
# space complexity = O(n) - result array only
# ----------------------------------------------------


def daily_temperatures_brute(temperatures):
    n = len(temperatures)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break

    return answer


# Example
print(daily_temperatures_brute(temperatures))  # [1, 1, 4, 2, 1, 1, 0, 0]

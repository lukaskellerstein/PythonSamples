# -----------------------
# Daily Temperatures (LeetCode 739)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of integers temperatures represents the daily
# temperatures, return an array answer such that answer[i] is the number
# of days you have to wait after the ith day to get a warmer temperature.
# If there is no future day for which this is possible, keep answer[i] == 0.

# -----------------------
# VISUALIZATION
# -----------------------
#
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#
# Process left to right with monotonic decreasing stack (storing indices):
#   i=0 (val=73): stack=[]             -> push 0, stack=[0]
#   i=1 (val=74): pop 0 (73<74)        -> answer[0]=1-0=1, push 1, stack=[1]
#   i=2 (val=75): pop 1 (74<75)        -> answer[1]=2-1=1, push 2, stack=[2]
#   i=3 (val=71): peek 75 (75>71)      -> push 3, stack=[2,3]
#   i=4 (val=69): peek 71 (71>69)      -> push 4, stack=[2,3,4]
#   i=5 (val=72): pop 4 (69<72)        -> answer[4]=5-4=1
#                 pop 3 (71<72)        -> answer[3]=5-3=2
#                 peek 75 (75>72)      -> push 5, stack=[2,5]
#   i=6 (val=76): pop 5 (72<76)        -> answer[5]=6-5=1
#                 pop 2 (75<76)        -> answer[2]=6-2=4
#                 stack=[]             -> push 6, stack=[6]
#   i=7 (val=73): peek 76 (76>73)      -> push 7, stack=[6,7]
#
# Remaining in stack [6,7] -> answer[6]=0, answer[7]=0
#
# Result: [1, 1, 4, 2, 1, 1, 0, 0]
#
# -----------------------

from typing import List


# ----------------------------------------------------
# Monotonic Stack solution (Optimal)
#
# time complexity = O(n) - each element pushed and popped at most once
# space complexity = O(n) - stack can hold up to n indices
# ----------------------------------------------------

def daily_temperatures(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n
    stack = []  # monotonic decreasing stack (stores indices)

    for i in range(n):
        # Pop indices whose temperature is less than current
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev = stack.pop()
            answer[prev] = i - prev
        stack.append(i)

    return answer


# Example
print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2) - for each day, scan all future days
# space complexity = O(1) - no extra space beyond output
# ----------------------------------------------------

def daily_temperatures_brute_force(temperatures: List[int]) -> List[int]:
    n = len(temperatures)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temperatures[j] > temperatures[i]:
                answer[i] = j - i
                break

    return answer


# Example
print(daily_temperatures_brute_force([73, 74, 75, 71, 69, 72, 76, 73]))  # [1, 1, 4, 2, 1, 1, 0, 0]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),
        ([30, 40, 50, 60], [1, 1, 1, 0]),
        ([30, 60, 90], [1, 1, 0]),
        ([90, 80, 70, 60], [0, 0, 0, 0]),
        ([50], [0]),
        ([70, 70, 70], [0, 0, 0]),
    ]

    print("\nDaily Temperatures Results:")
    print("-" * 70)
    print(f"{'temperatures':<30} {'Optimal':<25} {'Brute':<25}")
    print("-" * 70)

    for temps, expected in test_cases:
        result1 = daily_temperatures(temps)
        result2 = daily_temperatures_brute_force(temps)
        status = "✓" if result1 == expected and result2 == expected else "✗"
        print(f"{str(temps):<30} {str(result1):<25} {str(result2):<25} {status}")
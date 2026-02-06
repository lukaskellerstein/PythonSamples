
# -----------------------
# Merge Intervals (LeetCode 56)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of intervals where intervals[i] = [starti, endi],
# merge all overlapping intervals, and return an array of the non-overlapping
# intervals that cover all the intervals in the input.

# -----------------------

# For given intervals [[1,3],[2,6],[8,10],[15,18]], merge overlapping ones.
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# ----------------------------------------------------
# Sorting solution (Optimal)
#
# time complexity = O(n log n) - dominated by sorting
# space complexity = O(n) - for the result array (O(log n) for sorting)
# ----------------------------------------------------


def merge(intervals):
    if not intervals:
        return []

    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])

    result = [intervals[0]]

    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = result[-1]

        # If current interval overlaps with the last merged interval
        if current[0] <= last_merged[1]:
            # Merge by extending the end time
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval to result
            result.append(current)

    return result


# Example
print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
print(merge([[1, 4], [4, 5]]))  # [[1, 5]]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2) - compare each interval with every other
# space complexity = O(n) - for the result array
# ----------------------------------------------------


def merge_brute_force(intervals):
    if not intervals:
        return []

    # Mark intervals as merged using a set
    n = len(intervals)
    merged = [False] * n

    # Convert to mutable list of lists
    intervals = [list(interval) for interval in intervals]

    # Compare each pair of intervals and merge if overlapping
    changed = True
    while changed:
        changed = False
        for i in range(n):
            if merged[i]:
                continue
            for j in range(i + 1, n):
                if merged[j]:
                    continue

                # Check if intervals[i] and intervals[j] overlap
                if intervals[i][0] <= intervals[j][1] and intervals[j][0] <= intervals[i][1]:
                    # Merge j into i
                    intervals[i][0] = min(intervals[i][0], intervals[j][0])
                    intervals[i][1] = max(intervals[i][1], intervals[j][1])
                    merged[j] = True
                    changed = True

    # Collect non-merged intervals
    result = [intervals[i] for i in range(n) if not merged[i]]

    return result


# Example
print(merge_brute_force([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1, 6], [8, 10], [15, 18]]
print(merge_brute_force([[1, 4], [4, 5]]))  # [[1, 5]]


# -----------------------
# Meeting Rooms I (LeetCode 252)
# -----------------------

# Difficulty: Easy

# Problem: Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings (i.e., no two meetings overlap).

# -----------------------

# For given intervals [[0,30],[5,10],[15,20]], can a person attend all? No, overlaps exist.
intervals1 = [[0, 30], [5, 10], [15, 20]]
# For given intervals [[7,10],[2,4]], can a person attend all? Yes, no overlaps.
intervals2 = [[7, 10], [2, 4]]

# ----------------------------------------------------
# Sorting solution (Optimal)
#
# time complexity = O(n log n) - dominated by sorting
# space complexity = O(1) - only using pointers (O(log n) for sorting)
# ----------------------------------------------------


def can_attend_meetings(intervals):
    if not intervals:
        return True

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Check if any meeting starts before the previous one ends
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


# Example
print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # False
print(can_attend_meetings([[7, 10], [2, 4]]))  # True


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2) - compare each pair of intervals
# space complexity = O(1) - no extra space needed
# ----------------------------------------------------


def can_attend_meetings_brute_force(intervals):
    if not intervals:
        return True

    n = len(intervals)

    # Compare each pair of meetings for overlap
    for i in range(n):
        for j in range(i + 1, n):
            # Check if intervals[i] and intervals[j] overlap
            # Two intervals overlap if: start1 < end2 AND start2 < end1
            if intervals[i][0] < intervals[j][1] and intervals[j][0] < intervals[i][1]:
                return False

    return True


# Example
print(can_attend_meetings_brute_force([[0, 30], [5, 10], [15, 20]]))  # False
print(can_attend_meetings_brute_force([[7, 10], [2, 4]]))  # True


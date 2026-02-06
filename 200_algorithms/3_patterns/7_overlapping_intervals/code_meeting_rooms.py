
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


# ====================================================================================
# ====================================================================================


# -----------------------
# Meeting Rooms II (LeetCode 253)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of meeting time intervals where intervals[i] = [starti, endi],
# return the minimum number of conference rooms required to schedule all meetings.

# -----------------------

# For given intervals [[0,30],[5,10],[15,20]], minimum rooms needed = 2
intervals3 = [[0, 30], [5, 10], [15, 20]]
# For given intervals [[7,10],[2,4]], minimum rooms needed = 1
intervals4 = [[7, 10], [2, 4]]

# ----------------------------------------------------
# Min Heap solution (Optimal)
#
# time complexity = O(n log n) - sorting + heap operations
# space complexity = O(n) - heap can contain all meetings
# ----------------------------------------------------

import heapq


def min_meeting_rooms(intervals):
    if not intervals:
        return 0

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    # Min heap to track end times of ongoing meetings
    heap = []

    for interval in intervals:
        # If earliest ending meeting has ended, remove it
        if heap and heap[0] <= interval[0]:
            heapq.heappop(heap)

        # Add current meeting's end time
        heapq.heappush(heap, interval[1])

    # Heap size = number of rooms needed
    return len(heap)


# Example
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # 2
print(min_meeting_rooms([[7, 10], [2, 4]]))  # 1


# ----------------------------------------------------
# Chronological Ordering / Sweep Line solution (Optimal Alternative)
#
# time complexity = O(n log n) - sorting the events
# space complexity = O(n) - storing start and end events
# ----------------------------------------------------


def min_meeting_rooms_sweep_line(intervals):
    if not intervals:
        return 0

    # Create events: +1 for start, -1 for end
    events = []
    for start, end in intervals:
        events.append((start, 1))   # meeting starts
        events.append((end, -1))    # meeting ends

    # Sort by time; if same time, end (-1) comes before start (+1)
    # This handles the case where one meeting ends exactly when another starts
    events.sort(key=lambda x: (x[0], x[1]))

    max_rooms = 0
    current_rooms = 0

    for time, delta in events:
        current_rooms += delta
        max_rooms = max(max_rooms, current_rooms)

    return max_rooms


# Example
print(min_meeting_rooms_sweep_line([[0, 30], [5, 10], [15, 20]]))  # 2
print(min_meeting_rooms_sweep_line([[7, 10], [2, 4]]))  # 1


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2) - for each meeting, count overlaps
# space complexity = O(1) - only using counters
# ----------------------------------------------------


def min_meeting_rooms_brute_force(intervals):
    if not intervals:
        return 0

    max_rooms = 0
    n = len(intervals)

    # For each meeting, count how many other meetings overlap with it
    for i in range(n):
        rooms_needed = 1  # current meeting needs a room

        for j in range(n):
            if i != j:
                # Check if meeting j overlaps with meeting i
                # j overlaps i if: j starts before i ends AND j ends after i starts
                if intervals[j][0] < intervals[i][1] and intervals[j][1] > intervals[i][0]:
                    # But we only count if j started before or at the same time as i
                    # to avoid double counting
                    if intervals[j][0] <= intervals[i][0]:
                        rooms_needed += 1

        max_rooms = max(max_rooms, rooms_needed)

    return max_rooms


# Example
print(min_meeting_rooms_brute_force([[0, 30], [5, 10], [15, 20]]))  # 2
print(min_meeting_rooms_brute_force([[7, 10], [2, 4]]))  # 1

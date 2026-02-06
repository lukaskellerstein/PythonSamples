
# -----------------------
# Course Schedule (LeetCode 207)
# -----------------------

# Difficulty: Medium

# Problem: There are numCourses courses labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi]
# indicates that you must take course bi first if you want to take course ai.
#
# Return true if you can finish all courses. Otherwise, return false.
# (i.e., detect if there's a cycle in the directed graph)

# -----------------------

# Example 1:
# Input: numCourses = 4, prerequisites = [[1,0],[2,1],[3,2]]
# Output: true (take 0 → 1 → 2 → 3)
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
# Output: false (cycle: 0 needs 1, 1 needs 0)

from collections import defaultdict, deque


# ----------------------------------------------------
# DFS with Cycle Detection solution (Optimal)
#
# time complexity = O(V + E) - visit each node and edge once
# space complexity = O(V + E) - adjacency list and recursion stack
#
# Idea: Use DFS with three states: unvisited (0), visiting (1), visited (2).
# If we encounter a "visiting" node during DFS, we found a cycle.
# This is topological sort cycle detection.
# ----------------------------------------------------


def can_finish_dfs(numCourses, prerequisites):
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    # States: 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:  # Currently visiting -> cycle found
            return True
        if state[course] == 2:  # Already processed -> no cycle from here
            return False

        state[course] = 1  # Mark as visiting

        for next_course in graph[course]:
            if has_cycle(next_course):
                return True

        state[course] = 2  # Mark as visited
        return False

    # Check all courses (graph might be disconnected)
    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True


print(can_finish_dfs(4, [[1, 0], [2, 1], [3, 2]]))  # True
print(can_finish_dfs(2, [[0, 1], [1, 0]]))  # False
print(can_finish_dfs(3, [[0, 1], [0, 2], [1, 2]]))  # True


# ----------------------------------------------------
# DFS with Visited Set solution (Alternative)
#
# time complexity = O(V + E)
# space complexity = O(V + E)
#
# Idea: Use separate sets for current path and fully visited nodes.
# ----------------------------------------------------


def can_finish_dfs_sets(numCourses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    visited = set()      # Fully processed nodes
    path = set()         # Current DFS path

    def dfs(course):
        if course in path:      # Cycle detected
            return False
        if course in visited:   # Already processed
            return True

        path.add(course)

        for next_course in graph[course]:
            if not dfs(next_course):
                return False

        path.remove(course)
        visited.add(course)
        return True

    for course in range(numCourses):
        if not dfs(course):
            return False

    return True


print(can_finish_dfs_sets(4, [[1, 0], [2, 1], [3, 2]]))  # True
print(can_finish_dfs_sets(2, [[0, 1], [1, 0]]))  # False
print(can_finish_dfs_sets(3, [[0, 1], [0, 2], [1, 2]]))  # True


# ----------------------------------------------------
# Brute Force solution (Check all paths)
#
# time complexity = O(V * (V + E)) - DFS from each node
# space complexity = O(V + E)
#
# Idea: For each course, do a DFS to see if we can reach back to it
# (cycle detection by checking if starting node is reachable).
# Less efficient but conceptually simpler.
# ----------------------------------------------------


def can_finish_brute_force(numCourses, prerequisites):
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    def can_reach(start, current, visited):
        """Check if we can reach 'start' from 'current'."""
        if current == start and len(visited) > 0:
            return True  # Found a cycle back to start

        if current in visited:
            return False

        visited.add(current)

        for next_course in graph[current]:
            if can_reach(start, next_course, visited):
                return True

        return False

    # Check if any course can reach itself (cycle)
    for course in range(numCourses):
        if can_reach(course, course, set()):
            return False

    return True


print(can_finish_brute_force(4, [[1, 0], [2, 1], [3, 2]]))  # True
print(can_finish_brute_force(2, [[0, 1], [1, 0]]))  # False
print(can_finish_brute_force(3, [[0, 1], [0, 2], [1, 2]]))  # True

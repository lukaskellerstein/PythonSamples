
# ============================================================
# PROBLEM: Course Schedule (LeetCode 207)
# ============================================================
# Difficulty: Medium
# Pattern: Graph Traversal - DFS (Pre-Order) / Cycle Detection
#
# There are numCourses courses labeled from 0 to numCourses - 1. You are
# given an array prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi before course ai. Return true if you can
# finish all courses, otherwise return false. This is equivalent to
# detecting whether a directed graph contains a cycle.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: numCourses = 4, prerequisites = [[1,0],[2,1],[3,2]]
#   Output: true
#   Explanation: Take courses in order 0 -> 1 -> 2 -> 3. No cycles.
#
# Example 2:
#   Input: numCourses = 2, prerequisites = [[0,1],[1,0]]
#   Output: false
#   Explanation: Course 0 requires 1, and course 1 requires 0. Cycle!
#
# Example 3:
#   Input: numCourses = 3, prerequisites = [[0,1],[0,2],[1,2]]
#   Output: true
#   Explanation: Take 2 -> 1 -> 0. No cycles.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= numCourses <= 2000
# - 0 <= prerequisites.length <= 5000
# - prerequisites[i].length == 2
# - 0 <= ai, bi < numCourses
# - All prerequisite pairs are unique
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Example 1: numCourses=4, prereqs=[[1,0],[2,1],[3,2]]
#
#   0 --> 1 --> 2 --> 3    (linear chain, no cycle -> true)
#
# Example 2: numCourses=2, prereqs=[[0,1],[1,0]]
#
#   0 <--> 1               (cycle -> false)
#
# DFS cycle detection uses three states:
#   0 = unvisited
#   1 = visiting (in current DFS path)
#   2 = visited  (fully processed)
#
# If we encounter a node in state 1, a cycle exists.
#

from typing import List
from collections import defaultdict


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def can_finish_brute_force(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (DFS with 3-state cycle detection)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass

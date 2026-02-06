


# 1. Prefix sum

Query sum of elements in subarray.

Example:
Array = [1,2,3,4,5,6]
Give me a sum of number from index 3 to 5.

LeetCode:
Range Sum Query - Immutable
Contiguous Array
Subarray Sum Equals K


# 2. Two pointers pattern

During one iteration having two pointers in array and move them closer together.

Example:
Array = ["A", "N", "N", "A"]

Is string a palindrome? 
Is number a palindrome?

LeetCode:
Two Sum - Input Array is Sorted
3Sum
Container with Most Water


# 3. Sliding Window


Example:
Find subarray of size 'K' with maximum sum

[3, 2, 7, 5, 9, 6, 2], K=3

Brute force = two for loops = O(N*K)
Sliding Window = O(N)


LeetCode:
Maximum Average Subarray
Longest Substring Without Repeating Characters
Minimum Window Substring


# 4. Fast and Slow Pointers 
Moving two pointers in different speeds => It is a variant of Two pointers pattern


Example:
Does linkedlist contain a cycle?

LeetCode:
Linked List Cycle
Happy Number
Find the duplicate number


# 5. Linked List in-place reversal


Example:
Reverse pointers in linkedlist in only one iteration

LeetCode:
Reverse Linked List
Swap nodes in pairs


# 6. Monotonic Stack

Find "next greater" or "next smaller" element in array.

Example:
Given an array, find the next greater element for each item. If there isn't one, output -1.

Brute force = two for loops = O(n^2)
Stack = O(n)


LeetCode:
Next Greater Element
Daily temperature
Largest Rectangle in Histogram


# 7. Top "K" element 

Find "K largest" or "K smallest" or "K most frequent" elements in array.

Brute force = sort and take K elements = O(n log n) time
Min/Max HEAP =  O(n log k) ??? how is it different ???

LeetCode:
Kth largest element in an Array
Top K frequent Elements
Find K pairs with smallest sums


# 8. Overlapping intervals

Intervals and ranges that might overlap.

Example:

1) Merging intervals

2) Interval intersections

3) Insert Interval

Example: 

Find minimum meeting rooms needed for overlapping meeting times.

LeetCode:
Merge Intervals
Insert Interval
Non-overlapping intervals



# 9. Modified Binary Search - IGNORE

TBD
 
 
# 10. Binary Tree Traversal 

PreOrder, InOrder, PostOrder, LevelOrder.


> To retrieve the values of a binary search tree in sorted order, use **inorder traversal**
>
> To create a copy of a tree (serialization), use **preorder traversal**
>
> When you want to process child nodes before the parent, use **postorder traversal**
>
> When you need to explore all nodes at the current level before the next, use **level order traversal**

LeetCode:

PreOrder: Binary tree paths
InOrder: Kth smallest element in a BST
PostOrder: Binary Tree Maximum Path Sum
LevelOrder: Binary Tree Level Order Traversal 


# 11. DFS - Depth-First Search 

For Graphs and Trees.

Example:
Finding a path between two nodes.
Check if graph contains a cycle.
Finding a topological order in a directed acyclic graph (DAG).
Counting number of connected components in a graph

LeetCode:
Clone Graph
Path Sum
Course Schedule



# 12. BFS - Breadth-First Search 

For Graphs and Trees.

Uses Queue. 

Example:
Finding the shortes path between two nodes.
Printing all nodes of a tree level by level.
Finding all connected components in a graph.
Finding the shortest transformation sequence from one word to other.

LeetCode:
Binary Tree level Order traversa
Rotting oranges
Word ladder


# 13. Matrix traversal - Ignore

TBD


# 14. Backtracking

TBD


# 15. Dynamic programming


TBD
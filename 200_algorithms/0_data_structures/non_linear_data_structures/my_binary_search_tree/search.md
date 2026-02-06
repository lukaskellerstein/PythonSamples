| **Search Type**        | **Nodes Explored**                        | **Time Complexity**                |
| ---------------------- | ----------------------------------------- | ---------------------------------- |
| Binary Search (on BST) | Only nodes along the search path          | O(h), where h is the tree's height |
| BFS                    | All nodes level-by-level                  | O(n)                               |
| DFS                    | All nodes in a chosen order (pre/in/post) | O(n)                               |

Why is Binary Search Faster?
Targeted Search:
Binary search only explores a specific path (e.g., left or right) instead of visiting every node like BFS or DFS.

Time Complexity:

If the tree is balanced, the height of the tree is approximately
log
⁡
𝑛
logn, giving a time complexity of
𝑂
(
log
⁡
𝑛
)
O(logn).
BFS and DFS both require
𝑂
(
𝑛
)
O(n) because they may visit every node, even if the value is found early.
Worst Case:

If the tree is unbalanced (like a skewed tree where every node has only one child), the height
ℎ
h can be equal to
𝑛
n, making the time complexity degrade to
𝑂
(
𝑛
)
O(n), which is the same as BFS/DFS.

# Stage 2: Data Structures & Algorithms

Implement every DSA from scratch with Big-O analysis.

## Topics

1. Big-O Analysis — time/space complexity, amortized analysis
2. Arrays & Strings — dynamic arrays, two-pointer, sliding window, KMP
3. Linked Lists — singly, doubly, circular, Floyd's cycle detection
4. Stacks & Queues — monotonic stack, deque, priority queue
5. Hash Tables — collision resolution, load factor $\alpha = n/m$
6. Trees — BST, AVL (rotations), Trie, Segment Tree
7. Heaps — binary heap, heapify, heap sort
8. Graphs — BFS, DFS, Dijkstra, A*, MST (Kruskal, Prim)
9. Dynamic Programming — memoization, tabulation, classic problems
10. Greedy & Backtracking — activity selection, N-Queens

## Key Math

Master Theorem: $T(n) = aT(n/b) + f(n)$

Edit Distance: $dp[i][j] = \min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1] + [s_i \neq t_j])$

## Projects

1. Pathfinding Visualizer (BFS/DFS/Dijkstra/A*)
2. LRU + TTL Cache

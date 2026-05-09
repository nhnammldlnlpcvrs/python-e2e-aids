# ============================================
# 22. MST & UNION-FIND - CÂY KHUNG NHỎ NHẤT & DISJOINT SET
# ============================================
# MST (Minimum Spanning Tree): cây khung có tổng trọng số nhỏ nhất.
# Kruskal: sắp xếp cạnh + DSU - O(E log E).
# Prim: hàng đợi ưu tiên - O((V+E) log V).

import heapq
from collections import defaultdict


# ==============================
# UNION-FIND (DISJOINT SET UNION)
# ==============================

class UnionFind:
    """Disjoint Set Union với path compression + union by rank"""

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n

    def find(self, x):
        """Tìm đại diện của tập chứa x - O(alpha(n))"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        """Hợp nhất tập chứa x và y - O(alpha(n))"""
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        self.components -= 1
        return True

    def connected(self, x, y):
        """Kiểm tra x và y cùng tập không"""
        return self.find(x) == self.find(y)


# ==============================
# KRUSKAL - O(E log E)
# ==============================

def kruskal(vertices, edges):
    """Kruskal's MST algorithm.
    vertices: số đỉnh (0..V-1)
    edges: [(u, v, w), ...]"""
    # Sắp xếp cạnh theo trọng số tăng dần
    edges_sorted = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(vertices)
    mst = []
    total_weight = 0
    for u, v, w in edges_sorted:
        if uf.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == vertices - 1:
                break
    return mst, total_weight


# ==============================
# PRIM - O((V+E) log V)
# ==============================

def prim(graph, start=0):
    """Prim's MST algorithm.
    graph: dict {u: [(v, w), ...]}"""
    visited = set()
    mst = []
    total_weight = 0
    # Priority queue: (weight, u, v)
    pq = [(0, start, start)]  # (w, from, to)

    while pq and len(visited) < len(graph):
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue
        visited.add(v)
        if u != v:  # Không phải đỉnh start
            mst.append((u, v, w))
            total_weight += w
        for neighbor, weight in graph.get(v, []):
            if neighbor not in visited:
                heapq.heappush(pq, (weight, v, neighbor))

    return mst, total_weight


# ==============================
# Demo
# ==============================

# Đồ thị mẫu:
#       (0)--10--(1)--6--(2)
#       | \      |      / |
#      7|  8    5|    /  9|
#       |    \   |  /     |
#      (3)   (4) (5)    (6)
#       |    /   |    \  |
#      5|  3     2     4 |
#       | /      |       |
#      (7)--1--(8)--7--(9)

print("=== Đồ thị mẫu ===")
V = 10
edges = [
    (0, 1, 10), (0, 3, 7), (0, 4, 8),
    (1, 2, 6), (1, 5, 5),
    (2, 5, 9), (2, 6, 4),
    (3, 7, 5), (3, 4, 3),
    (4, 7, 3), (4, 5, 1),
    (5, 6, 4), (5, 8, 2),
    (7, 8, 1), (7, 9, 7), (8, 9, 7),
]
print(f"Số đỉnh: {V}, Số cạnh: {len(edges)}")

# Chuyển sang adjacency list cho Prim
graph_adj = defaultdict(list)
for u, v, w in edges:
    graph_adj[u].append((v, w))
    graph_adj[v].append((u, w))

print("\n--- Kruskal ---")
mst_k, weight_k = kruskal(V, edges)
print(f"MST edges: {mst_k}")
print(f"Total weight: {weight_k}")

print("\n--- Prim ---")
mst_p, weight_p = prim(graph_adj, 0)
print(f"MST edges: {mst_p}")
print(f"Total weight: {weight_p}")
print(f"Kruskal weight == Prim weight: {weight_k == weight_p}")

# ==============================
# Union-Find demo
# ==============================

print("\n=== Union-Find Demo ===")
uf = UnionFind(10)
print("Initial components:", uf.components)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)
uf.union(5, 6)
uf.union(6, 7)
uf.union(7, 8)
print(f"Sau 6 union: components={uf.components}")
print(f"connected(0,2): {uf.connected(0, 2)}")  # True - cùng tập
print(f"connected(0,3): {uf.connected(0, 3)}")  # False
print(f"connected(5,8): {uf.connected(5, 8)}")  # True
uf.union(2, 4)  # Nối 2 tập lớn
print(f"Sau union(2,4): components={uf.components}")
print(f"connected(0,4): {uf.connected(0, 4)}")  # True

# ==============================
# Ứng dụng: Kruskal clustering
# ==============================

print("\n=== Ứng dụng: Clustering với Kruskal ===")

def kruskal_clustering(vertices, edges, k):
    """Chia vertices thành k clusters, cực đại khoảng cách tối thiểu giữa clusters.
    Ý tưởng: chạy Kruskal, dừng khi còn k components."""
    edges_sorted = sorted(edges, key=lambda e: e[2])
    uf = UnionFind(vertices)
    for u, v, w in edges_sorted:
        if uf.components == k:
            break
        uf.union(u, v)
    # Khoảng cách giữa 2 cluster gần nhất = trọng số cạnh tiếp theo
    for u, v, w in edges_sorted:
        if not uf.connected(u, v):
            return w  # Max-spacing
    return 0


max_spacing = kruskal_clustering(V, edges, 3)
print(f"Max spacing với k=3 clusters: {max_spacing}")

# ==============================
# Ứng dụng: Cycle detection
# ==============================

def has_cycle_union_find(vertices, edges):
    """Phát hiện chu trình trong đồ thị vô hướng dùng Union-Find"""
    uf = UnionFind(vertices)
    for u, v, w in edges:
        if not uf.union(u, v):  # Đã cùng tập -> có cycle
            return True
    return False

print(f"\nCycle trong đồ thị mẫu?: {has_cycle_union_find(V, edges)}")
# Đồ thị không cycle: chỉ 2 cạnh cho 3 đỉnh
print(f"Cycle trong cây 0-1-2?: {has_cycle_union_find(3, [(0,1,1),(1,2,1)])}")

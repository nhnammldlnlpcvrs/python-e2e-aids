# ============================================
# 12. GRAPHS - ĐỒ THỊ / GRAPHS
# ============================================
# Graph G = (V, E): V = tập đỉnh, E = tập cạnh.
# Có hướng / vô hướng, có trọng số / không trọng số.

from collections import deque, defaultdict


class Graph:
    """Đồ thị vô hướng - Adjacency List"""

    def __init__(self):
        self.adj = defaultdict(list)

    def add_vertex(self, v):
        """Thêm đỉnh (tự động khi thêm cạnh, nhưng có thể gọi tường minh)"""
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        """Thêm cạnh vô hướng u-v"""
        self.adj[u].append(v)
        self.adj[v].append(u)

    def remove_edge(self, u, v):
        """Xóa cạnh u-v"""
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if u in self.adj[v]:
            self.adj[v].remove(u)

    def get_neighbors(self, v):
        return self.adj.get(v, [])

    def degree(self, v):
        """Bậc của đỉnh"""
        return len(self.adj.get(v, []))

    def num_vertices(self):
        return len(self.adj)

    def num_edges(self):
        """Số cạnh (mỗi cạnh đếm 2 lần trong adj list)"""
        return sum(len(v) for v in self.adj.values()) // 2

    def display(self):
        print("  Adjacency List:")
        for v in sorted(self.adj.keys()):
            print(f"    {v} -> {self.adj[v]}")


class DiGraph:
    """Đồ thị có hướng - Adjacency List"""

    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        """Thêm cạnh u -> v"""
        self.adj[u].append(v)
        if v not in self.adj:
            self.adj[v] = []

    def in_degree(self, v):
        """Bậc vào của đỉnh"""
        count = 0
        for neighbors in self.adj.values():
            if v in neighbors:
                count += 1
        return count

    def out_degree(self, v):
        """Bậc ra của đỉnh"""
        return len(self.adj.get(v, []))

    def display(self):
        print("  Adjacency List (có hướng):")
        for v in sorted(self.adj.keys()):
            print(f"    {v} -> {self.adj[v]}")


class WeightedGraph:
    """Đồ thị vô hướng có trọng số - Adjacency List"""

    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, weight):
        """Thêm cạnh u-v với trọng số w"""
        self.adj[u].append((v, weight))
        self.adj[v].append((u, weight))

    def display(self):
        print("  Weighted Adjacency List:")
        for v in sorted(self.adj.keys()):
            print(f"    {v} -> {self.adj[v]}")


# ==============================
# Demo: Đồ thị vô hướng
# ==============================

print("=== Đồ thị vô hướng ===")
#    0 -- 1
#    |  / |
#    | /  |
#    2 -- 3
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.display()
print("Số đỉnh:", g.num_vertices())
print("Số cạnh:", g.num_edges())
print("Bậc của đỉnh 1:", g.degree(1))
print("Neighbors của 1:", g.get_neighbors(1))

# ==============================
# Demo: Đồ thị có hướng
# ==============================

print("\n=== Đồ thị có hướng ===")
#    0 -> 1
#    |  /^
#    v / |
#    2 -> 3
dg = DiGraph()
dg.add_edge(0, 1)
dg.add_edge(0, 2)
dg.add_edge(1, 2)
dg.add_edge(2, 3)
dg.add_edge(3, 1)
dg.display()
print("out_degree(2):", dg.out_degree(2))
print("in_degree(2):", dg.in_degree(2))

# ==============================
# Demo: Đồ thị có trọng số
# ==============================

print("\n=== Đồ thị có trọng số ===")
#       5
#    0 --- 1
#   2|  \  |3
#    |  4\ |
#    2 --- 3
#       1
wg = WeightedGraph()
wg.add_edge(0, 1, 5)
wg.add_edge(0, 2, 2)
wg.add_edge(0, 3, 4)
wg.add_edge(1, 3, 3)
wg.add_edge(2, 3, 1)
wg.display()

# ==============================
# Adjacency Matrix
# ==============================

print("\n=== Adjacency Matrix ===")

def to_adjacency_matrix(graph, vertices):
    """Chuyển adjacency list sang matrix"""
    n = len(vertices)
    idx_map = {v: i for i, v in enumerate(vertices)}
    matrix = [[0] * n for _ in range(n)]
    for u in vertices:
        for v in graph.get_neighbors(u):
            matrix[idx_map[u]][idx_map[v]] = 1
    return matrix


def print_matrix(matrix, vertices):
    """In ma trận kề"""
    print("   ", " ".join(str(v) for v in vertices))
    for i, v in enumerate(vertices):
        print(f"  {v}", " ".join(str(matrix[i][j]) for j in range(len(vertices))))


print("Đồ thị vô hướng dạng matrix:")
vertices = sorted(g.adj.keys())
mat = to_adjacency_matrix(g, vertices)
print_matrix(mat, vertices)

# ==============================
# Edge List
# ==============================

print("\n=== Edge List ===")
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3)]
print("Edge list:", edges)
print("Đây là dạng biểu diễn đơn giản nhất, dùng cho Kruskal (MST).")

# ==============================
# Các loại đồ thị đặc biệt
# ==============================

print("\n=== Các loại đồ thị đặc biệt ===")

def is_connected(graph):
    """Kiểm tra đồ thị liên thông"""
    if not graph.adj:
        return True
    start = next(iter(graph.adj))
    visited = set()
    q = deque([start])
    visited.add(start)
    while q:
        u = q.popleft()
        for v in graph.get_neighbors(u):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return len(visited) == graph.num_vertices()

print("Đồ thị g liên thông?", is_connected(g))

# Tree detection: connected + n-1 edges
print("g là cây?", is_connected(g) and g.num_edges() == g.num_vertices() - 1)

# Complete graph: n(n-1)/2 edges
n = g.num_vertices()
print(f"g là đồ thị đầy đủ K{n}?", g.num_edges() == n * (n - 1) // 2)

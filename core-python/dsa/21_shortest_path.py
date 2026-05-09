# ============================================
# 21. SHORTEST PATH - ĐƯỜNG ĐI NGẮN NHẤT / SHORTEST PATH
# ============================================
# Dijkstra: đồ thị trọng số không âm, O((V+E) log V).
# Bellman-Ford: có thể có trọng số âm, phát hiện chu trình âm, O(VE).
# Floyd-Warshall: tất cả cặp đỉnh, O(V^3).

import heapq
from collections import defaultdict


class WeightedGraph:
    """Đồ thị có hướng có trọng số"""
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        if v not in self.adj:
            self.adj[v] = []

    def get_vertices(self):
        return list(self.adj.keys())


# ==============================
# DIJKSTRA - O((V+E) log V)
# ==============================

def dijkstra(graph, start):
    """Dijkstra - đường đi ngắn nhất từ start đến mọi đỉnh
    Yêu cầu: tất cả trọng số KHÔNG ÂM."""
    dist = {v: float('inf') for v in graph.adj}
    dist[start] = 0
    prev = {v: None for v in graph.adj}
    pq = [(0, start)]  # (distance, vertex)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:  # Bỏ qua entry cũ
            continue
        for v, w in graph.adj[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev


def reconstruct_path(prev, target):
    """Tái tạo đường đi từ mảng prev của Dijkstra/Bellman-Ford"""
    if prev.get(target) is None:  # prev[target] là None khi target == start
        return [target] if target in prev else []
    path = []
    cur = target
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    return path[::-1]


# ==============================
# BELLMAN-FORD - O(VE)
# ==============================

def bellman_ford(graph, start):
    """Bellman-Ford - xử lý được trọng số âm, phát hiện negative cycle"""
    vertices = list(graph.adj.keys())
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    prev = {v: None for v in vertices}

    # Relax V-1 lần
    for _ in range(len(vertices) - 1):
        updated = False
        for u in vertices:
            if dist[u] == float('inf'):
                continue
            for v, w in graph.adj[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    prev[v] = u
                    updated = True
        if not updated:  # Early stop nếu không còn relax được
            break

    # Kiểm tra negative cycle (thêm 1 lần relax nữa)
    has_negative_cycle = False
    for u in vertices:
        if dist[u] == float('inf'):
            continue
        for v, w in graph.adj[u]:
            if dist[u] + w < dist[v]:
                has_negative_cycle = True
                break

    return dist, prev, has_negative_cycle


# ==============================
# FLOYD-WARSHALL - O(V^3)
# ==============================

def floyd_warshall(graph):
    """Floyd-Warshall - đường đi ngắn nhất giữa MỌI cặp đỉnh"""
    vertices = sorted(graph.adj.keys())
    n = len(vertices)
    idx = {v: i for i, v in enumerate(vertices)}

    # Khởi tạo ma trận khoảng cách
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0

    for u in graph.adj:
        for v, w in graph.adj[u]:
            dist[idx[u]][idx[v]] = w

    # DP: thêm từng đỉnh k làm trung gian
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist, vertices, idx


# ==============================
# Demo
# ==============================

print("=== Đồ thị mẫu (có hướng, không âm) ===")
#     (0)--4-->(1)
#     | \      |
#    1|  \2   3|
#     v   \    v
#    (2)--5-->(3)
#     |        |
#    6|       1|
#     v        v
#    (4)<--2--(5)

g = WeightedGraph()
g.add_edge(0, 1, 4)
g.add_edge(0, 2, 1)
g.add_edge(0, 3, 2)
g.add_edge(1, 3, 3)
g.add_edge(2, 3, 5)
g.add_edge(2, 4, 6)
g.add_edge(3, 5, 1)
g.add_edge(5, 4, 2)

print("\n--- Dijkstra ---")
dist_d, prev_d = dijkstra(g, 0)
print("Khoảng cách từ 0:", {v: dist_d[v] for v in sorted(dist_d)})
for v in sorted(g.adj.keys()):
    path = reconstruct_path(prev_d, v)
    print(f"  Path 0 -> {v}: {path} (dist={dist_d[v]})")

print("\n--- Bellman-Ford ---")
dist_bf, prev_bf, neg_cycle = bellman_ford(g, 0)
print("Khoảng cách từ 0:", {v: dist_bf[v] for v in sorted(dist_bf)})
print("Negative cycle?:", neg_cycle)

# Test Bellman-Ford với trọng số âm (không có negative cycle)
print("\n--- Bellman-Ford với trọng số âm ---")
g_neg = WeightedGraph()
g_neg.add_edge(0, 1, 4)
g_neg.add_edge(0, 2, 5)
g_neg.add_edge(1, 2, -3)  # Trọng số âm
g_neg.add_edge(2, 3, 4)
g_neg.add_edge(1, 3, 2)
dist_n, prev_n, nc = bellman_ford(g_neg, 0)
print("Khoảng cách từ 0:", {v: dist_n[v] for v in sorted(dist_n)})
for v in sorted(g_neg.adj.keys()):
    path = reconstruct_path(prev_n, v)
    print(f"  Path 0 -> {v}: {path} (dist={dist_n[v]})")

# Test negative cycle
print("\n--- Bellman-Ford: Negative Cycle ---")
g_nc = WeightedGraph()
g_nc.add_edge(0, 1, 1)
g_nc.add_edge(1, 2, -1)
g_nc.add_edge(2, 3, -1)
g_nc.add_edge(3, 1, -1)  # Tạo chu trình âm: 1->2->3->1 = -3
_, _, nc = bellman_ford(g_nc, 0)
print("Có negative cycle?:", nc)

print("\n--- Floyd-Warshall (All Pairs) ---")
g_fw = WeightedGraph()
g_fw.add_edge(0, 1, 4)
g_fw.add_edge(0, 2, 1)
g_fw.add_edge(1, 3, 3)
g_fw.add_edge(2, 1, 2)
g_fw.add_edge(2, 3, 5)
dist_fw, vertices, idx = floyd_warshall(g_fw)
print("Ma trận khoảng cách:")
print(f"    ", " ".join(f"{v:>3}" for v in vertices))
for i, v in enumerate(vertices):
    row = [f"{dist_fw[i][j]:3.0f}" if dist_fw[i][j] != float('inf') else " INF" for j in range(len(vertices))]
    print(f"  {v} ", " ".join(row))

# ==============================
# So sánh
# ==============================

print("\n=== So sánh thuật toán Shortest Path ===")
print("""
Thuật toán        | Time         | Space  | Trọng số âm | All Pairs
-------------------|--------------|--------|-------------|----------
BFS (unweighted)   | O(V+E)       | O(V)   | N/A         | No
Dijkstra           | O((V+E)logV) | O(V)   | Không       | No
Bellman-Ford       | O(VE)        | O(V)   | Có (cảnh báo)| No
Floyd-Warshall     | O(V^3)       | O(V^2) | Có (không NC)| Yes
A*                 | O(E) avg     | O(V)   | Không (cần  | No
                   |              |        | heuristic)  |
""")

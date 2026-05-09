# ============================================
# 20. GRAPH TRAVERSAL - DUYỆT ĐỒ THỊ / GRAPH TRAVERSAL
# ============================================
# BFS: Duyệt theo chiều rộng (queue) - O(V+E).
# DFS: Duyệt theo chiều sâu (stack/recursion) - O(V+E).

from collections import deque, defaultdict


class Graph:
    """Đồ thị có hướng dùng adjacency list"""
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        if v not in self.adj:
            self.adj[v] = []


class UndirectedGraph:
    """Đồ thị vô hướng dùng adjacency list"""
    def __init__(self):
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)


# ==============================
# BFS - DUYỆT CHIỀU RỘNG
# ==============================

def bfs(graph, start):
    """BFS - duyệt đồ thị, trả về thứ tự duyệt"""
    visited = set()
    order = []
    q = deque([start])
    visited.add(start)
    while q:
        u = q.popleft()
        order.append(u)
        for v in graph.adj.get(u, []):
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order


def bfs_shortest_path(graph, start, target):
    """BFS tìm đường đi ngắn nhất trong đồ thị không trọng số"""
    if start == target:
        return [start], 0
    visited = {start}
    q = deque([(start, [start])])
    while q:
        u, path = q.popleft()
        for v in graph.adj.get(u, []):
            if v == target:
                return path + [v], len(path)
            if v not in visited:
                visited.add(v)
                q.append((v, path + [v]))
    return None, -1


def bfs_levels(graph, start):
    """BFS trả về khoảng cách từ start đến mọi đỉnh"""
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph.adj.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


# ==============================
# DFS - DUYỆT CHIỀU SÂU
# ==============================

def dfs_recursive(graph, start, visited=None, order=None):
    """DFS đệ quy"""
    if visited is None:
        visited = set()
        order = []
    visited.add(start)
    order.append(start)
    for v in graph.adj.get(start, []):
        if v not in visited:
            dfs_recursive(graph, v, visited, order)
    return order


def dfs_iterative(graph, start):
    """DFS dùng stack"""
    visited = set()
    order = []
    stack = [start]
    while stack:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            order.append(u)
            for v in reversed(graph.adj.get(u, [])):
                if v not in visited:
                    stack.append(v)
    return order


# ==============================
# CYCLE DETECTION
# ==============================

def has_cycle_directed(graph):
    """Phát hiện chu trình trong đồ thị có hướng - DFS 3 màu"""
    WHITE, GRAY, BLACK = 0, 1, 2
    color = defaultdict(int)  # Mặc định WHITE (0)

    def dfs(u):
        color[u] = GRAY
        for v in graph.adj.get(u, []):
            if color[v] == GRAY:  # Back edge -> có cycle
                return True
            if color[v] == WHITE and dfs(v):
                return True
        color[u] = BLACK
        return False

    for v in list(graph.adj.keys()):
        if color[v] == WHITE and dfs(v):
            return True
    return False


def has_cycle_undirected(graph):
    """Phát hiện chu trình trong đồ thị vô hướng"""
    visited = set()

    def dfs(u, parent):
        visited.add(u)
        for v in graph.adj.get(u, []):
            if v not in visited:
                if dfs(v, u):
                    return True
            elif v != parent:  # Tìm thấy đỉnh đã visited không phải cha
                return True
        return False

    for v in list(graph.adj.keys()):
        if v not in visited and dfs(v, -1):
            return True
    return False


# ==============================
# CONNECTED COMPONENTS
# ==============================

def connected_components(graph):
    """Đếm và liệt kê thành phần liên thông"""
    visited = set()
    components = []

    def dfs(u, comp):
        visited.add(u)
        comp.append(u)
        for v in graph.adj.get(u, []):
            if v not in visited:
                dfs(v, comp)

    for v in list(graph.adj.keys()):
        if v not in visited:
            comp = []
            dfs(v, comp)
            components.append(comp)
    return components


# ==============================
# BIPARTITE CHECK
# ==============================

def is_bipartite(graph):
    """Kiểm tra đồ thị 2 phía bằng BFS tô màu"""
    color = {}  # 0 và 1
    for start in graph.adj:
        if start not in color:
            q = deque([start])
            color[start] = 0
            while q:
                u = q.popleft()
                for v in graph.adj.get(u, []):
                    if v not in color:
                        color[v] = 1 - color[u]
                        q.append(v)
                    elif color[v] == color[u]:
                        return False  # 2 đỉnh kề cùng màu
    return True


# ==============================
# TOPOLOGICAL SORT
# ==============================

def topological_sort_kahn(graph):
    """Topo sort dùng Kahn (BFS + indegree) - O(V+E)"""
    indegree = defaultdict(int)
    for u in graph.adj:
        for v in graph.adj[u]:
            indegree[v] = indegree.get(v, 0) + 1

    q = deque([v for v in graph.adj if indegree.get(v, 0) == 0])
    result = []
    while q:
        u = q.popleft()
        result.append(u)
        for v in graph.adj.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    if len(result) != len(graph.adj):  # Có cycle
        return None
    return result


def topological_sort_dfs(graph):
    """Topo sort dùng DFS - O(V+E)"""
    visited = set()
    stack = []

    def dfs(u):
        visited.add(u)
        for v in graph.adj.get(u, []):
            if v not in visited:
                dfs(v)
        stack.append(u)

    for v in list(graph.adj.keys()):
        if v not in visited:
            dfs(v)
    return stack[::-1]


# ==============================
# Demo
# ==============================

# Xây đồ thị mẫu:
#     0 -> 1   4 -> 5
#     |  / |   |
#     v v  v   v
#     2 -> 3   6
print("=== Đồ thị mẫu (có hướng) ===")
dg = Graph()
edges = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (4, 5), (5, 6)]
for u, v in edges:
    dg.add_edge(u, v)
print("Cạnh:", edges)

print("\nBFS từ 0:", bfs(dg, 0))
print("DFS đệ quy từ 0:", dfs_recursive(dg, 0))
print("DFS vòng lặp từ 0:", dfs_iterative(dg, 0))

path, dist = bfs_shortest_path(dg, 0, 3)
print(f"\nĐường ngắn nhất 0->3: {path} (distance={dist})")
print(f"Khoảng cách BFS từ 0: {bfs_levels(dg, 0)}")

print("\n--- Cycle Detection ---")
print(f"Đồ thị có hướng có cycle? {has_cycle_directed(dg)}")
ug = UndirectedGraph()
for u, v in [(0, 1), (0, 2), (1, 2), (1, 3)]:
    ug.add_edge(u, v)
print(f"Đồ thị vô hướng (0-1-2-3) có cycle? {has_cycle_undirected(ug)}")

print("\n--- Connected Components ---")
ug2 = UndirectedGraph()
ug2.add_edge(0, 1)
ug2.add_edge(1, 2)
ug2.add_edge(3, 4)
ug2.adj[5] = []  # Đỉnh cô lập
comps = connected_components(ug2)
print(f"Components ({len(comps)}): {comps}")

print("\n--- Bipartite Check ---")
ug3 = UndirectedGraph()
for u, v in [(0, 1), (0, 3), (1, 2), (2, 3)]:  # Chu trình chẵn -> bipartite
    ug3.add_edge(u, v)
print(f"Graph 0-1-2-3-0 (even cycle): bipartite? {is_bipartite(ug3)}")
ug4 = UndirectedGraph()
for u, v in [(0, 1), (1, 2), (2, 0)]:  # Chu trình lẻ -> không bipartite
    ug4.add_edge(u, v)
print(f"Graph 0-1-2-0 (odd cycle): bipartite? {is_bipartite(ug4)}")

print("\n--- Topological Sort ---")
dag = Graph()
dag_edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 0), (4, 5)]
for u, v in dag_edges:
    dag.add_edge(u, v)
print(f"DAG edges: {dag_edges}")
print(f"Topo (Kahn): {topological_sort_kahn(dag)}")
print(f"Topo (DFS):  {topological_sort_dfs(dag)}")

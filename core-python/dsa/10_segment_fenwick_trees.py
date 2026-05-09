# ============================================
# 10. SEGMENT & FENWICK TREES - CÂY PHÂN ĐOẠN & CÂY FENWICK
# ============================================
# Segment Tree: cây cho range queries (sum/min/max) + point/range updates.
# Fenwick Tree (BIT): mảng prefix sum có thể update, code ngắn gọn hơn Segment Tree.


# ==============================
# SEGMENT TREE (Range Sum)
# ==============================

class SegmentTree:
    """Cây phân đoạn cho range sum query + point update"""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # Mảng lưu cây, size 4n là đủ
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, left, right):
        """Xây cây - O(n)"""
        if left == right:
            self.tree[node] = arr[left]
            return
        mid = (left + right) // 2
        self._build(arr, node * 2 + 1, left, mid)       # Con trái
        self._build(arr, node * 2 + 2, mid + 1, right)  # Con phải
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def query(self, ql, qr):
        """Tổng arr[ql..qr] - O(log n)"""
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, node, left, right, ql, qr):
        # Ngoài phạm vi
        if ql > right or qr < left:
            return 0
        # Nằm hoàn toàn trong phạm vi
        if ql <= left and right <= qr:
            return self.tree[node]
        # Giao một phần
        mid = (left + right) // 2
        left_sum = self._query(node * 2 + 1, left, mid, ql, qr)
        right_sum = self._query(node * 2 + 2, mid + 1, right, ql, qr)
        return left_sum + right_sum

    def update(self, idx, val):
        """Cập nhật arr[idx] = val - O(log n)"""
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, left, right, idx, val):
        if left == right:
            self.tree[node] = val
            return
        mid = (left + right) // 2
        if idx <= mid:
            self._update(node * 2 + 1, left, mid, idx, val)
        else:
            self._update(node * 2 + 2, mid + 1, right, idx, val)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]


# ==============================
# SEGMENT TREE + LAZY PROPAGATION (Range Update)
# ==============================

class LazySegmentTree:
    """Segment tree với lazy propagation cho range update"""

    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Mảng lazy
        self._build(arr, 0, 0, self.n - 1)

    def _build(self, arr, node, left, right):
        if left == right:
            self.tree[node] = arr[left]
            return
        mid = (left + right) // 2
        self._build(arr, node * 2 + 1, left, mid)
        self._build(arr, node * 2 + 2, mid + 1, right)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def _push(self, node, left, right):
        """Đẩy lazy value xuống con"""
        if self.lazy[node] != 0:
            self.tree[node] += (right - left + 1) * self.lazy[node]
            if left != right:  # Không phải lá
                self.lazy[node * 2 + 1] += self.lazy[node]
                self.lazy[node * 2 + 2] += self.lazy[node]
            self.lazy[node] = 0

    def range_update(self, ql, qr, delta):
        """Tăng arr[ql..qr] thêm delta - O(log n)"""
        self._range_update(0, 0, self.n - 1, ql, qr, delta)

    def _range_update(self, node, left, right, ql, qr, delta):
        self._push(node, left, right)
        if ql > right or qr < left:
            return
        if ql <= left and right <= qr:
            self.lazy[node] += delta
            self._push(node, left, right)
            return
        mid = (left + right) // 2
        self._range_update(node * 2 + 1, left, mid, ql, qr, delta)
        self._range_update(node * 2 + 2, mid + 1, right, ql, qr, delta)
        self.tree[node] = self.tree[node * 2 + 1] + self.tree[node * 2 + 2]

    def query(self, ql, qr):
        """Tổng arr[ql..qr] sau các range update - O(log n)"""
        return self._query(0, 0, self.n - 1, ql, qr)

    def _query(self, node, left, right, ql, qr):
        self._push(node, left, right)
        if ql > right or qr < left:
            return 0
        if ql <= left and right <= qr:
            return self.tree[node]
        mid = (left + right) // 2
        return (self._query(node * 2 + 1, left, mid, ql, qr) +
                self._query(node * 2 + 2, mid + 1, right, ql, qr))


# ==============================
# FENWICK TREE (Binary Indexed Tree)
# ==============================

class FenwickTree:
    """Cây BIT cho prefix sum - code ngắn hơn Segment Tree"""

    def __init__(self, arr):
        """Xây BIT - O(n log n) hoặc O(n)"""
        self.n = len(arr)
        self.bit = [0] * (self.n + 1)
        for i, val in enumerate(arr):
            self.add(i, val)

    def add(self, idx, delta):
        """Cập nhật arr[idx] += delta - O(log n)"""
        i = idx + 1  # BIT dùng 1-indexed
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i  # i + LSB(i)

    def prefix_sum(self, idx):
        """Tổng arr[0..idx] - O(log n)"""
        if idx < 0:
            return 0
        result = 0
        i = min(idx + 1, self.n)
        while i > 0:
            result += self.bit[i]
            i -= i & -i  # i - LSB(i)
        return result

    def range_sum(self, left, right):
        """Tổng arr[left..right] - O(log n)"""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

    def get(self, idx):
        """Lấy giá trị tại idx"""
        return self.range_sum(idx, idx)


# ==============================
# Demo
# ==============================
print("=== Segment Tree (range sum + point update) ===")
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)
print("arr:", arr)
print("Sum arr[1..4] (3+5+7+9):", st.query(1, 4))
print("Sum arr[0..2] (1+3+5):", st.query(0, 2))

st.update(2, 10)  # arr[2] = 10
print("Sau update(2, 10):")
print("Sum arr[0..2] (1+3+10):", st.query(0, 2))
print("Sum arr[0..5] (toàn bộ):", st.query(0, 5))

# --- Lazy Segment Tree ---
print("\n=== Segment Tree + Lazy Propagation (range update) ===")
arr2 = [1, 2, 3, 4, 5]
lst = LazySegmentTree(arr2)
print("arr:", arr2)
print("Sum arr[0..4]:", lst.query(0, 4))

lst.range_update(1, 3, 10)  # arr[1..3] += 10 -> [1, 12, 13, 14, 5]
print("Sau range_update(1, 3, +10):")
print("Sum arr[0..4]:", lst.query(0, 4))
print("Sum arr[1..3]:", lst.query(1, 3))  # 12+13+14 = 39
print("Sum arr[0..0]:", lst.query(0, 0))  # 1
print("Sum arr[4..4]:", lst.query(4, 4))  # 5

# --- Fenwick Tree ---
print("\n=== Fenwick Tree (BIT) ===")
arr3 = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit = FenwickTree(arr3)
print("arr:", arr3)
print("Prefix sum arr[0..4]:", bit.prefix_sum(4))  # 2+1+1+3+2 = 9
print("Range sum arr[3..7]:", bit.range_sum(3, 7)) # 3+2+3+4+5 = 17
print("Get arr[5]:", bit.get(5))

bit.add(3, 100)  # arr[3] += 100
print("Sau add(3, +100) -> arr[3] = 103:")
print("Prefix sum arr[0..4]:", bit.prefix_sum(4))  # +100
print("Get arr[3]:", bit.get(3))

# So sánh naive range sum vs BIT
print("\n--- So sánh hiệu năng ---")
import time

def naive_range_sum(arr, l, r):
    return sum(arr[l:r+1])

large_arr = list(range(50000))
bit_large = FenwickTree(large_arr)

# Naive query
start = time.perf_counter()
for _ in range(100):
    naive_range_sum(large_arr, 100, 40000)
naive_time = time.perf_counter() - start

# BIT query
start = time.perf_counter()
for _ in range(100):
    bit_large.range_sum(100, 40000)
bit_time = time.perf_counter() - start

print(f"Naive range sum (100 queries): {naive_time:.4f}s")
print(f"BIT range sum   (100 queries): {bit_time:.4f}s")

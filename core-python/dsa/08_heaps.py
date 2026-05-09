# ============================================
# 8. HEAPS - ĐỐNG / HEAPS
# ============================================
# Heap = cây nhị phân hoàn chỉnh (CBT) thỏa tính chất heap:
#   Min-Heap: parent <= children (gốc nhỏ nhất)
#   Max-Heap: parent >= children (gốc lớn nhất)
# Biểu diễn bằng mảng: con của i là 2i+1, 2i+2; cha là (i-1)//2.

import heapq

# ==============================
# MIN-HEAP TỰ CÀI
# ==============================

class MinHeap:
    """Min-Heap cài bằng list"""

    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def peek(self):
        """Xem giá trị nhỏ nhất - O(1)"""
        return self.heap[0] if self.heap else None

    def insert(self, val):
        """Chèn giá trị - O(log n)"""
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        """Đưa phần tử tại i lên đúng vị trí"""
        while i > 0:
            p = self.parent(i)
            if self.heap[i] < self.heap[p]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def extract_min(self):
        """Lấy và xóa giá trị nhỏ nhất - O(log n)"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Đưa phần tử cuối lên gốc
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        """Đưa phần tử tại i xuống đúng vị trí"""
        size = len(self.heap)
        while True:
            smallest = i
            left = self.left_child(i)
            right = self.right_child(i)
            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def build_heap(self, arr):
        """Xây heap từ mảng - O(n) dùng Floyd's method"""
        self.heap = arr[:]
        # Heapify từ dưới lên, bỏ qua lá
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def size(self):
        return len(self.heap)


print("=== MinHeap tự cài ===")
mh = MinHeap()
for v in [5, 3, 8, 1, 4, 7]:
    mh.insert(v)
print("Sau insert 5,3,8,1,4,7:", mh.heap)
print("Peek:", mh.peek())
print("Extract min:", mh.extract_min(), "- heap:", mh.heap)
print("Extract min:", mh.extract_min(), "- heap:", mh.heap)

# Build heap từ mảng - O(n)
mh2 = MinHeap()
mh2.build_heap([9, 4, 7, 1, 2, 6, 3, 5, 8])
print("\nBuild heap từ [9,4,7,1,2,6,3,5,8]:", mh2.heap)

# ==============================
# PYTHON heapq (MIN-HEAP)
# ==============================

print("\n=== Python heapq (Min-Heap) ===")
data = [5, 3, 8, 1, 4, 7]
heapq.heapify(data)  # O(n) - biến list thành heap
print("Sau heapify:", data)

heapq.heappush(data, 2)  # O(log n)
print("Sau heappush(2):", data)

print("heappop:", heapq.heappop(data), data)  # O(log n)
print("heappop:", heapq.heappop(data), data)

# nlargest / nsmallest
nums = [3, 7, 2, 9, 1, 5, 8, 4, 6]
print("\nnlargest(3):", heapq.nlargest(3, nums))
print("nsmallest(3):", heapq.nsmallest(3, nums))

# ==============================
# MAX-HEAP (dùng heap âm)
# ==============================

print("\n=== Max-Heap (dùng số âm) ===")
max_heap = []
for v in [5, 3, 8, 1, 4]:
    heapq.heappush(max_heap, -v)
print("Max-heap (giá trị âm):", max_heap)
print("Extract max:", -heapq.heappop(max_heap))
print("Extract max:", -heapq.heappop(max_heap))

# Max-Heap class
class MaxHeap:
    """Max-Heap wrapper dùng heapq với giá trị âm"""

    def __init__(self):
        self.heap = []

    def push(self, val):
        heapq.heappush(self.heap, -val)

    def pop(self):
        return -heapq.heappop(self.heap)

    def peek(self):
        return -self.heap[0] if self.heap else None

    def size(self):
        return len(self.heap)


print("\nMaxHeap class:")
mx = MaxHeap()
for v in [5, 3, 8, 1, 4]:
    mx.push(v)
print("Peek:", mx.peek())
print("Pop:", mx.pop(), "- Pop:", mx.pop())

# ==============================
# HEAP SORT
# ==============================

def heap_sort(arr):
    """Sắp xếp bằng heap - O(n log n)"""
    heapq.heapify(arr)  # O(n)
    return [heapq.heappop(arr) for _ in range(len(arr))]

print("\n=== Heap Sort ===")
unsorted = [7, 3, 9, 2, 8, 1, 5, 4]
sorted_arr = heap_sort(unsorted[:])
print("Unsorted:", unsorted)
print("Heap sort:", sorted_arr)

# ==============================
# PRIORITY QUEUE
# ==============================

print("\n=== Priority Queue ===")
# heapq hỗ trợ tuple: (priority, item)
pq = []
tasks = [(3, "Task C - thấp"), (1, "Task A - cao"), (2, "Task B - trung bình")]
for priority, task in tasks:
    heapq.heappush(pq, (priority, task))

print("Xử lý theo priority:")
while pq:
    priority, task = heapq.heappop(pq)
    print(f"  Priority {priority}: {task}")

# Priority Queue class tổng quát
from dataclasses import dataclass, field

@dataclass(order=True)
class PrioritizedItem:
    priority: int
    item: str = field(compare=False)


print("\nPriority Queue với dataclass:")
pq2 = []
heapq.heappush(pq2, PrioritizedItem(2, "Process B"))
heapq.heappush(pq2, PrioritizedItem(1, "Process A"))
heapq.heappush(pq2, PrioritizedItem(3, "Process C"))
while pq2:
    pi = heapq.heappop(pq2)
    print(f"  Priority {pi.priority}: {pi.item}")

# --- Kth Largest / Smallest ---
print("\n--- Kth Largest/Smallest ---")
def kth_largest(arr, k):
    """Tìm phần tử lớn thứ k - O(n log k)"""
    return heapq.nlargest(k, arr)[-1]

def kth_smallest(arr, k):
    """Tìm phần tử nhỏ thứ k - O(n log k)"""
    return heapq.nsmallest(k, arr)[-1]

arr = [7, 10, 4, 3, 20, 15]
print(f"arr = {arr}")
print(f"Kth smallest (k=3): {kth_smallest(arr, 3)}")
print(f"Kth largest  (k=2): {kth_largest(arr, 2)}")

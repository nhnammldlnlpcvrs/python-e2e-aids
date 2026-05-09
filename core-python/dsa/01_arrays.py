# ============================================
# 1. ARRAYS - MẢNG / ARRAYS
# ============================================
# Array = tập hợp các phần tử cùng kiểu, lưu liên tiếp trong bộ nhớ.
# Python list chính là dynamic array: tự resize khi cần.

# --- Tạo và truy cập mảng ---
arr = [10, 20, 30, 40, 50]
print("Mảng ban đầu:", arr)
print("arr[0] =", arr[0])       # Phần tử đầu
print("arr[-1] =", arr[-1])     # Phần tử cuối
print("len(arr) =", len(arr))   # Kích thước

# --- Duyệt mảng ---
print("\nDuyệt theo index:")
for i in range(len(arr)):
    print(f"  arr[{i}] = {arr[i]}")

print("Duyệt theo giá trị:")
for val in arr:
    print(f"  {val}", end=" ")
print()

# --- Slicing ---
print("\nSlicing:")
print("arr[1:4] =", arr[1:4])   # [20, 30, 40]
print("arr[:3] =", arr[:3])     # 3 phần tử đầu
print("arr[2:] =", arr[2:])     # Từ index 2 đến cuối
print("arr[::-1] =", arr[::-1]) # Đảo ngược
print("arr[::2] =", arr[::2])   # Nhảy bước 2

# --- Các thao tác cơ bản ---
arr.append(60)                   # Thêm cuối - O(1) amortized
print("\nSau append(60):", arr)

arr.insert(0, 5)                 # Chèn đầu - O(n)
print("Sau insert(0, 5):", arr)

arr.pop()                        # Xóa cuối - O(1)
print("Sau pop():", arr)

arr.pop(0)                       # Xóa đầu - O(n)
print("Sau pop(0):", arr)

arr.remove(30)                   # Xóa theo giá trị - O(n)
print("Sau remove(30):", arr)

# Tìm kiếm
idx = arr.index(40)              # O(n)
print("Index của 40:", idx)

# --- Reverse và Rotate ---
arr2 = [1, 2, 3, 4, 5]
arr2.reverse()                   # Đảo ngược tại chỗ - O(n)
print("\narr2.reverse():", arr2)

# Rotate phải k bước
def rotate_right(arr, k):
    """Xoay mảng sang phải k vị trí"""
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]

def rotate_left(arr, k):
    """Xoay mảng sang trái k vị trí"""
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

arr3 = [10, 20, 30, 40, 50]
print("\nrotate_right([10,20,30,40,50], 2):", rotate_right(arr3, 2))
print("rotate_left([10,20,30,40,50], 2):", rotate_left(arr3, 2))

# --- 2D Arrays / Ma trận ---
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMa trận 3x3:")
for row in matrix:
    print(" ", row)

def transpose(mat):
    """Chuyển vị ma trận"""
    rows, cols = len(mat), len(mat[0])
    return [[mat[r][c] for r in range(rows)] for c in range(cols)]

print("Transpose:")
for row in transpose(matrix):
    print(" ", row)

def multiply_matrices(A, B):
    """Nhân hai ma trận A (mxn) * B (nxp)"""
    m, n = len(A), len(A[0])
    p = len(B[0])
    # Khởi tạo ma trận kết quả m x p
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(n))
    return result

# Ma trận khởi tạo mxn
def create_matrix(rows, cols, default=0):
    """Tạo ma trận rows x cols"""
    return [[default] * cols for _ in range(rows)]

print("\nMatrix 3x4 (default 0):")
for row in create_matrix(3, 4):
    print(" ", row)

# --- Prefix Sum (Tổng tiền tố) ---
print("\n--- Prefix Sum ---")
def prefix_sum(arr):
    """Mảng tổng tiền tố: pre[i] = tổng arr[0...i]"""
    pre = [0] * len(arr)
    pre[0] = arr[0]
    for i in range(1, len(arr)):
        pre[i] = pre[i-1] + arr[i]
    return pre

def range_sum(pre, l, r):
    """Tổng arr[l...r] dùng prefix sum - O(1)"""
    if l == 0:
        return pre[r]
    return pre[r] - pre[l-1]

nums = [3, 1, 4, 1, 5, 9, 2, 6]
pre = prefix_sum(nums)
print("Mảng:", nums)
print("Prefix sum:", pre)
print("Tổng arr[2...5]:", range_sum(pre, 2, 5))  # 4+1+5+9 = 19

# --- Dynamic Array (tự cài đặt) ---
class DynamicArray:
    """Mảng động tự resize gấp đôi khi đầy"""

    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [None] * self.capacity

    def _resize(self, new_cap):
        """Tạo mảng mới và copy dữ liệu"""
        new_data = [None] * new_cap
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_cap

    def append(self, value):
        """Thêm cuối - O(1) amortized"""
        if self.size == self.capacity:
            self._resize(self.capacity * 2)
        self.data[self.size] = value
        self.size += 1

    def pop(self):
        """Xóa cuối - O(1)"""
        if self.size == 0:
            return None
        val = self.data[self.size - 1]
        self.size -= 1
        # Shrink nếu cần (capacity dùng dưới 1/4)
        if self.size < self.capacity // 4 and self.capacity > 2:
            self._resize(self.capacity // 2)
        return val

    def __getitem__(self, i):
        if 0 <= i < self.size:
            return self.data[i]
        raise IndexError("Index out of range")

    def __len__(self):
        return self.size

    def __repr__(self):
        return str([self.data[i] for i in range(self.size)])

print("\nDynamicArray demo:")
da = DynamicArray()
for v in [1, 2, 3, 4, 5, 6, 7]:
    da.append(v)
print(f"  Sau append 7 phần tử: {da} (capacity={da.capacity})")
print(f"  da[3] = {da[3]}")
da.pop()
da.pop()
print(f"  Sau 2 lần pop: {da} (capacity={da.capacity})")

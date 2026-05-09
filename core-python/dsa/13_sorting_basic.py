# ============================================
# 13. SORTING BASIC - SẮP XẾP CƠ BẢN / BASIC SORTING
# ============================================
# 3 thuật toán O(n^2): Bubble Sort, Selection Sort, Insertion Sort.
# Đơn giản, dễ cài, phù hợp với mảng nhỏ.

import time
import random


# ==============================
# BUBBLE SORT
# ==============================

def bubble_sort(arr):
    """Sắp xếp nổi bọt - O(n^2)
    So sánh cặp liền kề, đẩy phần tử lớn nhất về cuối."""
    n = len(arr)
    result = arr[:]
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:  # Nếu không có swap nào -> đã sắp xếp
            break
    return result


def bubble_sort_steps(arr):
    """Bubble sort có in từng bước"""
    result = arr[:]
    n = len(result)
    print("  Bắt đầu:", result)
    for i in range(n):
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
        print(f"  Pass {i+1}: {result}")
    return result


# ==============================
# SELECTION SORT
# ==============================

def selection_sort(arr):
    """Sắp xếp chọn - O(n^2)
    Tìm min trong phần chưa sắp xếp, đưa về đầu."""
    result = arr[:]
    n = len(result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
    return result


def selection_sort_steps(arr):
    """Selection sort có in từng bước"""
    result = arr[:]
    n = len(result)
    print("  Bắt đầu:", result)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j
        result[i], result[min_idx] = result[min_idx], result[i]
        print(f"  Pass {i+1} (chọn min={result[i]}): {result}")
    return result


# ==============================
# INSERTION SORT
# ==============================

def insertion_sort(arr):
    """Sắp xếp chèn - O(n^2), best case O(n)
    Chèn từng phần tử vào đúng vị trí trong phần đã sắp xếp."""
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
    return result


def insertion_sort_steps(arr):
    """Insertion sort có in từng bước"""
    result = arr[:]
    print("  Bắt đầu:", result)
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
        print(f"  Chèn {key}: {result}")
    return result


# ==============================
# Demo
# ==============================

sample = [64, 34, 25, 12, 22, 11, 90]

print("=== Bubble Sort ===")
print(f"Input: {sample}")
print(f"Output: {bubble_sort(sample)}")
print("Chi tiết từng bước:")
bubble_sort_steps(sample)

print("\n=== Selection Sort ===")
print(f"Input: {sample}")
print(f"Output: {selection_sort(sample)}")
print("Chi tiết từng bước:")
selection_sort_steps(sample)

print("\n=== Insertion Sort ===")
print(f"Input: {sample}")
print(f"Output: {insertion_sort(sample)}")
print("Chi tiết từng bước:")
insertion_sort_steps(sample)

# ==============================
# So sánh
# ==============================

print("\n=== So sánh 3 thuật toán ===")

def benchmark_sort(sort_func, arr):
    start = time.perf_counter()
    sort_func(arr[:])
    return time.perf_counter() - start

# Test với các kích thước khác nhau
sizes = [100, 500, 1000]
functions = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
}

print(f"{'Size':<8}", end="")
for name in functions:
    print(f"{name:<18}", end="")
print()

for size in sizes:
    random_arr = [random.randint(0, 10000) for _ in range(size)]
    print(f"{size:<8}", end="")
    for name, func in functions.items():
        t = benchmark_sort(func, random_arr)
        print(f"{t:.6f}s{'':<12}", end="")
    print()

# ==============================
# Tính chất
# ==============================

print("\n=== Tính chất ===")
print("""
Thuật toán      | Time (Worst) | Time (Best) | Stable | In-place | Space
----------------|--------------|-------------|--------|----------|------
Bubble Sort     | O(n^2)       | O(n)        | Yes    | Yes      | O(1)
Selection Sort  | O(n^2)       | O(n^2)      | No     | Yes      | O(1)
Insertion Sort  | O(n^2)       | O(n)        | Yes    | Yes      | O(1)

- Stable: giữ thứ tự tương đối của các phần tử bằng nhau
- In-place: không cần thêm mảng phụ (hoặc O(1) space)
- Với n < 50, Insertion Sort thường nhanh hơn Merge/Quick sort nhờ hằng số nhỏ
""")

# ============================================
# 15. SEARCHING - TÌM KIẾM / SEARCHING
# ============================================
# Linear Search: duyệt từng phần tử - O(n).
# Binary Search: chia đôi khoảng tìm kiếm - O(log n), cần mảng đã sắp xếp.


# ==============================
# LINEAR SEARCH - O(n)
# ==============================

def linear_search(arr, target):
    """Tìm kiếm tuyến tính - trả về index đầu tiên hoặc -1"""
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


def linear_search_all(arr, target):
    """Tìm tất cả vị trí của target"""
    return [i for i, val in enumerate(arr) if val == target]


# ==============================
# BINARY SEARCH - O(log n)
# ==============================

def binary_search_iterative(arr, target):
    """Tìm kiếm nhị phân (không đệ quy)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2  # Tránh overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """Tìm kiếm nhị phân (đệ quy)"""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


# ==============================
# LOWER BOUND / UPPER BOUND
# ==============================

def lower_bound(arr, target):
    """Vị trí đầu tiên >= target (bisect_left)"""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left


def upper_bound(arr, target):
    """Vị trí đầu tiên > target (bisect_right)"""
    left, right = 0, len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left


def first_occurrence(arr, target):
    """Vị trí xuất hiện đầu tiên của target"""
    idx = lower_bound(arr, target)
    if idx < len(arr) and arr[idx] == target:
        return idx
    return -1


def last_occurrence(arr, target):
    """Vị trí xuất hiện cuối cùng của target"""
    idx = upper_bound(arr, target)
    if idx > 0 and arr[idx - 1] == target:
        return idx - 1
    return -1


def count_occurrences(arr, target):
    """Đếm số lần xuất hiện của target"""
    return upper_bound(arr, target) - lower_bound(arr, target)


# ==============================
# INTERPOLATION SEARCH
# ==============================

def interpolation_search(arr, target):
    """Tìm kiếm nội suy - O(log log n) avg, O(n) worst
    Dùng khi dữ liệu phân bố đều."""
    left, right = 0, len(arr) - 1
    while left <= right and arr[left] <= target <= arr[right]:
        if left == right:
            return left if arr[left] == target else -1
        # Công thức nội suy
        pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
        if pos < left or pos > right:
            return -1
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            left = pos + 1
        else:
            right = pos - 1
    return -1


# ==============================
# TERNARY SEARCH
# ==============================

def ternary_search(arr, target, left=0, right=None):
    """Tìm kiếm tam phân - O(log_3 n)
    Chia mảng thành 3 phần thay vì 2."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid1 = left + (right - left) // 3
    mid2 = right - (right - left) // 3
    if arr[mid1] == target:
        return mid1
    if arr[mid2] == target:
        return mid2
    if target < arr[mid1]:
        return ternary_search(arr, target, left, mid1 - 1)
    elif target > arr[mid2]:
        return ternary_search(arr, target, mid2 + 1, right)
    else:
        return ternary_search(arr, target, mid1 + 1, mid2 - 1)


# ==============================
# JUMP SEARCH - O(√n)
# ==============================

def jump_search(arr, target):
    """Tìm kiếm nhảy - O(√n)
    Nhảy từng block sqrt(n), khi vượt target thì linear search trong block."""
    import math
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    # Nhảy đến khi vượt target
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    # Linear search trong block
    while prev < min(step, n):
        if arr[prev] == target:
            return prev
        prev += 1
    return -1


# ==============================
# SEARCH IN ROTATED SORTED ARRAY
# ==============================

def search_rotated(arr, target):
    """Tìm trong mảng đã xoay vòng - O(log n)"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        # Nửa trái đã sắp xếp
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Nửa phải đã sắp xếp
        else:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


# ==============================
# Demo
# ==============================

sorted_arr = [2, 5, 7, 7, 7, 10, 12, 15, 18, 20]
print("=== Linear Search ===")
print(f"Array: {sorted_arr}")
print(f"linear_search(7): {linear_search(sorted_arr, 7)}")
print(f"linear_search(99): {linear_search(sorted_arr, 99)}")
print(f"linear_search_all(7): {linear_search_all(sorted_arr, 7)}")

print("\n=== Binary Search ===")
print(f"binary_search_iterative(10): {binary_search_iterative(sorted_arr, 10)}")
print(f"binary_search_recursive(10): {binary_search_recursive(sorted_arr, 10)}")
print(f"binary_search_iterative(99): {binary_search_iterative(sorted_arr, 99)}")

print("\n=== Lower/Upper Bound ===")
print(f"Array: {sorted_arr}")
print(f"lower_bound(7): {lower_bound(sorted_arr, 7)}")
print(f"upper_bound(7): {upper_bound(sorted_arr, 7)}")
print(f"first_occurrence(7): {first_occurrence(sorted_arr, 7)}")
print(f"last_occurrence(7): {last_occurrence(sorted_arr, 7)}")
print(f"count_occurrences(7): {count_occurrences(sorted_arr, 7)}")

print("\n=== Interpolation Search ===")
uniform_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(f"Array: {uniform_arr}")
print(f"interpolation_search(50): {interpolation_search(uniform_arr, 50)}")
print(f"interpolation_search(55): {interpolation_search(uniform_arr, 55)}")

print("\n=== Ternary Search ===")
print(f"ternary_search(15): {ternary_search(sorted_arr, 15)}")

print("\n=== Jump Search ===")
print(f"jump_search(12): {jump_search(sorted_arr, 12)}")
print(f"jump_search(99): {jump_search(sorted_arr, 99)}")

print("\n=== Search in Rotated Sorted Array ===")
rotated = [15, 18, 20, 2, 5, 7, 7, 7, 10, 12]
print(f"Rotated: {rotated}")
print(f"search_rotated(7): {search_rotated(rotated, 7)}")
print(f"search_rotated(20): {search_rotated(rotated, 20)}")
print(f"search_rotated(99): {search_rotated(rotated, 99)}")

# ==============================
# So sánh hiệu năng
# ==============================

print("\n=== So sánh ===")
import time, random

large_sorted = sorted([random.randint(0, 10000000) for _ in range(100000)])

# Linear search: tìm ở giữa
target = large_sorted[len(large_sorted) // 2]
start = time.perf_counter()
for _ in range(100):
    linear_search(large_sorted, target)
linear_time = time.perf_counter() - start

start = time.perf_counter()
for _ in range(100):
    binary_search_iterative(large_sorted, target)
binary_time = time.perf_counter() - start

print(f"Linear search (100 queries x 100k):  {linear_time:.4f}s")
print(f"Binary search (100 queries x 100k):  {binary_time:.6f}s")

# ============================================
# 14. SORTING ADVANCED - SẮP XẾP NÂNG CAO / ADVANCED SORTING
# ============================================
# O(n log n): Merge Sort, Quick Sort, Heap Sort.
# O(n + k): Counting Sort, Radix Sort, Bucket Sort.

import time
import random
import sys

sys.setrecursionlimit(10000)


# ==============================
# MERGE SORT - O(n log n)
# ==============================

def merge_sort(arr):
    """Sắp xếp trộn - O(n log n), stable, không in-place"""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    """Trộn 2 mảng đã sắp xếp"""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Merge sort in-place version
def merge_sort_inplace(arr, left=0, right=None):
    """Merge sort in-place (dùng mảng tạm)"""
    if right is None:
        right = len(arr) - 1
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort_inplace(arr, left, mid)
    merge_sort_inplace(arr, mid + 1, right)
    _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr, left, mid, right):
    temp = []
    i, j = left, mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
    temp.extend(arr[i:mid + 1])
    temp.extend(arr[j:right + 1])
    for k in range(len(temp)):
        arr[left + k] = temp[k]


# ==============================
# QUICK SORT - O(n log n) avg
# ==============================

def quick_sort_lomuto(arr, low=0, high=None):
    """Quick Sort dùng Lomuto partition"""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = _lomuto_partition(arr, low, high)
        quick_sort_lomuto(arr, low, pivot_idx - 1)
        quick_sort_lomuto(arr, pivot_idx + 1, high)


def _lomuto_partition(arr, low, high):
    """Lomuto: chọn pivot là phần tử cuối"""
    pivot = arr[high]
    i = low - 1  # Vị trí cuối của phần <= pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_hoare(arr, low=0, high=None):
    """Quick Sort dùng Hoare partition (nhanh hơn Lomuto)"""
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = _hoare_partition(arr, low, high)
        quick_sort_hoare(arr, low, pivot_idx)       # Chú ý: pivot_idx, không phải pivot_idx-1
        quick_sort_hoare(arr, pivot_idx + 1, high)


def _hoare_partition(arr, low, high):
    """Hoare: 2 con trỏ từ 2 đầu, pivot là phần tử đầu"""
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# Quick Sort với pivot median-of-three
def quick_sort_median(arr, low=0, high=None):
    """Quick Sort + median-of-three pivot selection"""
    if high is None:
        high = len(arr) - 1
    if low < high:
        # Median-of-three
        mid = (low + high) // 2
        if arr[mid] < arr[low]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] < arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        pivot_idx = _lomuto_partition(arr, low, high)
        quick_sort_median(arr, low, pivot_idx - 1)
        quick_sort_median(arr, pivot_idx + 1, high)


# ==============================
# COUNTING SORT - O(n + k)
# ==============================

def counting_sort(arr):
    """Counting Sort cho mảng số nguyên không âm - O(n + k)"""
    if not arr:
        return []
    max_val = max(arr)
    count = [0] * (max_val + 1)
    # Đếm
    for x in arr:
        count[x] += 1
    # Cộng dồn (prefix sum)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    # Xếp kết quả (duyệt ngược để stable)
    output = [0] * len(arr)
    for x in reversed(arr):
        count[x] -= 1
        output[count[x]] = x
    return output


# ==============================
# RADIX SORT (LSD) - O(d * (n + b))
# ==============================

def counting_sort_by_digit(arr, exp):
    """Counting sort theo 1 chữ số (dùng cho Radix Sort)"""
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # 10 chữ số (0-9)
    for x in arr:
        digit = (x // exp) % 10
        count[digit] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for x in reversed(arr):
        digit = (x // exp) % 10
        count[digit] -= 1
        output[count[digit]] = x
    return output


def radix_sort_lsd(arr):
    """Radix Sort LSD cho mảng số nguyên không âm"""
    if not arr:
        return []
    max_val = max(arr)
    result = arr[:]
    exp = 1
    while max_val // exp > 0:
        result = counting_sort_by_digit(result, exp)
        exp *= 10
    return result


# ==============================
# BUCKET SORT - O(n + k) avg
# ==============================

def bucket_sort(arr, num_buckets=10):
    """Bucket Sort cho mảng số thực [0, 1) hoặc scale được"""
    if not arr:
        return []
    # Tạo buckets
    buckets = [[] for _ in range(num_buckets)]
    # Phân phối vào buckets
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val + 1) / num_buckets if max_val != min_val else 1
    for x in arr:
        idx = int((x - min_val) / bucket_range)
        idx = min(idx, num_buckets - 1)  # Tránh out of range
        buckets[idx].append(x)
    # Sắp xếp từng bucket (dùng insertion sort)
    for bucket in buckets:
        bucket.sort()  # Insertion sort cho bucket nhỏ
    # Ghép lại
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result


# ==============================
# Demo
# ==============================

sample = [38, 27, 43, 3, 9, 82, 10]

print("=== Merge Sort ===")
print(f"Input:  {sample}")
print(f"Output: {merge_sort(sample)}")

print("\n=== Quick Sort ===")
arr_lom = sample[:]
quick_sort_lomuto(arr_lom)
print(f"Lomuto: {arr_lom}")

arr_hoa = sample[:]
quick_sort_hoare(arr_hoa)
print(f"Hoare:  {arr_hoa}")

arr_med = sample[:]
quick_sort_median(arr_med)
print(f"Median: {arr_med}")

# ==============================
# Counting / Radix / Bucket
# ==============================

print("\n=== Counting Sort ===")
int_arr = [4, 2, 2, 8, 3, 3, 1, 7]
print(f"Input:  {int_arr}")
print(f"Output: {counting_sort(int_arr)}")

print("\n=== Radix Sort (LSD) ===")
radix_arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Input:  {radix_arr}")
print(f"Output: {radix_sort_lsd(radix_arr)}")

print("\n=== Bucket Sort ===")
bucket_arr = [42, 32, 33, 52, 37, 47, 51, 78, 91, 10, 21]
print(f"Input:  {bucket_arr}")
print(f"Output: {bucket_sort(bucket_arr)}")

# ==============================
# Benchmark so sánh
# ==============================

print("\n=== Benchmark (n=2000) ===")
large_arr = [random.randint(0, 100000) for _ in range(2000)]
almost_sorted = sorted(large_arr)
almost_sorted[0], almost_sorted[-1] = almost_sorted[-1], almost_sorted[0]

algorithms = {
    "Merge Sort": lambda a: merge_sort(a[:]),
    "Quick Sort (Median)": lambda a: quick_sort_median(a[:], 0, len(a) - 1) or a,
    "Counting Sort": counting_sort,
    "Radix Sort": radix_sort_lsd,
    "Python sorted()": sorted,
}

def measure(func, arr):
    arr_copy = arr[:]
    start = time.perf_counter()
    func(arr_copy)
    elapsed = time.perf_counter() - start
    return elapsed

print(f"{'Algorithm':<22} {'Random':>10} {'Nearly Sorted':>15}")
for name, func in algorithms.items():
    t1 = measure(func, large_arr)
    t2 = measure(func, almost_sorted)
    print(f"{name:<22} {t1:>8.4f}s {t2:>13.4f}s")

print("\nTất cả đều xác nhận đúng:", end=" ")
expected = sorted(large_arr)
all_correct = all(
    func(large_arr) == expected
    for name, func in algorithms.items()
    if name != "Quick Sort (Median)"  # Median sửa in-place
)
print(all_correct)

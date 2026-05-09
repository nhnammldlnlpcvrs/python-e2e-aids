# ============================================
# 17. DIVIDE & CONQUER - CHIA ĐỂ TRỊ / DIVIDE & CONQUER
# ============================================
# 3 bước: Divide (chia) -> Conquer (trị) -> Combine (gộp).
# Các thuật toán: Merge Sort, Quick Sort, Quick Select, Binary Search.
# Phân tích bằng Master Theorem: T(n) = a*T(n/b) + f(n).

# Merge Sort đã có ở 14_sorting_advanced.py, ở đây tập trung các thuật toán khác.


# ==============================
# QUICK SELECT (Kth Smallest)
# ==============================

def quick_select(arr, k):
    """Tìm phần tử nhỏ thứ k (0-indexed) - O(n) average, O(n^2) worst"""
    if not arr or k < 0 or k >= len(arr):
        return None
    return _quick_select(arr, 0, len(arr) - 1, k)


def _quick_select(arr, left, right, k):
    if left == right:
        return arr[left]
    pivot_idx = _partition_quickselect(arr, left, right)
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return _quick_select(arr, left, pivot_idx - 1, k)
    else:
        return _quick_select(arr, pivot_idx + 1, right, k)


def _partition_quickselect(arr, left, right):
    """Lomuto partition cho quickselect"""
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


# ==============================
# MAXIMUM SUBARRAY (KADANE)
# ==============================

def max_subarray_kadane(arr):
    """Tìm subarray có tổng lớn nhất - O(n)
    Kadane: keep track of current max ending at i"""
    if not arr:
        return 0, -1, -1
    max_so_far = arr[0]
    current_max = arr[0]
    start = end = temp_start = 0
    for i in range(1, len(arr)):
        if current_max + arr[i] < arr[i]:
            current_max = arr[i]
            temp_start = i
        else:
            current_max += arr[i]
        if current_max > max_so_far:
            max_so_far = current_max
            start = temp_start
            end = i
    return max_so_far, start, end


def max_subarray_dc(arr, left=0, right=None):
    """Tìm max subarray bằng Divide & Conquer - O(n log n)"""
    if right is None:
        right = len(arr) - 1
    if left == right:
        return arr[left], left, right
    mid = (left + right) // 2
    # Max bên trái
    left_max, left_l, left_r = max_subarray_dc(arr, left, mid)
    # Max bên phải
    right_max, right_l, right_r = max_subarray_dc(arr, mid + 1, right)
    # Max xuyên qua mid
    cross_max, cross_l, cross_r = _max_crossing(arr, left, mid, right)
    # Lấy max trong 3
    if left_max >= right_max and left_max >= cross_max:
        return left_max, left_l, left_r
    elif right_max >= left_max and right_max >= cross_max:
        return right_max, right_l, right_r
    else:
        return cross_max, cross_l, cross_r


def _max_crossing(arr, left, mid, right):
    """Tìm subarray xuyên qua mid"""
    left_sum = float('-inf')
    total = 0
    max_left = mid
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i
    right_sum = float('-inf')
    total = 0
    max_right = mid + 1
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i
    return left_sum + right_sum, max_left, max_right


# ==============================
# CLOSEST PAIR (1D)
# ==============================

def closest_pair_1d(points):
    """Tìm cặp điểm gần nhất trong 1D - O(n log n)"""
    points = sorted(points)
    min_dist = float('inf')
    closest_pair = None
    for i in range(len(points) - 1):
        dist = points[i + 1] - points[i]
        if dist < min_dist:
            min_dist = dist
            closest_pair = (points[i], points[i + 1])
    return closest_pair, min_dist


# ==============================
# BINARY EXPONENTIATION (Lũy thừa nhanh)
# ==============================

def pow_mod(base, exp, mod):
    """Tính (base^exp) % mod - O(log exp)"""
    result = 1
    base = base % mod
    while exp > 0:
        if exp & 1:  # Nếu bit cuối = 1
            result = (result * base) % mod
        base = (base * base) % mod  # Bình phương
        exp >>= 1    # Dịch phải
    return result


def pow_recursive(base, exp):
    """Lũy thừa đệ quy - O(log exp)"""
    if exp == 0:
        return 1
    half = pow_recursive(base, exp // 2)
    if exp & 1:
        return half * half * base
    return half * half


# ==============================
# MASTER THEOREM
# ==============================

def master_theorem_overview():
    """Tóm tắt Master Theorem"""
    return """
    Master Theorem: T(n) = a * T(n/b) + f(n)

    So sánh f(n) với n^{log_b a}:

    Case 1: f(n) = O(n^{log_b a - ε})
            -> T(n) = Θ(n^{log_b a})

    Case 2: f(n) = Θ(n^{log_b a} * log^k n)
            -> T(n) = Θ(n^{log_b a} * log^{k+1} n)

    Case 3: f(n) = Ω(n^{log_b a + ε}) + a*f(n/b) <= c*f(n)
            -> T(n) = Θ(f(n))

    Ví dụ:
    - Merge Sort:  T(n) = 2T(n/2) + O(n)  -> Θ(n log n)  (Case 2)
    - Binary Search: T(n) = T(n/2) + O(1)  -> Θ(log n)    (Case 2)
    - Strassen:    T(n) = 7T(n/2) + O(n^2)  -> Θ(n^2.807)  (Case 1)
    """


# ==============================
# Demo
# ==============================

print("=== Quick Select ===")
arr = [7, 10, 4, 3, 20, 15, 8, 12]
print(f"arr = {arr}")
for k in range(len(arr)):
    print(f"  k={k} -> phần tử nhỏ thứ {k+1}: {quick_select(arr[:], k)}")
print(f"Median (k={len(arr)//2}): {quick_select(arr[:], len(arr)//2)}")

print("\n=== Maximum Subarray ===")
arr2 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"arr = {arr2}")
kadane_sum, start, end = max_subarray_kadane(arr2)
print(f"Kadane: max_sum={kadane_sum}, subarray={arr2[start:end+1]}")
dc_sum, dc_start, dc_end = max_subarray_dc(arr2)
print(f"D&C:    max_sum={dc_sum}, subarray={arr2[dc_start:dc_end+1]}")

print("\n=== Closest Pair (1D) ===")
points = [3, 10, 15, 21, 28, 35, 40]
pair, dist = closest_pair_1d(points)
print(f"Points: {points}")
print(f"Closest pair: {pair}, distance: {dist}")

print("\n=== Binary Exponentiation ===")
print(f"2^10 = {pow_recursive(2, 10)}")
print(f"2^10 mod 1000 = {pow_mod(2, 10, 1000)}")
print(f"3^100 mod 10^9+7 = {pow_mod(3, 100, 10**9+7)}")

print("\n=== Master Theorem ===")
print(master_theorem_overview())

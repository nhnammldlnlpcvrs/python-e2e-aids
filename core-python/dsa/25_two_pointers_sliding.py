# ============================================
# 25. TWO POINTERS & SLIDING WINDOW - HAI CON TRỎ & CỬA SỔ TRƯỢT
# ============================================
# Two pointers: dùng 2 con trỏ duyệt mảng để giảm từ O(n^2) -> O(n).
# Sliding window: duy trì 1 "cửa sổ" thỏa điều kiện, mở rộng/thu hẹp.

from collections import defaultdict, Counter


# ==============================
# TWO POINTERS (Opposite Direction)
# ==============================

def two_sum_sorted(arr, target):
    """Tìm 2 số có tổng = target trong mảng đã sắp xếp - O(n)"""
    left, right = 0, len(arr) - 1
    while left < right:
        s = arr[left] + arr[right]
        if s == target:
            return left, right
        elif s < target:
            left += 1
        else:
            right -= 1
    return None


def three_sum(arr, target=0):
    """Tìm tất cả bộ 3 số có tổng = target - O(n^2)"""
    arr.sort()
    result = []
    n = len(arr)
    for i in range(n - 2):
        if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicate
            continue
        left, right = i + 1, n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == target:
                result.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    return result


def container_most_water(height):
    """Container chứa nhiều nước nhất - O(n)"""
    left, right = 0, len(height) - 1
    max_area = 0
    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def is_palindrome_two_pointers(s):
    """Kiểm tra palindrome dùng 2 con trỏ"""
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


# ==============================
# TWO POINTERS (Same Direction / Fast-Slow)
# ==============================

def remove_duplicates_sorted(arr):
    """Xóa phần tử trùng trong mảng đã sắp xếp (in-place) - O(n)"""
    if not arr:
        return 0
    slow = 0  # Vị trí gán phần tử duy nhất tiếp theo
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1  # Độ dài mới


def move_zeros(arr):
    """Di chuyển tất cả số 0 về cuối mảng - O(n)"""
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    return arr


def dutch_national_flag(arr):
    """Sắp xếp mảng 0, 1, 2 (Dutch national flag) - O(n)"""
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
    return arr


# ==============================
# SLIDING WINDOW (Fixed Size)
# ==============================

def max_sum_subarray(arr, k):
    """Tổng lớn nhất của subarray kích thước k - O(n)"""
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def max_avg_subarray(arr, k):
    """Trung bình lớn nhất của subarray kích thước k"""
    if len(arr) < k:
        return None
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum / k


# ==============================
# SLIDING WINDOW (Variable Size)
# ==============================

def longest_substring_no_repeat(s):
    """Chuỗi con dài nhất không lặp ký tự - O(n)"""
    char_set = set()
    left = 0
    max_len = 0
    start = 0  # Vị trí bắt đầu của substring dài nhất
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left
    return max_len, s[start:start + max_len]


def min_window_substring(s, t):
    """Cửa sổ nhỏ nhất trong s chứa tất cả ký tự của t - O(|s| + |t|)"""
    if not t or not s:
        return ""
    target = Counter(t)
    window = defaultdict(int)
    have, need = 0, len(target)
    min_len = float('inf')
    min_start = 0
    left = 0

    for right in range(len(s)):
        ch = s[right]
        window[ch] += 1
        if ch in target and window[ch] == target[ch]:
            have += 1
        while have == need:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            # Thu hẹp từ trái
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in target and window[left_ch] < target[left_ch]:
                have -= 1
            left += 1

    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


def longest_substring_at_most_k_distinct(s, k):
    """Chuỗi con dài nhất có tối đa k ký tự khác nhau - O(n)"""
    freq = defaultdict(int)
    left = 0
    max_len = 0
    for right in range(len(s)):
        freq[s[right]] += 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1
        max_len = max(max_len, right - left + 1)
    return max_len


# ==============================
# Demo
# ==============================

print("=== Two Sum (sorted) ===")
arr = [2, 7, 11, 15]
print(f"arr={arr}, target=9 -> {two_sum_sorted(arr, 9)}")

print("\n=== Three Sum ===")
arr3 = [-1, 0, 1, 2, -1, -4]
print(f"arr={arr3}, target=0 -> {three_sum(arr3)}")

print("\n=== Container Most Water ===")
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"height={height} -> max_area={container_most_water(height)}")

print("\n=== Remove Duplicates (sorted) ===")
arr_dup = [1, 1, 2, 2, 3, 4, 4, 5]
new_len = remove_duplicates_sorted(arr_dup)
print(f"  Input: [1,1,2,2,3,4,4,5] -> len={new_len}, arr={arr_dup[:new_len]}")

print("\n=== Move Zeros ===")
arr_zero = [0, 1, 0, 3, 12]
print(f"  Input: [0,1,0,3,12] -> {move_zeros(arr_zero)}")

print("\n=== Dutch National Flag ===")
arr_dnf = [2, 0, 2, 1, 1, 0]
print(f"  Input: [2,0,2,1,1,0] -> {dutch_national_flag(arr_dnf)}")

print("\n=== Fixed Sliding Window ===")
arr_sw = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(f"arr={arr_sw}, k={k}")
print(f"Max sum subarray (size {k}): {max_sum_subarray(arr_sw, k)}")
print(f"Max avg subarray (size {k}): {max_avg_subarray(arr_sw, k):.2f}")

print("\n=== Variable Sliding Window ===")
s = "abcabcbb"
length, substr = longest_substring_no_repeat(s)
print(f"Longest no-repeat in '{s}': '{substr}' (length={length})")

s2, t2 = "ADOBECODEBANC", "ABC"
print(f"Min window in '{s2}' containing '{t2}': '{min_window_substring(s2, t2)}'")

s3 = "eceba"
print(f"Longest at most 2 distinct in '{s3}': {longest_substring_at_most_k_distinct(s3, 2)}")

print("\n=== Palindrome Check ===")
for w in ["radar", "hello", "level", "python"]:
    print(f"  '{w}': {is_palindrome_two_pointers(w)}")

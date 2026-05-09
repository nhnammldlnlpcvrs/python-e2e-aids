# ============================================
# 23. STRING ALGORITHMS - THUẬT TOÁN CHUỖI / STRING ALGORITHMS
# ============================================
# KMP: tìm pattern trong text - O(n+m).
# Rabin-Karp: dùng rolling hash - O(n+m) avg.
# Z-algorithm: tìm mọi occurrence - O(n+m).


# ==============================
# KMP (Knuth-Morris-Pratt)
# ==============================

def build_lps(pattern):
    """Xây dựng mảng LPS (Longest Prefix Suffix) - O(m)"""
    m = len(pattern)
    lps = [0] * m
    length = 0  # Độ dài prefix = suffix hiện tại
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # Fallback
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """Tìm pattern trong text dùng KMP - O(n+m)
    Trả về danh sách vị trí bắt đầu khớp (0-indexed)."""
    if not pattern:
        return []
    n, m = len(text), len(pattern)
    lps = build_lps(pattern)
    matches = []
    i = j = 0  # i: text index, j: pattern index
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:  # Tìm thấy match
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


# ==============================
# RABIN-KARP (Rolling Hash)
# ==============================

def rabin_karp(text, pattern, prime=101):
    """Tìm pattern dùng Rabin-Karp với rolling hash - O(n+m) avg"""
    n, m = len(text), len(pattern)
    if m > n:
        return []

    base = 256  # Số ký tự (ASCII)
    # Tính hash của pattern và window đầu tiên
    pattern_hash = 0
    window_hash = 0
    h = 1  # base^(m-1) % prime
    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        window_hash = (base * window_hash + ord(text[i])) % prime

    matches = []
    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i:i + m] == pattern:  # Xác nhận lại (tránh collision)
                matches.append(i)
        if i < n - m:
            # Rolling hash: xóa text[i], thêm text[i+m]
            window_hash = (base * (window_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if window_hash < 0:
                window_hash += prime
    return matches


# ==============================
# Z-ALGORITHM
# ==============================

def build_z_array(s):
    """Xây dựng Z-array - O(n)
    Z[i] = length of longest substring starting at i that matches prefix"""
    n = len(s)
    z = [0] * n
    left = right = 0  # Cửa sổ Z-box: [left, right)
    for i in range(1, n):
        if i < right:
            z[i] = min(right - i, z[i - left])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > right:
            left = i
            right = i + z[i]
    return z


def z_algorithm_search(text, pattern):
    """Tìm pattern trong text dùng Z-algorithm - O(n+m)
    Tạo chuỗi pattern + '$' + text, tính Z-array."""
    if not pattern:
        return []
    concat = pattern + '$' + text
    z = build_z_array(concat)
    m = len(pattern)
    matches = []
    for i in range(m + 1, len(concat)):
        if z[i] == m:
            matches.append(i - m - 1)
    return matches


# ==============================
# LONGEST PALINDROMIC SUBSTRING
# ==============================

def longest_palindrome_expand(s):
    """Tìm palindrome dài nhất - expand around center - O(n^2)"""
    if not s:
        return ""
    start_idx, max_len = 0, 1
    for i in range(len(s)):
        # Palindrome độ dài lẻ
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start_idx = left
                max_len = right - left + 1
            left -= 1
            right += 1
        # Palindrome độ dài chẵn
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start_idx = left
                max_len = right - left + 1
            left -= 1
            right += 1
    return s[start_idx:start_idx + max_len]


# Manacher's Algorithm (overview + simplified)
def manacher_overview():
    return """
    Manacher's Algorithm: O(n)
    - Biến đổi chuỗi: "abc" -> "#a#b#c#" để xử lý cả pal chẵn/lẻ
    - Dùng mảng P[i] = bán kính palindrome tại i
    - Tận dụng tính đối xứng để skip (giống Z-algorithm)
    - Phức tạp hơn expand-around-center nhưng O(n) guaranteed
    """


# ==============================
# LONGEST COMMON PREFIX (LCP)
# ==============================

def longest_common_prefix(strs):
    """Tìm LCP của mảng các string - O(S) với S = tổng ký tự"""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefix) and i < len(s) and prefix[i] == s[i]:
            i += 1
        prefix = prefix[:i]
        if not prefix:
            break
    return prefix


# ==============================
# Demo
# ==============================

print("=== KMP ===")
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"Text:    '{text}'")
print(f"Pattern: '{pattern}'")
print(f"LPS: {build_lps(pattern)}")
print(f"KMP matches: {kmp_search(text, pattern)}")

print("\n=== Rabin-Karp ===")
print(f"Rabin-Karp matches: {rabin_karp(text, pattern)}")

print("\n=== Z-Algorithm ===")
s = "aabxaabxcaabxaabxay"
print(f"String: '{s}'")
print(f"Z-array: {build_z_array(s)[:20]}...")
print(f"Search '{pattern}' in '{text}': {z_algorithm_search(text, pattern)}")

# Verify all 3 give same results
kmp_res = kmp_search(text, pattern)
rk_res = rabin_karp(text, pattern)
z_res = z_algorithm_search(text, pattern)
print(f"\nAll 3 algorithms match: {kmp_res == rk_res == z_res}")

print("\n=== Longest Palindromic Substring ===")
test_strings = ["babad", "cbbd", "a", "racecar", "bananas"]
for ts in test_strings:
    lps_result = longest_palindrome_expand(ts)
    print(f"  '{ts}' -> '{lps_result}'")

print("\n=== Manacher's Algorithm Overview ===")
print(manacher_overview())

print("=== Longest Common Prefix ===")
strs = ["flower", "flow", "flight"]
print(f"  {strs} -> '{longest_common_prefix(strs)}'")
strs2 = ["dog", "racecar", "car"]
print(f"  {strs2} -> '{longest_common_prefix(strs2)}'")

# ==============================
# So sánh thuật toán tìm pattern
# ==============================

print("\n=== So sánh Pattern Matching ===")
print("""
Thuật toán   | Time (Worst)   | Time (Avg)    | Space | Đặc điểm
-------------|----------------|---------------|-------|---------
Naive        | O(n*m)         | O(n*m)        | O(1)  | Đơn giản
KMP          | O(n+m)         | O(n+m)        | O(m)  | Không quay lui text
Rabin-Karp   | O(n*m)         | O(n+m)        | O(1)  | Dùng hash, có thể false positive
Z-algorithm  | O(n+m)         | O(n+m)        | O(n)  | Linh hoạt, dùng cho nhiều bài toán
Boyer-Moore  | O(n*m)         | O(n/m)        | O(k)  | Nhanh trong thực tế, skip thông minh
""")

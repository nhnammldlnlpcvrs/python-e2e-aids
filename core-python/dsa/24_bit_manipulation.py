# ============================================
# 24. BIT MANIPULATION - THAO TÁC BIT / BIT MANIPULATION
# ============================================
# Làm việc trực tiếp với bit của số nguyên.
# Nhanh, tiết kiệm bộ nhớ, thường dùng trong:
#   - Tối ưu hóa, embedded systems
#   - Bitmask DP, trạng thái nén
#   - Crypto, hash, checksum


# ==============================
# BASIC BIT OPERATIONS
# ==============================

print("=== Basic Bit Operations ===")
a, b = 0b1100, 0b1010  # 12, 10
print(f"a = {a} ({bin(a)})")
print(f"b = {b} ({bin(b)})")
print(f"a & b  (AND)      = {a & b} ({bin(a & b)})")   # 1000 = 8
print(f"a | b  (OR)       = {a | b} ({bin(a | b)})")   # 1110 = 14
print(f"a ^ b  (XOR)      = {a ^ b} ({bin(a ^ b)})")   # 0110 = 6
print(f"~a     (NOT)      = {~a} ({bin(~a)})")          # Đảo bit (two's complement)
print(f"a << 1 (left)     = {a << 1} ({bin(a << 1)})") # 11000 = 24
print(f"a >> 1 (right)    = {a >> 1} ({bin(a >> 1)})") # 110 = 6


# ==============================
# BIT MANIPULATION TRICKS
# ==============================

def get_bit(n, pos):
    """Lấy bit tại vị trí pos (0-indexed từ phải)"""
    return (n >> pos) & 1


def set_bit(n, pos):
    """Bật bit tại pos lên 1"""
    return n | (1 << pos)


def clear_bit(n, pos):
    """Tắt bit tại pos về 0"""
    return n & ~(1 << pos)


def toggle_bit(n, pos):
    """Đảo bit tại pos"""
    return n ^ (1 << pos)


def is_power_of_two(n):
    """Kiểm tra n có phải lũy thừa của 2"""
    return n > 0 and (n & (n - 1)) == 0


def count_set_bits(n):
    """Đếm số bit 1 (Brian Kernighan's algorithm) - O(k) với k = số bit 1"""
    count = 0
    while n:
        n &= n - 1  # Tắt bit 1 thấp nhất
        count += 1
    return count


def lowest_set_bit(n):
    """Lấy bit 1 thấp nhất (LSB)"""
    return n & -n


def clear_lowest_set_bit(n):
    """Tắt bit 1 thấp nhất"""
    return n & (n - 1)


def highest_set_bit_pos(n):
    """Vị trí bit 1 cao nhất"""
    if n == 0:
        return -1
    pos = 0
    while n > 1:
        n >>= 1
        pos += 1
    return pos


def isolate_lowest_set_bit(n):
    """Giữ lại bit 1 thấp nhất, xóa hết các bit khác"""
    return n & -n


print("\n=== Bit Tricks ===")
n = 0b10110100  # 180
print(f"n = {n} ({bin(n)})")
print(f"get_bit(n, 2): {get_bit(n, 2)}")
print(f"set_bit(n, 1): {set_bit(n, 1)} ({bin(set_bit(n, 1))})")
print(f"clear_bit(n, 4): {clear_bit(n, 4)} ({bin(clear_bit(n, 4))})")
print(f"toggle_bit(n, 3): {toggle_bit(n, 3)} ({bin(toggle_bit(n, 3))})")
print(f"is_power_of_two(16): {is_power_of_two(16)}")
print(f"is_power_of_two(18): {is_power_of_two(18)}")
print(f"count_set_bits(n): {count_set_bits(n)}")  # 4
print(f"lowest_set_bit: {lowest_set_bit(n)} ({bin(lowest_set_bit(n))})")
print(f"clear_lowest_set_bit: {clear_lowest_set_bit(n)} ({bin(clear_lowest_set_bit(n))})")

# ==============================
# COMMON APPLICATIONS
# ==============================

print("\n=== Common Applications ===")

# 1. Tìm số xuất hiện 1 lần trong mảng các số xuất hiện 2 lần
def find_single_number(nums):
    """Mọi số xuất hiện 2 lần, 1 số xuất hiện 1 lần - O(n), O(1)"""
    result = 0
    for n in nums:
        result ^= n
    return result

nums = [4, 1, 2, 1, 2]
print(f"1. Single number in {nums}: {find_single_number(nums)}")

# 2. Tìm 2 số xuất hiện 1 lần
def find_two_single_numbers(nums):
    """Mọi số xuất hiện 2 lần, 2 số xuất hiện 1 lần"""
    xor_all = 0
    for n in nums:
        xor_all ^= n
    # Tìm bit khác nhau đầu tiên của 2 số
    diff_bit = xor_all & -xor_all
    a = b = 0
    for n in nums:
        if n & diff_bit:
            a ^= n
        else:
            b ^= n
    return a, b

nums2 = [1, 2, 1, 3, 2, 5]
print(f"2. Two single numbers in {nums2}: {find_two_single_numbers(nums2)}")

# 3. Đếm bit 1 từ 0 đến n (DP pattern)
def count_bits(n):
    """Đếm số bit 1 cho mọi số từ 0 đến n - O(n)"""
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)  # dp[i] = dp[i/2] + last_bit
    return dp

print(f"3. Count bits 0..5: {count_bits(5)}")

# 4. Tập con bằng bitmask
def subsets_bitmask(arr):
    """Sinh tất cả tập con dùng bitmask - O(n * 2^n)"""
    n = len(arr)
    result = []
    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(arr[i])
        result.append(subset)
    return result

print(f"4. Subsets of [1,2,3] by bitmask: {subsets_bitmask([1, 2, 3])[:5]}...")

# 5. Bit DP intro: TSP (Traveling Salesman) simplified
def tsp_bitmask(dist):
    """TSP cơ bản dùng bitmask DP - O(n^2 * 2^n)"""
    n = len(dist)
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Bắt đầu từ 0, đã visit {0}

    for mask in range(1 << n):
        for u in range(n):
            if dp[mask][u] == INF:
                continue
            for v in range(n):
                if mask & (1 << v):  # Đã visit v
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + dist[u][v])

    # Quay về 0
    full_mask = (1 << n) - 1
    min_cost = min(dp[full_mask][u] + dist[u][0] for u in range(n))
    return min_cost


print("\n5. TSP Bitmask DP:")
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
]
print(f"   Min cost: {tsp_bitmask(distances)}")

# ==============================
# BIT TRICKS REFERENCE
# ==============================

print("\n=== Bit Tricks Reference ===")
print("""
x & 1          -> bit cuối cùng (x lẻ hay chẵn)
x & (x-1)      -> tắt bit 1 thấp nhất
x & -x         -> giữ bit 1 thấp nhất (LSB)
x | (1 << k)   -> bật bit thứ k
x & ~(1 << k)  -> tắt bit thứ k
x ^ (1 << k)   -> đảo bit thứ k
x ^ x          -> 0
x ^ 0          -> x
x >> 1         -> x // 2
x << 1         -> x * 2
x & (x-1) == 0 -> x là lũy thừa của 2
x & 0x55555555 -> các bit ở vị trí chẵn
x & 0xAAAAAAAA -> các bit ở vị trí lẻ
""")

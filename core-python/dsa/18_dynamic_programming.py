# ============================================
# 18. DYNAMIC PROGRAMMING - QUY HOẠCH ĐỘNG / DP
# ============================================
# DP: chia bài toán thành các bài toán con chồng lấp (overlapping subproblems)
# và có cấu trúc con tối ưu (optimal substructure).
# 2 cách tiếp cận: Top-down (memoization) & Bottom-up (tabulation).


# ==============================
# 1. FIBONACCI - DP cơ bản nhất
# ==============================

def fib_memo(n, memo=None):
    """Top-down: Fibonacci với memoization - O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    """Bottom-up: Fibonacci với tabulation - O(n), O(1) space"""
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1


# ==============================
# 2. KNAPSACK 0/1 (Balo)
# ==============================

def knapsack_01(weights, values, capacity):
    """Knapsack 0/1 - bottom-up DP - O(n*W)"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(capacity + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[n][capacity]


def knapsack_01_optimized(weights, values, capacity):
    """Knapsack 0/1 - tối ưu về O(W) space"""
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for j in range(capacity, w - 1, -1):  # Duyệt ngược!
            dp[j] = max(dp[j], dp[j - w] + v)
    return dp[capacity]


def knapsack_with_items(weights, values, capacity):
    """Knapsack 0/1 + truy vết items được chọn"""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        w, v = weights[i - 1], values[i - 1]
        for j in range(capacity + 1):
            if w <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
    # Truy vết
    items = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            items.append(i - 1)
            j -= weights[i - 1]
    return dp[n][capacity], items[::-1]


# ==============================
# 3. LCS (Longest Common Subsequence)
# ==============================

def lcs(s1, s2):
    """Chuỗi con chung dài nhất - O(m*n)"""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    # Truy vết LCS
    lcs_result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs_result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return dp[m][n], ''.join(reversed(lcs_result))


# ==============================
# 4. LIS (Longest Increasing Subsequence)
# ==============================

def lis_dp(arr):
    """LIS - O(n^2)"""
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) if dp else 0


def lis_nlogn(arr):
    """LIS - O(n log n) dùng patience sorting + binary search"""
    import bisect
    tails = []
    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


# ==============================
# 5. COIN CHANGE
# ==============================

def coin_change_min(coins, amount):
    """Số đồng xu tối thiểu để tạo amount - O(amount * len(coins))"""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """Số cách đổi amount - O(amount * len(coins))"""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


# ==============================
# 6. EDIT DISTANCE (Levenshtein)
# ==============================

def edit_distance(s1, s2):
    """Khoảng cách Levenshtein - O(m*n)
    Số thao tác tối thiểu (insert, delete, replace) để biến s1 -> s2."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    return dp[m][n]


# ==============================
# 7. MATRIX CHAIN MULTIPLICATION
# ==============================

def matrix_chain_order(dims):
    """Số phép nhân tối thiểu để nhân chuỗi ma trận - O(n^3)
    dims[i-1] x dims[i] là kích thước ma trận thứ i."""
    n = len(dims) - 1
    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):  # length của chuỗi
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1]
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n - 1]


# ==============================
# Demo
# ==============================

print("=== Fibonacci ===")
print("fib_memo(20):", fib_memo(20))
print("fib_tab(20): ", fib_tab(20))

print("\n=== Knapsack 0/1 ===")
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 8
print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
print(f"Max value (2D): {knapsack_01(weights, values, capacity)}")
print(f"Max value (1D): {knapsack_01_optimized(weights, values, capacity)}")
max_val, items = knapsack_with_items(weights, values, capacity)
print(f"Items selected: {items} -> weights={[weights[i] for i in items]}, values={[values[i] for i in items]}")

print("\n=== LCS ===")
s1, s2 = "ABCDGH", "AEDFHR"
length, subsequence = lcs(s1, s2)
print(f"'{s1}' vs '{s2}' -> LCS: '{subsequence}' (length={length})")

print("\n=== LIS ===")
arr_lis = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(f"arr: {arr_lis}")
print(f"LIS O(n^2): {lis_dp(arr_lis)}")
print(f"LIS O(n log n): {lis_nlogn(arr_lis)}")

print("\n=== Coin Change ===")
coins = [1, 2, 5]
amount = 11
print(f"Coins: {coins}, Amount: {amount}")
print(f"Min coins: {coin_change_min(coins, amount)}")
print(f"Số cách đổi {amount}: {coin_change_ways(coins, amount)}")

print("\n=== Edit Distance ===")
w1, w2 = "kitten", "sitting"
print(f"'{w1}' -> '{w2}': {edit_distance(w1, w2)}")
w3, w4 = "intention", "execution"
print(f"'{w3}' -> '{w4}': {edit_distance(w3, w4)}")

print("\n=== Matrix Chain Multiplication ===")
dims = [10, 30, 5, 60]  # 3 ma trận: 10x30, 30x5, 5x60
print(f"Dimensions: {dims}")
print(f"Min multiplications: {matrix_chain_order(dims)}")

# ==============================
# DP Patterns
# ==============================

print("\n=== DP Problem-Solving Patterns ===")
print("""
1. 0/1 Knapsack pattern: chọn/không chọn từng item
   -> Subset sum, Partition equal sum, Target sum

2. Unbounded Knapsack: có thể chọn 1 item nhiều lần
   -> Coin change, Rod cutting, Min cost to fill bag

3. LCS pattern: 2 chuỗi, tìm subsequence chung
   -> Edit distance, Shortest common supersequence

4. LIS pattern: dãy con tăng dài nhất
   -> Russian doll envelopes, Box stacking

5. Matrix Chain pattern: chia đoạn tối ưu
   -> Burst balloons, Min cost tree from leaf

6. DP on Trees: DP trên cấu trúc cây
   -> Diameter of tree, House robber III

7. DP on Grid: bài toán lưới
   -> Unique paths, Min path sum, Maximal square

8. State Machine DP: DP với trạng thái
   -> Best time to buy/sell stock, Max profit with cooldown

9. Digit DP: đếm số thỏa điều kiện trong khoảng
   -> Count numbers with constraints

10. Bitmask DP: dùng bitmask làm trạng thái
    -> TSP, Assignment problem
""")

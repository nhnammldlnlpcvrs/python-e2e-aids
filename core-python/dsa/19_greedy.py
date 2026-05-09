# ============================================
# 19. GREEDY - THAM LAM / GREEDY ALGORITHMS
# ============================================
# Greedy: chọn phương án tối ưu cục bộ (local optimal) ở mỗi bước,
# hy vọng dẫn đến tối ưu toàn cục (global optimal).
# Chỉ đúng với bài toán có "greedy choice property".

import heapq


# ==============================
# 1. ACTIVITY SELECTION
# ==============================

def activity_selection(start, finish):
    """Chọn tối đa số hoạt động không trùng lịch - O(n log n)
    Chọn hoạt động kết thúc sớm nhất."""
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    selected = []
    last_finish = float('-inf')
    for s, f in activities:
        if s >= last_finish:
            selected.append((s, f))
            last_finish = f
    return selected


# ==============================
# 2. FRACTIONAL KNAPSACK
# ==============================

def fractional_knapsack(weights, values, capacity):
    """Knapsack dạng phân số - O(n log n)
    Có thể lấy 1 phần của item. Chọn item có value/weight cao nhất trước."""
    items = [(v / w, w, v) for w, v in zip(weights, values)]
    items.sort(reverse=True)  # Sắp xếp theo value/weight giảm dần

    total_value = 0
    taken = []
    for ratio, w, v in items:
        if capacity <= 0:
            break
        take = min(w, capacity)
        total_value += take * ratio
        taken.append((v, w, take, "full" if take == w else f"{take}/{w}"))
        capacity -= take
    return total_value, taken


# ==============================
# 3. HUFFMAN CODING
# ==============================

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(text):
    """Xây dựng mã Huffman cho text"""
    if not text:
        return {}, None
    # Đếm tần suất
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    # Heap
    heap = [HuffmanNode(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    # Sinh mã
    codes = {}
    def generate(node, code):
        if node is None:
            return
        if node.char is not None:
            codes[node.char] = code
            return
        generate(node.left, code + "0")
        generate(node.right, code + "1")
    generate(heap[0], "")
    return codes, heap[0]


# ==============================
# 4. JOB SEQUENCING WITH DEADLINES
# ==============================

def job_sequencing(jobs):
    """Chọn jobs để max profit, mỗi job mất 1 đơn vị thời gian.
    jobs = [(profit, deadline), ...]"""
    # Sắp xếp theo profit giảm dần
    jobs_sorted = sorted(jobs, key=lambda x: x[0], reverse=True)
    max_deadline = max(j[1] for j in jobs) if jobs else 0
    # Mảng slot: -1 = trống
    slots = [-1] * max_deadline
    total_profit = 0
    selected = []
    for profit, deadline in jobs_sorted:
        # Tìm slot trống từ deadline-1 về 0
        for t in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[t] == -1:
                slots[t] = (profit, deadline)
                total_profit += profit
                selected.append((profit, deadline))
                break
    return total_profit, selected


# ==============================
# 5. COIN CHANGE GREEDY (minh họa khi tham lam sai)
# ==============================

def coin_change_greedy(coins, amount):
    """Đổi xu tham lam - chỉ đúng với 1 số bộ coins (VD: 1,2,5,10)"""
    coins = sorted(coins, reverse=True)
    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    return result if amount == 0 else None


# ==============================
# 6. MINIMUM PLATFORMS (Trains)
# ==============================

def min_platforms(arrivals, departures):
    """Số sân ga tối thiểu cho các chuyến tàu"""
    arrivals.sort()
    departures.sort()
    n = len(arrivals)
    platforms = 0
    max_platforms = 0
    i = j = 0
    while i < n and j < n:
        if arrivals[i] <= departures[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1
    return max_platforms


# ==============================
# Demo
# ==============================

print("=== Activity Selection ===")
start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
selected = activity_selection(start, finish)
print(f"Activities (start, finish): {list(zip(start, finish))}")
print(f"Selected ({len(selected)}): {selected}")

print("\n=== Fractional Knapsack ===")
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
total_val, taken = fractional_knapsack(weights, values, capacity)
print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
print(f"Max value: {total_val:.2f}")
for v, w, take, status in taken:
    print(f"  Item (value={v}, weight={w}): take {status}")

print("\n=== Huffman Coding ===")
text = "aababcabcdab"
codes, _ = huffman_coding(text)
print(f"Text: '{text}'")
for ch, code in sorted(codes.items()):
    print(f"  '{ch}' -> {code}")
encoded = ''.join(codes[ch] for ch in text)
print(f"Encoded: {encoded}")
print(f"Compression: {len(text)*8} bits -> {len(encoded)} bits")

print("\n=== Job Sequencing ===")
jobs = [(100, 2), (19, 1), (27, 2), (25, 1), (15, 3)]
profit, selected_jobs = job_sequencing(jobs)
print(f"Jobs (profit, deadline): {jobs}")
print(f"Max profit: {profit}")
print(f"Selected: {selected_jobs}")

print("\n=== Coin Change (Greedy) ===")
print("Bộ xu chuẩn {1,2,5,10}, amount=28:")
print(f"  Kết quả: {coin_change_greedy([1, 2, 5, 10], 28)}")
print("Bộ xu 'lạ' {1,3,4}, amount=6:")
result = coin_change_greedy([1, 3, 4], 6)
print(f"  Greedy: {result} (4+1+1 = 3 xu)")
print(f"  Tối ưu thực sự: 3+3 = 2 xu")
print("  -> Greedy KHÔNG luôn tối ưu cho Coin Change!")

print("\n=== Minimum Platforms ===")
arr = [900, 940, 950, 1100, 1500, 1800]
dep = [910, 1200, 1120, 1130, 1900, 2000]
print(f"Arrivals:   {arr}")
print(f"Departures: {dep}")
print(f"Min platforms: {min_platforms(arr, dep)}")

# ==============================
# Greedy vs DP
# ==============================

print("\n=== Greedy vs DP ===")
print("""
Khi nào dùng Greedy:
  - Bài toán có "greedy choice property" (chọn tối ưu cục bộ = tối ưu toàn cục)
  - Ví dụ: Activity Selection, Huffman, Kruskal/Prim MST, Dijkstra

Khi nào cần DP:
  - Greedy cho kết quả sai (VD: Coin Change với bộ xu bất kỳ)
  - Bài toán có overlapping subproblems
  - Ví dụ: 0/1 Knapsack, LCS, Edit Distance, Coin Change tổng quát

Cách nhận biết:
  - Thử greedy trước. Nếu counterexample tồn tại -> dùng DP.
  - Greedy thường O(n log n), DP thường O(n^2) hoặc tệ hơn.
""")

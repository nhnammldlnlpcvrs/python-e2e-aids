# ============================================
# 16. RECURSION & BACKTRACKING - ĐỆ QUY & QUAY LUI
# ============================================
# Recursion: hàm gọi chính nó, gồm base case + recursive case.
# Backtracking: thử tất cả khả năng, quay lui khi gặp ngõ cụt.


# ==============================
# RECURSION CƠ BẢN
# ==============================

def factorial(n):
    """Giai thừa - O(n)"""
    if n <= 1:          # Base case
        return 1
    return n * factorial(n - 1)  # Recursive case


def fibonacci(n):
    """Fibonacci đệ quy - O(2^n) - minh họa, không tối ưu"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci với memoization (top-down DP)
def fibonacci_memo(n, memo=None):
    """Fibonacci có memoization - O(n)"""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


# ==============================
# SUBSETS (TẬP CON) - 2^n
# ==============================

def generate_subsets(nums):
    """Sinh tất cả tập con (power set) - O(n * 2^n)"""
    result = []

    def backtrack(start, current):
        result.append(current[:])  # Lưu bản copy
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)  # Include nums[i]
            current.pop()              # Exclude nums[i] (backtrack)

    backtrack(0, [])
    return result


# ==============================
# PERMUTATIONS (HOÁN VỊ) - n!
# ==============================

def generate_permutations(nums):
    """Sinh tất cả hoán vị - O(n * n!)"""
    result = []
    used = [False] * len(nums)

    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current.append(nums[i])
                backtrack(current)
                current.pop()
                used[i] = False

    backtrack([])
    return result


# ==============================
# COMBINATIONS (TỔ HỢP) - C(n,k)
# ==============================

def generate_combinations(n, k):
    """Sinh C(n, k) - tổ hợp chập k của n"""
    result = []

    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()

    backtrack(1, [])
    return result


# ==============================
# N-QUEENS - ĐẶT HẬU
# ==============================

def solve_n_queens(n):
    """Giải bài toán N-Queens: đặt n quân hậu lên bàn cờ nxn"""
    solutions = []
    board = [-1] * n  # board[row] = col

    def is_safe(row, col):
        for r in range(row):
            if board[r] == col:
                return False
            if abs(board[r] - col) == abs(r - row):  # Cùng đường chéo
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                # board[row] tự bị ghi đè, không cần undo

    backtrack(0)
    return solutions


def print_n_queens_solution(board):
    """In bàn cờ"""
    n = len(board)
    for row in range(n):
        line = ["."] * n
        line[board[row]] = "Q"
        print("  ", " ".join(line))
    print()


# ==============================
# SUDOKU SOLVER (ĐƠN GIẢN)
# ==============================

def solve_sudoku(board):
    """Giải Sudoku 9x9 bằng backtracking"""

    def is_valid(board, row, col, num):
        # Kiểm tra hàng
        if num in board[row]:
            return False
        # Kiểm tra cột
        if num in [board[r][col] for r in range(9)]:
            return False
        # Kiểm tra box 3x3
        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False
        return True

    def backtrack():
        for r in range(9):
            for c in range(9):
                if board[r][c] == 0:
                    for num in range(1, 10):
                        if is_valid(board, r, c, num):
                            board[r][c] = num
                            if backtrack():
                                return True
                            board[r][c] = 0  # Quay lui
                    return False
        return True

    return backtrack()


# ==============================
# Demo
# ==============================

print("=== Recursion Cơ bản ===")
print("5! =", factorial(5))
print("fibonacci(8) =", fibonacci(8))
print("fibonacci_memo(30) =", fibonacci_memo(30))

print("\n=== Subsets (Tập con) ===")
nums = [1, 2, 3]
subsets = generate_subsets(nums)
print(f"Mảng: {nums}")
print(f"Tất cả tập con ({len(subsets)} tập):")
for s in subsets:
    print(f"  {s}")

print("\n=== Permutations (Hoán vị) ===")
nums2 = [1, 2, 3]
perms = generate_permutations(nums2)
print(f"Mảng: {nums2}")
print(f"Tất cả hoán vị ({len(perms)} hoán vị):")
for p in perms:
    print(f"  {p}")

print("\n=== Combinations (Tổ hợp) ===")
combs = generate_combinations(4, 2)
print(f"C(4, 2) = {len(combs)}:")
for c in combs:
    print(f"  {c}")

print("\n=== N-Queens ===")
n = 4
solutions = solve_n_queens(n)
print(f"N={n}: {len(solutions)} solutions")
for sol in solutions:
    print_n_queens_solution(sol)

print("=== Sudoku Solver ===")
# 0 = ô trống
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

print("Input (0 = trống):")
for row in sudoku_board:
    print(" ", row)

solved = solve_sudoku(sudoku_board)
print(f"\nĐã giải được: {solved}")
if solved:
    print("Output:")
    for row in sudoku_board:
        print(" ", row)

# ==============================
# Backtracking Pattern
# ==============================

print("\n=== Backtracking Template ===")
print("""
def backtrack(state):
    if is_solution(state):
        output(state)
        return
    for choice in choices(state):
        if is_valid(choice):
            apply(choice, state)
            backtrack(state)
            undo(choice, state)    # <-- Quay lui

3 bước: Chọn -> Thử -> Hoàn tác
""")

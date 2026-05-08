# ============================================
# 6. LAMBDA - HÀM ẨN DANH
# ============================================
# Lambda là hàm 1 dòng, không tên, không cần def
# Cú pháp: lambda arguments: expression
# Chỉ chứa 1 biểu thức, không có statement (if, for, return,...)

# --- Lambda cơ bản ---
square = lambda x: x * x
print("5^2 =", square(5))  # 25

# Tương đương với:
# def square(x):
#     return x * x


# --- Lambda nhiều tham số ---
add = lambda a, b: a + b
print("3 + 5 =", add(3, 5))

multiply = lambda a, b, c: a * b * c
print("2 * 3 * 4 =", multiply(2, 3, 4))


# --- Lambda không tham số ---
get_time = lambda: "12:00"
print(get_time())


# --- Lambda với điều kiện (ternary) ---
# Cú pháp: <true_value> if <condition> else <false_value>
is_even = lambda x: "Chẵn" if x % 2 == 0 else "Lẻ"
print("5 là:", is_even(5))
print("6 là:", is_even(6))

max_of_two = lambda a, b: a if a > b else b
print("Max của 10 và 20:", max_of_two(10, 20))


# --- Lambda với default parameter ---
power = lambda base, exp=2: base ** exp
print("3^2 =", power(3))
print("3^3 =", power(3, 3))


# --- Dùng lambda trực tiếp không gán biến (IIFE) ---
# (lambda args: expr)(values) -> gọi ngay lập tức
result = (lambda x, y: x * y)(6, 7)
print("6 * 7 =", result)  # 42


# --- Lambda trong các hàm built-in ---
# sorted() với key
students = [
    {"name": "Nam", "score": 8},
    {"name": "An", "score": 9},
    {"name": "Linh", "score": 7},
]

# Sắp xếp theo score
sorted_students = sorted(students, key=lambda s: s["score"])
print("Sorted by score:", sorted_students)

# Sắp xếp theo tên
sorted_by_name = sorted(students, key=lambda s: s["name"])
print("Sorted by name:", sorted_by_name)

# Sắp xếp theo score giảm dần
sorted_desc = sorted(students, key=lambda s: s["score"], reverse=True)
print("Sorted desc:", sorted_desc)


# max() / min() với key
nums = [1, -2, 3, -4, 5]
max_abs = max(nums, key=lambda x: abs(x))  # Tìm số có |x| lớn nhất
print("Max |x|:", max_abs)  # 5 (hoặc -5, tùy xuất hiện trước)


# ===== SO SÁNH: Lambda vs Def =====
# Lambda: nhanh, 1 dòng, dùng 1 lần rồi bỏ
# Def: nhiều dòng, có docstring, tái sử dụng, phức tạp

# KHI NÀO DÙNG LAMBDA:
# 1. Truyền vào hàm built-in (sorted, map, filter, max, min...)
# 2. Callback đơn giản
# 3. Không cần đặt tên, dùng 1 lần

# KHI NÀO DÙNG DEF:
# 1. Logic phức tạp, nhiều dòng
# 2. Cần docstring
# 3. Cần tái sử dụng nhiều lần
# 4. Có vòng lặp, try/except, v.v.

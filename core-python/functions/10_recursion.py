# ============================================
# 10. RECURSION - ĐỆ QUY
# ============================================
# Đệ quy: hàm gọi chính nó
# Cần 2 thứ: 1) Base case (điểm dừng) 2) Recursive case (bước đệ quy)

# ===== Đệ quy cơ bản: Giai thừa =====
# n! = n * (n-1)!, với 0! = 1


def factorial(n):
    """Tính giai thừa bằng đệ quy"""
    if n <= 1:  # Base case: điểm dừng
        return 1
    return n * factorial(n - 1)  # Recursive case


print("5! =", factorial(5))  # 120
# Cách tính: 5 * 4 * 3 * 2 * 1 = 120


# ===== Fibonacci =====
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)


def fibonacci(n):
    """Tính số Fibonacci thứ n"""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("F(7) =", fibonacci(7))  # 13
# Dãy: 0, 1, 1, 2, 3, 5, 8, 13


# ===== Đếm ngược =====
def countdown(n):
    """In đếm ngược từ n về 0"""
    if n < 0:  # Base case
        return
    print(n)
    countdown(n - 1)  # Recursive case


print("Đếm ngược từ 5:")
countdown(5)


# ===== Duyệt cấu trúc lồng nhau (nested list) =====
def flatten(nested_list):
    """Làm phẳng list lồng nhau"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            # Đệ quy: gọi flatten cho list con
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


nested = [1, [2, 3], [4, [5, 6]], 7]
print("Flattened:", flatten(nested))  # [1, 2, 3, 4, 5, 6, 7]


# ===== Tổng các chữ số =====
def sum_digits(n):
    """Tính tổng các chữ số của n"""
    if n < 10:  # Base case: 1 chữ số
        return n
    return n % 10 + sum_digits(n // 10)  # Chữ số cuối + phần còn lại


print("Tổng chữ số 12345:", sum_digits(12345))  # 1+2+3+4+5 = 15


# ===== Đệ quy vs Vòng lặp =====
# Tổng từ 1 đến n


def sum_recursive(n):
    if n <= 0:
        return 0
    return n + sum_recursive(n - 1)


def sum_iterative(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


print("Sum recursive(10):", sum_recursive(10))  # 55
print("Sum iterative(10):", sum_iterative(10))  # 55


# ===== GIỚI HẠN ĐỆ QUY =====
# Python giới hạn độ sâu đệ quy (mặc định ~1000)
import sys

print("Recursion limit:", sys.getrecursionlimit())  # Thường là 1000

# Ví dụ vượt giới hạn (bỏ comment để test):
# def infinite_recursion():
#     return infinite_recursion()
# infinite_recursion()  # RecursionError


# ===== KHI NÀO DÙNG ĐỆ QUY =====
# NÊN:
# - Cấu trúc đệ quy tự nhiên (cây, thư mục, JSON lồng...)
# - Code ngắn gọn, dễ đọc hơn vòng lặp
# - Bài toán chia để trị (divide and conquer)

# KHÔNG NÊN:
# - Đệ quy quá sâu -> RecursionError
# - Hiệu năng kém (Python không tối ưu tail recursion)
# - Có giải pháp vòng lặp đơn giản hơn

# ============================================
# 7. HIGHER-ORDER FUNCTIONS - HÀM BẬC CAO
# ============================================
# Hàm bậc cao là hàm: nhận hàm khác làm tham số HOẶC trả về 1 hàm

# ===== MAP: áp dụng hàm lên từng phần tử =====
# map(function, iterable) -> iterator
numbers = [1, 2, 3, 4, 5]

# Nhân đôi mỗi số
doubled = list(map(lambda x: x * 2, numbers))
print("Doubled:", doubled)  # [2, 4, 6, 8, 10]

# Chuyển sang chuỗi
strings = list(map(str, numbers))
print("Strings:", strings)  # ['1', '2', '3', '4', '5']

# Ép kiểu
str_nums = ["10", "20", "30"]
int_nums = list(map(int, str_nums))
print("Ints:", int_nums)  # [10, 20, 30]


# ===== FILTER: lọc phần tử theo điều kiện =====
# filter(function, iterable) -> iterator
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Lọc số chẵn
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Số chẵn:", evens)  # [2, 4, 6, 8, 10]

# Lọc số > 5
big = list(filter(lambda x: x > 5, numbers))
print("Lớn hơn 5:", big)  # [6, 7, 8, 9, 10]

# Lọc chuỗi không rỗng
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))  # None -> tự lọc falsy
print("Không rỗng:", non_empty)  # ['hello', 'world', 'python']


# ===== REDUCE: gộp dần các phần tử (từ functools) =====
from functools import reduce

# reduce(function, iterable, [initial])
numbers = [1, 2, 3, 4, 5]

# Tính tổng: ((((1+2)+3)+4)+5)
total = reduce(lambda acc, x: acc + x, numbers)
print("Tổng:", total)  # 15

# Tính tích (giai thừa 5)
factorial = reduce(lambda acc, x: acc * x, numbers)
print("5! =", factorial)  # 120

# Tìm max
maximum = reduce(lambda a, b: a if a > b else b, numbers)
print("Max:", maximum)  # 5

# reduce với initial value
total_with_init = reduce(lambda acc, x: acc + x, numbers, 10)
print("Tổng + 10:", total_with_init)  # 25


# ===== Hàm nhận hàm khác làm tham số =====
def apply(func, value):
    """Gọi func(value) và trả về kết quả"""
    return func(value)


print("apply(pow, 5):", apply(lambda x: x ** 2, 5))  # 25
print("apply(str.upper, 'hi'):", apply(str.upper, "hi"))  # "HI"


# ===== Hàm trả về hàm (Closure) =====
def multiplier(n):
    """Trả về hàm nhân với n"""
    return lambda x: x * n  # Closure: nhớ giá trị n


double = multiplier(2)
triple = multiplier(3)
print("Double 10:", double(10))  # 20
print("Triple 10:", triple(10))  # 30


# ===== Decorator với hàm (giới thiệu nhẹ) =====
def uppercase_decorator(func):
    """Nhận hàm, trả về hàm đã được 'bọc'"""
    def wrapper():
        result = func()
        return result.upper()

    return wrapper


def hello():
    return "hello world"


decorated_hello = uppercase_decorator(hello)
print("Decorated:", decorated_hello())  # "HELLO WORLD"


# ===== List comprehension thay cho map/filter =====
# Pythonic: thường dùng list comprehension hơn map/filter
numbers = [1, 2, 3, 4, 5]

# Thay map: [func(x) for x in iterable]
doubled_lc = [x * 2 for x in numbers]
print("LC doubled:", doubled_lc)

# Thay filter: [x for x in iterable if condition]
evens_lc = [x for x in numbers if x % 2 == 0]
print("LC evens:", evens_lc)

# Không có reduce equivalent bằng comprehension

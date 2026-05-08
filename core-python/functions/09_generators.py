# Generator là hàm dùng yield thay vì return
# yield: trả về giá trị và TẠM DỪNG hàm, lần gọi sau TIẾP TỤC từ điểm dừng
# Generator tiết kiệm bộ nhớ vì sinh từng giá trị, không lưu cả list

# ===== Generator cơ bản =====
def count_up_to(n):
    """Generator đếm từ 1 đến n"""
    i = 1
    while i <= n:
        yield i  # Trả về i và tạm dừng
        i += 1


# Gọi generator -> trả về generator object
gen = count_up_to(5)
print(type(gen))  # <class 'generator'>

# Duyệt generator bằng next()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 4
print(next(gen))  # 5
# print(next(gen))  # StopIteration: hết giá trị


# ===== Generator trong vòng lặp for =====
# For tự động gọi next() và bắt StopIteration
for num in count_up_to(3):
    print("Đếm:", num)


# ===== Generator vs List (so sánh bộ nhớ) =====
import sys

# List: lưu tất cả giá trị trong bộ nhớ
list_data = [x for x in range(1000)]
print("List size:", sys.getsizeof(list_data))  # ~8KB cho 1000 phần tử

# Generator: chỉ lưu trạng thái hiện tại
gen_data = (x for x in range(1000))  # () thay vì [] -> generator expression
print("Generator size:", sys.getsizeof(gen_data))  # ~200 bytes


# ===== Generator vô hạn =====
def infinite_counter():
    """Đếm mãi mãi"""
    n = 0
    while True:
        yield n
        n += 1


gen = infinite_counter()
print("Vô hạn:", next(gen))  # 0
print("Vô hạn:", next(gen))  # 1
print("Vô hạn:", next(gen))  # 2
# Có thể gọi mãi mãi, mỗi lần chỉ sinh 1 giá trị


# ===== Generator Expression (tương tự list comprehension) =====
# Dùng () thay vì []
# List comprehension: [expr for x in iterable]
# Generator expression: (expr for x in iterable)

squares = (x * x for x in range(5))
print("Squares generator:", list(squares))  # [0, 1, 4, 9, 16]

# Generator expression có thể truyền trực tiếp vào hàm
total = sum(x * x for x in range(5))  # Không cần ()
print("Sum of squares:", total)  # 30

# Lọc với generator expression
evens = (x for x in range(10) if x % 2 == 0)
print("Evens:", list(evens))  # [0, 2, 4, 6, 8]


# ===== yield from: ủy quyền cho generator khác =====
def gen_range(start, end):
    for i in range(start, end):
        yield i


def combined():
    yield from gen_range(0, 3)  # yield từng giá trị từ gen_range
    yield from gen_range(10, 13)


print("Combined:", list(combined()))  # [0, 1, 2, 10, 11, 12]


# ===== Generator có thể nhận giá trị từ bên ngoài (send) =====
def accumulator():
    total = 0
    while True:
        value = yield total  # Nhận giá trị từ send(), trả về total
        if value is not None:
            total += value


acc = accumulator()
print("Start:", next(acc))  # 0 - khởi động generator
print("+10:", acc.send(10))  # Gửi 10 -> total = 10
print("+20:", acc.send(20))  # Gửi 20 -> total = 30
print("+5:", acc.send(5))  # Gửi 5 -> total = 35


# ===== Generator pipeline (chuỗi xử lý dữ liệu) =====
def read_numbers():
    """Step 1: sinh số"""
    for i in range(1, 11):
        yield i


def filter_even(numbers):
    """Step 2: lọc số chẵn"""
    for n in numbers:
        if n % 2 == 0:
            yield n


def square_numbers(numbers):
    """Step 3: bình phương"""
    for n in numbers:
        yield n * n


# Chuỗi pipeline: read -> filter -> square
pipeline = square_numbers(filter_even(read_numbers()))
print("Pipeline result:", list(pipeline))  # [4, 16, 36, 64, 100]

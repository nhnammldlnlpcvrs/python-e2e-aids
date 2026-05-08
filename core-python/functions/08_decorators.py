# ============================================
# 8. DECORATORS - TRANG TRÍ HÀM
# ============================================
# Decorator là hàm nhận vào 1 hàm, trả về 1 hàm mới
# Dùng để thêm tính năng mà không sửa code gốc
# Cú pháp: @decorator_name đặt trên def

# ===== Decorator cơ bản =====
def my_decorator(func):
    """Wrapper pattern: bọc hàm gốc bằng code mới"""

    def wrapper():
        print(">>> Trước khi gọi hàm")
        func()  # Gọi hàm gốc
        print(">>> Sau khi gọi hàm")

    return wrapper


@my_decorator  # Tương đương: say_hello = my_decorator(say_hello)
def say_hello():
    print("Xin chào!")


say_hello()
# Output:
# >>> Trước khi gọi hàm
# Xin chào!
# >>> Sau khi gọi hàm


# ===== Decorator với tham số của hàm gốc =====
# Dùng *args, **kwargs để decorator hoạt động với mọi hàm
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Gọi {func.__name__} với args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Kết quả: {result}")
        return result

    return wrapper


@log_call
def add(a, b):
    return a + b


@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


add(5, 3)
greet("Nam", greeting="Xin chào")


# ===== Decorator đo thời gian chạy =====
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} chạy trong {end - start:.4f}s")
        return result

    return wrapper


@timer
def slow_function():
    time.sleep(0.5)  # Giả lập chạy chậm
    return "Done"


slow_function()


# ===== Decorator với tham số riêng (Decorator Factory) =====
# 3 lớp: factory nhận param -> decorator nhận func -> wrapper nhận args
def repeat(n):
    """Factory: trả về decorator lặp n lần"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator


@repeat(3)  # Gọi say_name 3 lần
def say_name():
    print("Nam")


say_name()  # In "Nam" 3 lần


# ===== Giữ metadata của hàm gốc (__name__, __doc__) =====
from functools import wraps


def good_decorator(func):
    @wraps(func)  # Giữ lại metadata của func
    def wrapper(*args, **kwargs):
        """Đây là wrapper"""
        return func(*args, **kwargs)

    return wrapper


@good_decorator
def important_function():
    """Đây là hàm quan trọng"""
    pass


print("__name__:", important_function.__name__)  # important_function
print("__doc__:", important_function.__doc__)  # Đây là hàm quan trọng
# Không có @wraps: __name__ sẽ là "wrapper", __doc__ sẽ là "Đây là wrapper"


# ===== Nhiều decorator chồng nhau =====
# Thứ tự: decorator gần def nhất chạy đầu tiên
@log_call
@timer
def compute():
    return sum(range(1000000))


result = compute()
# Thứ tự áp dụng: compute -> timer(compute) -> log_call(timer(compute))
# Khi gọi: log_call -> timer -> compute thực sự -> timer -> log_call


# ===== Class-based decorator (nâng cao) =====
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"Đã gọi {self.count} lần")
        return self.func(*args, **kwargs)


@CountCalls
def hello():
    print("Hello!")


hello()
hello()
hello()

# Exception Handling - Xử lý lỗi

# try-except cơ bản
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Không thể chia cho 0!")

# Bắt nhiều loại lỗi
try:
    num = int("abc")
except (ValueError, TypeError) as e:
    print(f"Lỗi: {e}")

# else: chạy khi không có lỗi
try:
    num = int("123")
except ValueError:
    print("Không phải số!")
else:
    print("Thành công:", num)

# finally: luôn chạy dù có lỗi hay không
try:
    num = int("abc")
except ValueError:
    print("Lỗi rồi!")
finally:
    print("Khối finally luôn được chạy")

# Tự raise lỗi
def divide(a, b):
    if b == 0:
        raise ValueError("b không thể bằng 0")
    return a / b

try:
    print(divide(10, 0))
except ValueError as e:
    print(f"Bắt được lỗi: {e}")

# --- Tham số bắt buộc (Positional) ---
def greet(name, age):
    """name và age là tham số bắt buộc"""
    print(f"Tên: {name}, Tuổi: {age}")


greet("Nam", 18)  # Truyền theo thứ tự
# greet("Nam")  # ERROR: thiếu 1 tham số age


# --- Default Parameters (Tham số mặc định) ---
def power(base, exp=2):
    """exp có giá trị mặc định = 2, nếu không truyền thì lấy mặc định"""
    return base ** exp


print("3^2 =", power(3))  # Chỉ truyền base, exp lấy mặc định = 2
print("3^3 =", power(3, 3))  # Truyền cả 2, ghi đè exp
print("5^2 =", power(5))  # base=5, exp mặc định = 2


# --- Keyword Arguments (Truyền tham số theo tên) ---
def describe(name, age, city="Hà Nội"):
    print(f"{name}, {age} tuổi, sống ở {city}")


# Truyền theo thứ tự (positional)
describe("Nam", 18)

# Truyền theo tên (keyword) - không cần theo thứ tự
describe(age=20, city="HCM", name="An")

# Kết hợp cả 2: positional trước, keyword sau
describe("Linh", age=22)
# describe(name="Linh", 22)  # ERROR: keyword trước, positional sau


# --- Default Parameter với mutable object (LƯU Ý QUAN TRỌNG) ---
# DEFAULT CHỈ ĐƯỢC TẠO 1 LẦN khi định nghĩa hàm, không phải mỗi lần gọi
def bad_append(item, my_list=[]):
    """Lỗi: list mặc định dùng chung giữa các lần gọi"""
    my_list.append(item)
    return my_list


print("bad_append lần 1:", bad_append(1))  # [1]
print("bad_append lần 2:", bad_append(2))  # [1, 2] -> Oops! List cũ vẫn còn dữ liệu


# Cách đúng: dùng None làm default
def good_append(item, my_list=None):
    if my_list is None:
        my_list = []  # Tạo list mới mỗi lần gọi
    my_list.append(item)
    return my_list


print("good_append lần 1:", good_append(1))  # [1]
print("good_append lần 2:", good_append(2))  # [2] -> Đúng


# --- Keyword-Only Arguments (Python 3.8+, dùng *) ---
# Sau dấu *, tất cả tham số bắt buộc phải truyền theo keyword
def register(username, *, email, phone):
    """email và phone bắt buộc truyền theo keyword"""
    print(f"User: {username}, Email: {email}, Phone: {phone}")


register("nam123", email="nam@mail.com", phone="012345")
# register("nam123", "nam@mail.com", "012345")  # ERROR


# --- Positional-Only Arguments (Python 3.8+, dùng /) ---
# Trước dấu /, tất cả tham số chỉ được truyền theo vị trí
def divide(a, b, /):
    """a và b chỉ nhận theo vị trí, không dùng keyword được"""
    return a / b


print("10/2 =", divide(10, 2))  # OK
# print(divide(a=10, b=2))  # ERROR


# --- Kết hợp / và * ---
def mixed(a, b, /, c, *, d):
    """a,b: positional-only | c: positional hoặc keyword | d: keyword-only"""
    print(f"a={a}, b={b}, c={c}, d={d}")


mixed(1, 2, 3, d=4)  # OK
mixed(1, 2, c=3, d=4)  # Cũng OK

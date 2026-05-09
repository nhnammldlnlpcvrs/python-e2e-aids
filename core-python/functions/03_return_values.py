# --- return: trả về giá trị và kết thúc hàm ---
def add(a, b):
    return a + b  # Trả về tổng, hàm kết thúc tại đây


result = add(5, 3)
print("5 + 3 =", result)


# --- return không có giá trị -> trả về None ---
def do_nothing():
    return  # Tương đương return None


print(do_nothing())  # None


# --- Không có return -> cũng trả về None ---
def no_return():
    _ = 1 + 1  # Code chạy nhưng không return gì cả


print(no_return())  # None


# --- Return nhiều giá trị (thực chất là tuple) ---
def get_user():
    name = "Nam"
    age = 18
    job = "Dev"
    return name, age, job  # Python tự động gói thành tuple


result = get_user()
print(result)  # ('Nam', 18, 'Dev') -> tuple
print(type(result))  # <class 'tuple'>


# Unpacking (giải nén) khi nhận
name, age, job = get_user()
print(f"Tên: {name}, Tuổi: {age}, Job: {job}")


# Chỉ lấy 1 giá trị, dùng _ bỏ qua các giá trị khác
name, _, _ = get_user()
print("Tên:", name)


# --- Return sớm (early return) ---
def check_age(age):
    """Kiểm tra tuổi, dùng return sớm để thoát"""
    if age < 0:
        return "Tuổi không hợp lệ"  # Thoát sớm
    if age < 18:
        return "Trẻ em"             # Thoát sớm
    if age < 60:
        return "Người lớn"          # Thoát sớm
    return "Người già"              # Default


print(check_age(-5))  # Tuổi không hợp lệ
print(check_age(10))  # Trẻ em
print(check_age(30))  # Người lớn
print(check_age(70))  # Người già


# --- Return trong vòng lặp ---
def find_first_even(numbers):
    """Tìm số chẵn đầu tiên trong list"""
    for n in numbers:
        if n % 2 == 0:
            return n  # Thoát hàm ngay khi tìm thấy
    return None  # Không tìm thấy


print("Số chẵn đầu tiên:", find_first_even([1, 3, 4, 7, 8]))  # 4
print("Số chẵn đầu tiên:", find_first_even([1, 3, 5]))  # None


# --- Hàm trả về hàm (function factory) ---
def make_multiplier(n):
    """Trả về một hàm mới nhân với n"""
    def multiplier(x):
        return x * n

    return multiplier  # Trả về function, không gọi


double = make_multiplier(2)
triple = make_multiplier(3)
print("Double 5:", double(5))  # 10
print("Triple 5:", triple(5))  # 15


# --- Type hints cho return value (Python 3.5+) ---
def multiply(a: int, b: int) -> int:
    """a:int, b:int -> kiểu trả về int"""
    return a * b


print("6 * 7 =", multiply(6, 7))
# Type hints chỉ là gợi ý, Python không ép kiểu
print(multiply("ha", 3))  # Vẫn chạy: "hahaha"

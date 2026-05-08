# --- *args: nhận nhiều tham số không tên (positional) ---
# *args gói tất cả tham số thừa thành 1 tuple
def sum_all(*args):
    """Nhận bao nhiêu số cũng được"""
    print(f"args type: {type(args)}")  # <class 'tuple'>
    print(f"args = {args}")
    return sum(args)


print("Tổng:", sum_all(1, 2, 3, 4, 5))
print("Tổng 2 số:", sum_all(10, 20))
print("Tổng 0 số:", sum_all())  # args = ()


# --- *args kết hợp tham số bình thường ---
def describe_person(name, *hobbies):
    """name là bắt buộc, hobbies nhận tùy ý"""
    print(f"Tên: {name}")
    if hobbies:
        print(f"Sở thích: {', '.join(hobbies)}")
    else:
        print("Không có sở thích")


describe_person("Nam", "code", "game", "music")
describe_person("An")  # hobbies = ()


# --- **kwargs: nhận nhiều tham số có tên (keyword) ---
# **kwargs gói tất cả keyword arguments thành 1 dict
def show_config(**kwargs):
    """Nhận bao nhiêu keyword argument cũng được"""
    print(f"kwargs type: {type(kwargs)}")  # <class 'dict'>
    print(f"kwargs = {kwargs}")
    for key, value in kwargs.items():
        print(f"  {key} = {value}")


show_config(host="localhost", port=8080, debug=True)


# --- **kwargs kết hợp tham số bình thường ---
def create_user(username, **details):
    """username bắt buộc, các thông tin khác tùy ý"""
    user = {"username": username, **details}
    # **details unpack dict vào dict mới
    print(f"User: {user}")


create_user("nam123", age=18, city="HN", job="Dev")


# --- Kết hợp *args và **kwargs ---
# Thứ tự: positional -> *args -> keyword -> **kwargs
def mega_function(a, b, *args, default=True, **kwargs):
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"*args = {args}")
    print(f"default = {default}")
    print(f"**kwargs = {kwargs}")


mega_function(1, 2, 3, 4, 5, default=False, x=10, y=20)


# --- Unpacking: truyền list/tuple/dict vào hàm ---
# Dùng * để unpack list/tuple thành positional args
def multiply(a, b, c):
    return a * b * c


numbers = [2, 3, 4]
print("*numbers:", multiply(*numbers))  # 2*3*4 = 24

# Dùng ** để unpack dict thành keyword args
params = {"a": 2, "b": 3, "c": 4}
print("**params:", multiply(**params))  # 2*3*4 = 24


# --- *args với *unpacking trong thực tế ---
def log(message, *tags):
    """Ghi log với tags tùy chọn"""
    tag_str = " | ".join(tags) if tags else "INFO"
    print(f"[{tag_str}] {message}")


log("Server started")
log("Error occurred", "ERROR", "CRITICAL")
log("User login", "AUTH", "SUCCESS")

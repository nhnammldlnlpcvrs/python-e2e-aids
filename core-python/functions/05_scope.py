# ============================================
# 5. SCOPE - PHẠM VI BIẾN
# ============================================
# Python có quy tắc LEGB: Local -> Enclosing -> Global -> Built-in

# ===== GLOBAL SCOPE =====
# Biến ngoài hàm -> global scope
x = "global"


def show_global():
    print("Bên trong hàm:", x)  # Đọc được biến global


show_global()
print("Bên ngoài hàm:", x)


# ===== LOCAL SCOPE =====
# Biến trong hàm -> local scope, không truy cập từ ngoài
def create_local():
    local_var = "Tôi là local"
    print("Trong hàm:", local_var)


create_local()
# print(local_var)  # ERROR: NameError, không tồn tại bên ngoài


# ===== Biến local CHE biến global =====
x = "global"


def shadow():
    x = "local"  # Tạo biến local MỚI, không ảnh hưởng global
    print("Trong shadow():", x)


shadow()
print("Ngoài shadow():", x)  # Vẫn là "global"


# ===== global keyword: ghi vào biến global từ trong hàm =====
counter = 0


def increment():
    global counter  # Báo cho Python: "counter" là biến global
    counter += 1  # Bây giờ mới ghi được


print("Trước:", counter)
increment()
increment()
print("Sau:", counter)  # 2


# ===== Không có global -> sẽ bị lỗi khi gán =====
total = 100


def try_modify():
    # print(total)  # Uncomment sẽ lỗi: UnboundLocalError
    # Lý do: Python thấy "total =" ở dưới -> coi total là local
    total = 200  # Tạo local mới
    print("Local total:", total)


try_modify()
print("Global total:", total)  # Vẫn 100


# ===== ENCLOSING SCOPE (Hàm lồng nhau) =====
def outer():
    outer_var = "outer"

    def inner():
        print("inner thấy:", outer_var)  # Đọc được biến từ outer

    inner()
    # print(outer_var)  # Không thấy, outer_var là local của outer


outer()


# ===== nonlocal keyword: ghi vào biến của enclosing function =====
def counter_factory():
    count = 0  # Biến trong enclosing scope

    def increment():
        nonlocal count  # Báo: dùng count từ outer, không tạo local mới
        count += 1
        return count

    return increment  # Trả về hàm inner


my_counter = counter_factory()
print("Đếm:", my_counter())  # 1
print("Đếm:", my_counter())  # 2
print("Đếm:", my_counter())  # 3


# ===== BUILT-IN SCOPE =====
# Python có sẵn các hàm như print, len, sum...
print("Built-in len():", len("hello"))


# Cẩn thận: không nên đặt tên biến trùng built-in
# len = 5  # BAD! Ghi đè built-in len
# print(len("hello"))  # ERROR: int không gọi được


# ===== Quy tắc LEGB: Python tìm biến theo thứ tự =====
# Local -> Enclosing -> Global -> Built-in
message = "Global"


def outer():
    message = "Enclosing"

    def inner():
        print("Tìm thấy:", message)  # Tìm từ trong ra ngoài -> "Enclosing"

    inner()


outer()

# def function_name():
#     """docstring (mô tả hàm)"""
#     # thân hàm
#     # ...


def greet():
    """Hàm đơn giản in ra lời chào"""
    print("Xin chào!")


greet()  # Gọi hàm: tên_hàm()


# --- Docstring: chuỗi mô tả hàm (nằm ngay sau def) ---
# Truy cập docstring qua __doc__
print(greet.__doc__)  # In ra docstring của hàm


# --- Hàm không có docstring ---
def say_hello():
    print("Hello!")


say_hello()


# --- Hàm với pass (placeholder) ---
def future_function():
    pass  # pass = "chưa làm gì cả", giữ chỗ


future_function()  # Không làm gì


# --- Gọi hàm nhiều lần ---
def count():
    print("1... 2... 3...")


count()
count()
count()


# --- Hàm bên trong script: định nghĩa trước khi gọi ---
# Python chạy code từ trên xuống, nên phải def trước khi gọi
def top_function():
    print("Được định nghĩa trước")


top_function()  # OK


# bottom_function()  # ERROR! Chưa được định nghĩa

def bottom_function():
    print("Định nghĩa sau")


bottom_function()  # OK, đã được định nghĩa rồi


# --- Hàm có thể được gán vào biến ---
def original():
    print("Hàm gốc")


alias = original  # Gán hàm vào biến (không gọi hàm, chỉ tham chiếu)
alias()  # Gọi qua alias -> "Hàm gốc"
print(type(alias))  # <class 'function'>
print(callable(alias))  # True - có thể gọi được

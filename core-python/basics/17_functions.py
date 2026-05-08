# Functions - Hàm trong Python

# Hàm cơ bản
def greet():
    print("Xin chào!")

greet()

# Hàm có tham số
def greet_name(name):
    print(f"Xin chào, {name}!")

greet_name("Nam")

# Hàm có giá trị trả về
def add(a, b):
    return a + b

result = add(3, 5)
print("3 + 5 =", result)

# Tham số mặc định
def power(base, exp=2):
    return base ** exp

print("3^2 =", power(3))
print("3^3 =", power(3, 3))

# Keyword arguments
def describe(name, age, city):
    print(f"{name}, {age} tuổi, sống ở {city}")

describe(age=18, city="Hà Nội", name="Nam")

# *args: nhận nhiều tham số không tên
def sum_all(*args):
    return sum(args)

print("Tổng:", sum_all(1, 2, 3, 4, 5))

# **kwargs: nhận nhiều tham số có tên
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_info(name="Nam", age=18, job="Dev")

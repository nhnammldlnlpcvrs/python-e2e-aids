# ============================================
# 2. ATTRIBUTES & METHODS - THUỘC TÍNH VÀ PHƯƠNG THỨC
# ============================================

# ===== 1. INSTANCE ATTRIBUTES: mỗi object có riêng =====
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance attribute
        self.breed = breed  # Instance attribute


d1 = Dog("Milo", "Golden")
d2 = Dog("Max", "Husky")
print(f"{d1.name} là {d1.breed}")
print(f"{d2.name} là {d2.breed}")


# ===== 2. CLASS ATTRIBUTES: dùng chung cho cả class =====
class Dog:
    species = "Canine"  # Class attribute
    count = 0  # Đếm số lượng Dog

    def __init__(self, name):
        self.name = name  # Instance attribute
        Dog.count += 1  # Tăng biến class


d1 = Dog("Milo")
d2 = Dog("Max")
print("Species:", Dog.species)  # Truy cập qua class
print("Species:", d1.species)  # Truy cập qua instance (đọc)
print("Tổng số chó:", Dog.count)  # 2


# CẢNH BÁO: gán qua instance TẠO instance attribute mới, không sửa class attribute
d1.species = "Feline"  # Tạo instance attribute "species" cho d1
print("d1.species:", d1.species)  # "Feline" (instance attribute che class attribute)
print("d2.species:", d2.species)  # "Canine" (vẫn đọc từ class)
print("Dog.species:", Dog.species)  # "Canine" (class attribute không đổi)


# ===== 3. INSTANCE METHODS: method thông thường =====
# Dùng self. Truy cập cả instance và class attributes.
class Calculator:
    factor = 10  # Class attribute

    def __init__(self, value):
        self.value = value  # Instance attribute

    def compute(self):
        """Instance method: có self"""
        return self.value * self.factor  # Dùng được cả 2


c = Calculator(5)
print("Compute:", c.compute())  # 50


# ===== 4. @classmethod: method của class, không cần instance =====
# Dùng cls thay vì self. Thường dùng làm factory method.
class Student:
    school = "ABC University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_school(cls, new_school):
        """Thay đổi class attribute"""
        cls.school = new_school

    @classmethod
    def from_string(cls, data):
        """Factory method: tạo Student từ chuỗi "name,age" """
        name, age = data.split(",")
        return cls(name, int(age))  # cls(...) = Student(...)


# Gọi classmethod qua class (không cần instance)
Student.change_school("XYZ University")
print("School:", Student.school)

# Factory method
s = Student.from_string("Nam,18")
print(f"Name: {s.name}, Age: {s.age}")


# ===== 5. @staticmethod: method độc lập, không dùng self/cls =====
# Giống hàm bình thường, nhưng đặt trong class để tổ chức code
class Math:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0

    @staticmethod
    def circle_area(radius):
        import math
        return math.pi * radius ** 2


# Gọi không cần instance
print("Add:", Math.add(5, 3))
print("Is 7 even?", Math.is_even(7))
print("Circle area r=10:", Math.circle_area(10))


# ===== SO SÁNH 3 LOẠI METHOD =====
class Demo:
    class_var = "class"

    def instance_method(self):
        """Có self -> truy cập được instance + class"""
        return f"instance_method: self={self}"

    @classmethod
    def class_method(cls):
        """Có cls -> truy cập được class, không cần instance"""
        return f"class_method: cls={cls}"

    @staticmethod
    def static_method():
        """Không self, không cls -> độc lập hoàn toàn"""
        return "static_method: không có self/cls"


d = Demo()
print(d.instance_method())
print(Demo.class_method())
print(Demo.static_method())

# Tóm tắt:
# instance method: method bình thường, có self, gọi qua object
# classmethod:    có cls, gọi qua class (hoặc object), dùng làm factory
# staticmethod:   không self/cls, gọi qua class, chỉ là hàm trong class

# ============================================
# 1. CLASS BASICS - LỚP VÀ ĐỐI TƯỢNG CƠ BẢN
# ============================================
# Class = bản thiết kế (blueprint). Object = sản phẩm từ bản thiết kế đó.
# Class mô tả dữ liệu + hành vi. Object là 1 instance cụ thể của class.

# --- Định nghĩa class cơ bản ---
# class ClassName:
#     """docstring"""
#     thuộc_tính = giá_trị
#     def phương_thức(self):
#         ...


class Student:
    """Lớp mô tả sinh viên"""

    # Class attribute: dùng chung cho tất cả instance
    school = "ABC University"

    # __init__: phương thức khởi tạo (constructor)
    def __init__(self, name, age, grade):
        """Tự động gọi khi tạo object mới"""
        # Instance attributes: mỗi object có riêng
        self.name = name
        self.age = age
        self.grade = grade

    # Instance method: phương thức của object
    def introduce(self):
        """self = tham chiếu đến chính object đang gọi"""
        return f"Tôi là {self.name}, {self.age} tuổi, lớp {self.grade}"

    def is_passed(self):
        """Kiểm tra đậu/rớt"""
        return self.grade >= 5.0


# Tạo object (instance) từ class
s1 = Student("Nam", 18, 8.5)
s2 = Student("An", 19, 4.0)

# Truy cập attributes
print("Tên:", s1.name)  # Instance attribute
print("Tên:", s2.name)
print("Trường:", s1.school)  # Class attribute (dùng chung)
print("Trường:", s2.school)  # Cùng giá trị

# Gọi methods
print(s1.introduce())
print(s2.introduce())
print("Nam đậu?", s1.is_passed())
print("An đậu?", s2.is_passed())


# --- self là gì? ---
# Python tự động truyền object vào làm tham số đầu tiên
# s1.introduce() -> Python gọi Student.introduce(s1)


class Demo:
    def show_id(self):
        print(f"id của self: {id(self)}")


d = Demo()
print(f"id của d:    {id(d)}")  # Giống nhau: self chính là object
d.show_id()


# --- Class không có __init__ ---
# Python tự tạo constructor mặc định (không làm gì)
class Empty:
    pass


e = Empty()  # Vẫn tạo được object
e.name = "Thêm thuộc tính sau"  # Python cho phép thêm attribute sau
print(e.name)


# --- isinstance() và type() ---
print("\n--- Kiểm tra kiểu ---")
print(isinstance(s1, Student))  # True - s1 là instance của Student
print(isinstance(s1, object))  # True - mọi class đều kế thừa object
print(type(s1))  # <class '__main__.Student'>
print(type(s1) == Student)  # True


# --- __dict__: xem tất cả attributes của object ---
print("\n__dict__ của s1:")
print(s1.__dict__)  # {'name': 'Nam', 'age': 18, 'grade': 8.5}

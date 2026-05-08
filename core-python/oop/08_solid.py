# ============================================
# 8. SOLID PRINCIPLES - 5 NGUYÊN TẮC SOLID
# ============================================
# SOLID = 5 nguyên tắc thiết kế OOP của Robert C. Martin
# Giúp code dễ bảo trì, dễ mở rộng, dễ test

# ===== S: Single Responsibility (SRP) =====
# Mỗi class CHỈ có 1 lý do để thay đổi = 1 trách nhiệm duy nhất

# BAD: 1 class làm quá nhiều việc
class UserManager_BAD:
    def create_user(self, name, email):
        pass  # Logic tạo user

    def send_email(self, email, content):
        pass  # Logic gửi email -> KHÔNG phải việc của UserManager!

    def log_to_file(self, message):
        pass  # Logic ghi log -> CŨNG KHÔNG phải!


# GOOD: Tách thành các class riêng, mỗi class 1 việc
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class UserRepository:
    """Chỉ lo lưu/xóa/tìm user"""
    def save(self, user):
        print(f"Lưu user {user.name} vào DB")

    def delete(self, user):
        print(f"Xóa user {user.name}")


class EmailService:
    """Chỉ lo gửi email"""
    def send_welcome(self, user):
        print(f"Gửi email welcome đến {user.email}")


class Logger:
    """Chỉ lo ghi log"""
    def log(self, message):
        print(f"[LOG] {message}")


# Sử dụng
user = User("Nam", "nam@mail.com")
repo = UserRepository()
email_svc = EmailService()
logger = Logger()

repo.save(user)
email_svc.send_welcome(user)
logger.log("User created successfully")


# ===== O: Open/Closed (OCP) =====
# MỞ để mở rộng (thêm tính năng), ĐÓNG để sửa đổi (không sửa code cũ)

# BAD: mỗi khi thêm loại discount mới -> phải sửa class
class DiscountCalculator_BAD:
    def calculate(self, amount, discount_type):
        if discount_type == "percent":
            return amount * 0.9
        elif discount_type == "fixed":
            return amount - 10
        elif discount_type == "vip":  # Phải SỬA code cũ để thêm!
            return amount * 0.5
        # Thêm loại mới = thêm elif = sửa code cũ = nguy cơ bug


# GOOD: dùng kế thừa + polymorphism
from abc import ABC, abstractmethod


class Discount(ABC):
    @abstractmethod
    def apply(self, amount):
        pass


class PercentDiscount(Discount):
    def apply(self, amount):
        return amount * 0.9


class FixedDiscount(Discount):
    def apply(self, amount):
        return amount - 10


class VIPDiscount(Discount):
    def apply(self, amount):
        return amount * 0.5


class DiscountCalculator:
    """Không cần sửa khi thêm Discount mới"""
    def calculate(self, amount, discount: Discount):
        return discount.apply(amount)


calc = DiscountCalculator()
print(f"Percent: {calc.calculate(100, PercentDiscount())}")  # 90
print(f"VIP: {calc.calculate(100, VIPDiscount())}")  # 50
# Thêm discount mới = tạo class mới, không đụng code cũ!


# ===== L: Liskov Substitution (LSP) =====
# Class con có thể thay thế class cha mà không làm hỏng chương trình

# BAD: Square không thể thay thế Rectangle
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, w):
        self.width = w

    def set_height(self, h):
        self.height = h

    def area(self):
        return self.width * self.height


class Square_BAD(Rectangle):
    def set_width(self, w):
        self.width = w
        self.height = w  # Square: width = height

    def set_height(self, h):
        self.width = h  # Sửa luôn width -> phá vỡ hành vi Rectangle!
        self.height = h


# Test LSP violation
def resize_rect(rect: Rectangle):
    rect.set_width(5)
    rect.set_height(10)
    # Với Rectangle: area = 5*10 = 50
    # Với Square_BAD: area = 10*10 = 100 -> SAI!
    assert rect.area() == 50, f"LSP violation! Area = {rect.area()}"


# resize_rect(Square_BAD(4))  # AssertionError!


# GOOD: Không dùng kế thừa ở đây, dùng composition hoặc abstract Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class RectangleGood(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class SquareGood(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# ===== I: Interface Segregation (ISP) =====
# Không ép client phụ thuộc vào method nó không dùng
# Tách interface lớn thành nhiều interface nhỏ

# BAD: 1 interface quá to
class Worker_BAD(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


# Robot phải implement eat() và sleep() -> vô nghĩa!
class Robot_BAD(Worker_BAD):
    def work(self):
        return "Robot làm việc"

    def eat(self):
        raise NotImplementedError("Robot không ăn!")  # VI PHẠM ISP

    def sleep(self):
        raise NotImplementedError("Robot không ngủ!")  # VI PHẠM ISP


# GOOD: tách thành interface nhỏ
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


class Human(Workable, Eatable, Sleepable):
    def work(self):
        return "Người làm việc"

    def eat(self):
        return "Người ăn"

    def sleep(self):
        return "Người ngủ"


class Robot(Workable):
    """Robot chỉ implement Workable - không bị ép ăn/ngủ"""
    def work(self):
        return "Robot làm việc"


print(Human().work(), "|", Human().eat())
print(Robot().work())


# ===== D: Dependency Inversion (DIP) =====
# Module cấp cao không nên phụ thuộc vào module cấp thấp
# Cả 2 nên phụ thuộc vào abstraction (interface)

# BAD: class cấp cao phụ thuộc trực tiếp vào class cấp thấp
class MySQLDatabase_BAD:
    def save(self, data):
        print(f"Lưu {data} vào MySQL")


class UserService_BAD:
    def __init__(self):
        self.db = MySQLDatabase_BAD()  # Phụ thuộc CỨNG vào MySQL!

    def create_user(self, name):
        self.db.save({"name": name})


# Muốn đổi sang PostgreSQL? -> phải sửa UserService!


# GOOD: dùng abstraction
class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Lưu {data} vào MySQL")


class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Lưu {data} vào PostgreSQL")


class UserService:
    def __init__(self, db: Database):
        self.db = db  # Phụ thuộc vào ABSTRACTION, không phải concrete class

    def create_user(self, name):
        self.db.save({"name": name})


# Dễ dàng đổi DB
service = UserService(MySQLDatabase())
service.create_user("Nam")  # Lưu vào MySQL

service = UserService(PostgreSQLDatabase())
service.create_user("An")  # Lưu vào PostgreSQL

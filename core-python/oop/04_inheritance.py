# ============================================
# 4. INHERITANCE - KẾ THỪA
# ============================================
# Kế thừa: class con nhận attributes + methods từ class cha
# Mục đích: tái sử dụng code, mở rộng chức năng

# ===== Kế thừa cơ bản =====
class Animal:
    """Class cha (base class / super class)"""

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "... (âm thanh chung)"

    def describe(self):
        return f"Tôi là {self.name}, tôi nói: {self.speak()}"


class Dog(Animal):
    """Class con (derived class / sub class)"""

    def speak(self):
        """Ghi đè (override) method của class cha"""
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


# Dog và Cat kế thừa __init__ và describe từ Animal
dog = Dog("Milo")
cat = Cat("Kitty")
print(dog.describe())  # Tôi là Milo, tôi nói: Woof!
print(cat.describe())  # Tôi là Kitty, tôi nói: Meow!


# ===== super(): gọi method của class cha =====
class Dog(Animal):
    def __init__(self, name, breed):
        """Mở rộng __init__, thêm breed"""
        super().__init__(name)  # Gọi __init__ của Animal
        self.breed = breed  # Thêm attribute mới

    def speak(self):
        return "Woof!"

    def describe(self):
        parent_desc = super().describe()  # Gọi describe của Animal
        return f"{parent_desc}. Giống: {self.breed}"


dog = Dog("Milo", "Golden Retriever")
print(dog.describe())


# ===== isinstance() với class cha =====
print("isinstance(dog, Dog):", isinstance(dog, Dog))  # True
print("isinstance(dog, Animal):", isinstance(dog, Animal))  # True - dog cũng là Animal!
print("isinstance(dog, object):", isinstance(dog, object))  # True - mọi class đều từ object


# ===== ĐA KẾ THỪA (Multiple Inheritance) =====
class Flyer:
    def fly(self):
        return "Đang bay..."

    def move(self):
        return "Bay"


class Swimmer:
    def swim(self):
        return "Đang bơi..."

    def move(self):
        return "Bơi"


class Duck(Flyer, Swimmer):
    """Kế thừa từ cả Flyer và Swimmer"""

    def move(self):
        """Override move để kết hợp cả 2"""
        return "Bay và Bơi"


duck = Duck()
print(duck.fly())  # Từ Flyer
print(duck.swim())  # Từ Swimmer
print(duck.move())  # Override trong Duck


# ===== MRO: Method Resolution Order =====
# Thứ tự Python tìm method khi gọi: Duck -> Flyer -> Swimmer -> object
print("\nMRO của Duck:")
for cls in Duck.__mro__:
    print(f"  {cls.__name__}")
# Duck -> Flyer -> Swimmer -> Animal (hoặc object)


# MRO giúp giải quyết Diamond Problem
class A:
    def method(self):
        return "A"


class B(A):
    def method(self):
        return "B"


class C(A):
    def method(self):
        return "C"


class D(B, C):
    """Diamond: D -> B -> C -> A"""
    pass


d = D()
print("\nDiamond problem:", d.method())  # "B" (theo MRO: B trước C)
print("MRO của D:", [c.__name__ for c in D.__mro__])


# ===== Mixin: kế thừa để THÊM tính năng (không phải "is-a") =====
# Mixin là class nhỏ, độc lập, thêm 1 chức năng cụ thể
class JsonMixin:
    """Mixin: thêm khả năng chuyển thành JSON"""
    import json

    def to_json(self):
        return self.json.dumps(self.__dict__, ensure_ascii=False)


class LogMixin:
    """Mixin: thêm khả năng log"""
    def log(self, message):
        print(f"[LOG][{self.__class__.__name__}] {message}")


class User(JsonMixin, LogMixin):
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save(self):
        self.log(f"Đang lưu user {self.name}")
        # Lưu vào DB...
        return self.to_json()


user = User("Nam", "nam@mail.com")
print(user.to_json())  # Từ JsonMixin
user.log("Test")  # Từ LogMixin
print(user.save())

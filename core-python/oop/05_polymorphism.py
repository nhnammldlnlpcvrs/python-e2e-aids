# ============================================
# 5. POLYMORPHISM - ĐA HÌNH
# ============================================
# Đa hình: code làm việc với interface chung, không cần biết kiểu cụ thể
# Python có 2 kiểu: Duck Typing (chính) và Abstract Base Class

# ===== 1. DUCK TYPING: "If it walks like a duck and quacks like a duck..." =====
# Không quan tâm object thuộc class nào, chỉ cần có method/attribute cần dùng


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Duck:
    def speak(self):
        return "Quack!"


# Hàm này không quan tâm object là Dog, Cat hay Duck
# Chỉ cần object CÓ method speak() là được
def make_sound(animal):
    """Nhận bất kỳ object nào có .speak()"""
    print(animal.speak())


make_sound(Dog())
make_sound(Cat())
make_sound(Duck())


# Duck typing với iteration (mọi object có __iter__ đều dùng được for)
class CountDown:
    """Class này có __iter__ và __next__ -> dùng được trong for"""

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val


# Dùng trong for - Python chỉ cần __iter__ và __next__, không cần biết class
print("Đếm ngược:")
for n in CountDown(3):
    print(n)


# ===== 2. ABSTRACT BASE CLASS (ABC) =====
# Dùng ABC khi muốn ÉP BUỘC class con phải implement method nào đó
# Không thể tạo instance của ABC trực tiếp
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract class: không thể tạo Shape() trực tiếp"""

    @abstractmethod
    def area(self):
        """Class con BẮT BUỘC phải override method này"""
        pass

    @abstractmethod
    def perimeter(self):
        pass

    # Method thường vẫn có thể có body trong ABC
    def describe(self):
        return f"Diện tích: {self.area()}, Chu vi: {self.perimeter()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

    def perimeter(self):
        import math
        return 2 * math.pi * self.radius


# shape = Shape()  # TypeError: Can't instantiate abstract class
rect = Rectangle(5, 3)
circ = Circle(4)

# Code làm việc qua interface chung Shape
shapes = [rect, circ]
for shape in shapes:
    print(shape.describe())


# Nếu quên implement abstract method -> lỗi ngay khi tạo class
# class IncompleteShape(Shape):
#     pass
# x = IncompleteShape()  # TypeError


# ===== 3. Protocol (Python 3.8+): ABC nhẹ hơn =====
from typing import Protocol


class Drawable(Protocol):
    """Protocol: quy định interface, nhưng không cần kế thừa"""

    def draw(self) -> str:
        ...


class Button:
    def draw(self) -> str:
        return "[Button]"


class TextBox:
    def draw(self) -> str:
        return "[TextBox]"


# render() nhận mọi object có method draw()
# Không cần Button/TextBox kế thừa Drawable
def render(element: Drawable):
    print(f"Rendering: {element.draw()}")


render(Button())  # OK - Button có draw()
render(TextBox())  # OK - TextBox có draw()


# ===== 4. isinstance() + issubclass() =====
print("\nKiểm tra quan hệ:")
print("isinstance(rect, Rectangle):", isinstance(rect, Rectangle))
print("isinstance(rect, Shape):", isinstance(rect, Shape))
print("issubclass(Rectangle, Shape):", issubclass(Rectangle, Shape))
print("issubclass(Circle, Shape):", issubclass(Circle, Shape))

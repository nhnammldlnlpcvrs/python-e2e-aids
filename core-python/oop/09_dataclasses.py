# ============================================
# 9. DATACLASSES - LỚP DỮ LIỆU (Python 3.7+)
# ============================================
# @dataclass tự động tạo __init__, __repr__, __eq__ và nhiều thứ khác
# Giảm boilerplate code khi class chủ yếu để chứa dữ liệu

from dataclasses import dataclass, field, asdict, astuple

# ===== TRƯỚC KHI CÓ dataclass (code nhiều) =====
class PersonOld:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"PersonOld(name={self.name!r}, age={self.age!r}, email={self.email!r})"

    def __eq__(self, other):
        if not isinstance(other, PersonOld):
            return False
        return self.name == other.name and self.age == other.age and self.email == other.email


# ===== @dataclass: code ít, tự động tạo __init__, __repr__, __eq__ =====
@dataclass
class Person:
    name: str
    age: int
    email: str = ""  # Default value


p1 = Person("Nam", 18, "nam@mail.com")
p2 = Person("Nam", 18, "nam@mail.com")
p3 = Person("An", 20)

print(p1)  # Person(name='Nam', age=18, email='nam@mail.com') -> __repr__ tự động
print(p1 == p2)  # True -> __eq__ tự động
print(p1 == p3)  # False
print(p3)  # Person(name='An', age=20, email='')


# ===== Default value với field() =====
# Dùng field() cho mutable default (list, dict) hoặc default phức tạp
import uuid


@dataclass
class User:
    # field(default_factory=...) cho mutable default
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    tags: list = field(default_factory=list)  # Mỗi instance có list riêng
    metadata: dict = field(default_factory=dict)
    # repr=False: ẩn field này khỏi __repr__
    password: str = field(default="", repr=False)

    def add_tag(self, tag):
        self.tags.append(tag)


u1 = User(name="Nam")
u2 = User(name="An", tags=["admin"])
print(u1)  # Không hiện password
print("u1 id:", u1.id)  # Random UUID
print("u2 id:", u2.id)  # UUID khác
print("u2 tags:", u2.tags)  # ['admin']

# Đảm bảo mỗi instance có list riêng (không shared)
u1.add_tag("user")
u2.add_tag("vip")
print("u1 tags:", u1.tags)  # ['user']
print("u2 tags:", u2.tags)  # ['admin', 'vip'] - RIÊNG BIỆT


# ===== Các option của @dataclass =====
# order=True: tự động tạo __lt__, __le__, __gt__, __ge__
# frozen=True: immutable (không thay đổi được sau khi tạo)
# unsafe_hash=True: tạo __hash__ (dùng với frozen)


@dataclass(order=True, frozen=True)
class Score:
    value: float
    subject: str


s1 = Score(8.5, "Math")
s2 = Score(9.0, "Physics")
s3 = Score(8.5, "Literature")

print("\nSo sánh:")
print("s1 < s2:", s1 < s2)  # True (so sánh theo thứ tự field: value trước)
print("s1 == s3:", s1 == s3)  # True (cùng value nhưng khác subject vẫn =)

# frozen=True -> immutable
# s1.value = 10.0  # FrozenInstanceError: cannot assign to field 'value'

# Có thể dùng làm key trong dict vì frozen
grades = {s1: "A", s2: "A+"}
print("Dict keys:", grades)


# ===== asdict() và astuple() =====
@dataclass
class Point:
    x: int
    y: int


p = Point(3, 5)
print("\nConvert:")
print("dict:", asdict(p))  # {'x': 3, 'y': 5}
print("tuple:", astuple(p))  # (3, 5)


# ===== Kế thừa với dataclass =====
@dataclass
class Animal:
    name: str
    age: int = 0


@dataclass
class Dog(Animal):
    breed: str = "Mixed"


@dataclass
class Cat(Animal):
    color: str = "Black"


dog = Dog("Milo", 3, "Golden")
cat = Cat("Kitty", 2, "White")
print("\nKế thừa dataclass:")
print(dog)  # Dog(name='Milo', age=3, breed='Golden')
print(cat)  # Cat(name='Kitty', age=2, color='White')


# ===== SO SÁNH: @dataclass vs class thường vs namedtuple =====
# @dataclass:   linh hoạt nhất, mutable, có method, typing, default
# class thường: cần kiểm soát hoàn toàn, logic phức tạp
# namedtuple:   immutable, nhẹ, nhưng giới hạn tính năng

# @dataclass nên dùng khi: class chủ yếu chứa data, cần type hints
# class thường nên dùng khi: logic phức tạp, cần kiểm soát __init__

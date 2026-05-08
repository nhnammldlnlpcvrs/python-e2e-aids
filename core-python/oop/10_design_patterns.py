# ============================================
# 10. DESIGN PATTERNS - MẪU THIẾT KẾ
# ============================================
# Design patterns = giải pháp đã được chứng minh cho vấn đề phổ biến
# Không phải code cụ thể, mà là ý tưởng/cách tổ chức

# ===== 1. SINGLETON: Đảm bảo class chỉ có 1 instance duy nhất =====
# Dùng cho: config, logger, database connection pool


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        """__new__ tạo instance. Nếu đã có thì trả cái cũ."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value=None):
        # Chỉ init lần đầu
        if not hasattr(self, '_initialized'):
            self.value = value
            self._initialized = True


a = Singleton("First")
b = Singleton("Second")  # Không ghi đè value vì đã _initialized
print("a is b:", a is b)  # True - cùng 1 object
print("a.value:", a.value)  # "First"
print("b.value:", b.value)  # "First" (cùng object)


# Singleton Decorator (cách khác)
def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class AppConfig:
    def __init__(self):
        self.settings = {"debug": True, "host": "localhost"}


c1 = AppConfig()
c2 = AppConfig()
print("c1 is c2:", c1 is c2)  # True


# ===== 2. FACTORY: Tạo object mà không cần chỉ định class cụ thể =====
# Dùng khi: logic tạo object phức tạp, muốn ẩn class cụ thể
from abc import ABC, abstractmethod


# Simple Factory
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Duck(Animal):
    def speak(self):
        return "Quack!"


class AnimalFactory:
    """Factory: quyết định tạo Animal nào dựa vào type"""

    @staticmethod
    def create(animal_type: str) -> Animal:
        animals = {
            "dog": Dog,
            "cat": Cat,
            "duck": Duck,
        }
        animal_class = animals.get(animal_type.lower())
        if animal_class is None:
            raise ValueError(f"Unknown animal: {animal_type}")
        return animal_class()


# Client code không cần biết Dog, Cat, Duck
factory = AnimalFactory()
my_pet = factory.create("dog")
print("My pet says:", my_pet.speak())


# Factory Method pattern (linh hoạt hơn)
class Document(ABC):
    @abstractmethod
    def create_pages(self):
        pass

    def render(self):
        pages = self.create_pages()
        return f"Rendering {len(pages)} pages"


class PDFDocument(Document):
    def create_pages(self):
        return ["PDF Header", "PDF Body", "PDF Footer"]


class HTMLDocument(Document):
    def create_pages(self):
        return ["<html>", "<body>", "</body>", "</html>"]


print(PDFDocument().render())
print(HTMLDocument().render())


# ===== 3. BUILDER: Tạo object phức tạp từng bước =====
# Dùng khi: object có nhiều field tùy chọn, muốn tách logic xây dựng


class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None
        self.os = None

    def __repr__(self):
        return f"Computer(cpu={self.cpu}, ram={self.ram}, storage={self.storage}, gpu={self.gpu}, os={self.os})"


class ComputerBuilder:
    """Builder: xây dựng Computer từng bước"""

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # Return self -> method chaining

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_os(self, os):
        self.computer.os = os
        return self

    def build(self):
        return self.computer


# Method chaining: xây dựng object rõ ràng, từng bước
gaming_pc = (ComputerBuilder()
             .set_cpu("Intel i9")
             .set_ram("32GB")
             .set_storage("1TB SSD")
             .set_gpu("RTX 4090")
             .set_os("Windows 11")
             .build())

office_pc = (ComputerBuilder()
             .set_cpu("Intel i5")
             .set_ram("16GB")
             .set_storage("512GB SSD")
             .set_os("Ubuntu")
             .build())

print("\nGaming PC:", gaming_pc)
print("Office PC:", office_pc)


# ===== 4. OBSERVER: 1 object thay đổi -> tự động thông báo cho các object khác =====
# Dùng cho: event system, pub/sub, UI updates


class EventManager:
    """Subject: quản lý danh sách observer và thông báo"""

    def __init__(self):
        self._observers = {}

    def subscribe(self, event, observer):
        if event not in self._observers:
            self._observers[event] = []
        self._observers[event].append(observer)

    def unsubscribe(self, event, observer):
        if event in self._observers:
            self._observers[event].remove(observer)

    def notify(self, event, data=None):
        if event in self._observers:
            for observer in self._observers[event]:
                observer.update(event, data)


class UserService:
    """Subject cụ thể: quản lý user, thông báo khi có thay đổi"""

    def __init__(self):
        self.events = EventManager()

    def create_user(self, name):
        print(f"Tạo user: {name}")
        self.events.notify("user_created", {"name": name})  # Bắn sự kiện

    def delete_user(self, name):
        print(f"Xóa user: {name}")
        self.events.notify("user_deleted", {"name": name})


# Observers
class EmailNotifier:
    def update(self, event, data):
        if event == "user_created":
            print(f"  [Email] Gửi welcome email đến {data['name']}")
        elif event == "user_deleted":
            print(f"  [Email] Gửi goodbye email đến {data['name']}")


class Logger:
    def update(self, event, data):
        print(f"  [Log] Event: {event}, Data: {data}")


class Analytics:
    def update(self, event, data):
        print(f"  [Analytics] Track: {event}")


# Kết nối lại với nhau
service = UserService()
service.events.subscribe("user_created", EmailNotifier())
service.events.subscribe("user_created", Logger())
service.events.subscribe("user_deleted", EmailNotifier())
service.events.subscribe("user_deleted", Analytics())

print("\n--- Tạo user ---")
service.create_user("Nam")
# Tự động: EmailNotifier.update() + Logger.update()

print("\n--- Xóa user ---")
service.delete_user("Nam")
# Tự động: EmailNotifier.update() + Analytics.update()

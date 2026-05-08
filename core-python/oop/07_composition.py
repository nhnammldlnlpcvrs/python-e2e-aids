# ============================================
# 7. COMPOSITION - COMPOSITION OVER INHERITANCE
# ============================================
# "Ưu tiên Composition hơn Kế thừa" - Gang of Four
# Kế thừa: "is-a" (Dog IS an Animal)
# Composition: "has-a" (Car HAS an Engine)
# Composition linh hoạt hơn, dễ thay đổi hơn kế thừa

# ===== VÍ DỤ: Kế thừa -> vấn đề =====
# Thiết kế Robot với kế thừa dễ bị bùng nổ class


# Cách dùng Kế thừa (có vấn đề):
class Robot:
    def move(self):
        pass


class WalkingRobot(Robot):
    def move(self):
        return "Đi bộ"


class FlyingRobot(Robot):
    def move(self):
        return "Bay"


# Muốn robot vừa đi vừa bay? Phải tạo class mới!
class WalkingFlyingRobot(WalkingRobot, FlyingRobot):
    def move(self):
        return "Đi bộ và Bay"


# -> Bùng nổ tổ hợp khi thêm khả năng mới


# ===== CÁCH COMPOSITION (linh hoạt hơn) =====
# Tách hành vi thành các component riêng, rồi "lắp ráp" vào robot
class WalkBehavior:
    """Component: khả năng đi bộ"""

    def move(self):
        return "Đi bộ"


class FlyBehavior:
    """Component: khả năng bay"""

    def move(self):
        return "Bay"


class SwimBehavior:
    """Component: khả năng bơi"""

    def move(self):
        return "Bơi"


class Robot:
    """Robot được lắp ráp từ các behavior component"""

    def __init__(self, name):
        self.name = name
        self._behaviors = []  # Danh sách các khả năng

    def add_behavior(self, behavior):
        """Gắn thêm khả năng cho robot"""
        self._behaviors.append(behavior)

    def remove_behavior(self, behavior):
        """Tháo khả năng khỏi robot (linh hoạt!)"""
        self._behaviors.remove(behavior)

    def show_abilities(self):
        """Liệt kê các khả năng"""
        abilities = [b.move() for b in self._behaviors]
        return f"{self.name} có thể: {', '.join(abilities)}"


# Lắp ráp robot tùy ý, không cần tạo class mới!
r2d2 = Robot("R2-D2")
r2d2.add_behavior(WalkBehavior())
print(r2d2.show_abilities())  # Có thể: Đi bộ

r2d2.add_behavior(SwimBehavior())  # Gắn thêm khả năng bơi
print(r2d2.show_abilities())  # Có thể: Đi bộ, Bơi

# Tạo robot khác với tổ hợp khác
drone = Robot("Drone-X")
drone.add_behavior(FlyBehavior())
print(drone.show_abilities())  # Có thể: Bay

# Thêm khả năng mới mà không cần sửa class Robot hay class khác
class TeleportBehavior:
    def move(self):
        return "Dịch chuyển tức thời"


r2d2.add_behavior(TeleportBehavior())
print(r2d2.show_abilities())  # Có thể: Đi bộ, Bơi, Dịch chuyển tức thời


# ===== COMPOSITION VỚI DEPENDENCY INJECTION =====
# Inject dependency qua constructor -> dễ test và thay đổi
class EmailService:
    def send(self, to, message):
        print(f"Gửi email đến {to}: {message}")


class SMSService:
    def send(self, to, message):
        print(f"Gửi SMS đến {to}: {message}")


class NotificationManager:
    """Quản lý notification, KHÔNG phụ thuộc vào Email/SMS cụ thể"""

    def __init__(self, service):
        """Nhận service từ bên ngoài (Dependency Injection)"""
        self._service = service  # Composition: HAS a notification service

    def notify(self, user, message):
        self._service.send(user, message)

    def set_service(self, service):
        """Có thể đổi service bất cứ lúc nào"""
        self._service = service


# Dùng Email
notifier = NotificationManager(EmailService())
notifier.notify("nam@mail.com", "Chào bạn!")

# Đổi sang SMS dễ dàng
notifier.set_service(SMSService())
notifier.notify("0123456789", "Chào bạn!")


# ===== KHI NÀO DÙNG INHERITANCE, KHI NÀO DÙNG COMPOSITION =====
# INHERITANCE (is-a):
# - Mối quan hệ "là một" rõ ràng, ổn định
# - Muốn tái sử dụng toàn bộ interface của class cha
# - Ví dụ: Dog IS an Animal, Rectangle IS a Shape

# COMPOSITION (has-a):
# - Mối quan hệ "có một" hoặc "sử dụng một"
# - Cần linh hoạt, dễ thay đổi khi runtime
# - Muốn tránh bùng nổ class (class explosion)
# - Ví dụ: Car HAS an Engine, Robot HAS MoveBehavior

# NGUYÊN TẮC: Khi nghi ngờ, chọn COMPOSITION.

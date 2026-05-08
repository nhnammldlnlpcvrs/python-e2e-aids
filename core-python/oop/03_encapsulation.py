# ============================================
# 3. ENCAPSULATION - ĐÓNG GÓI
# ============================================
# Đóng gói: ẩn dữ liệu bên trong, chỉ truy cập qua method công khai
# Python dùng QUY ƯỚC (convention) thay vì bắt buộc (không có private thực sự)
# 3 cấp độ: public, _protected, __private

# ===== 1. PUBLIC: không có dấu gạch dưới =====
# Có thể truy cập từ bất kỳ đâu
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.balance = balance  # Public attribute -> ai cũng sửa được!


acc = BankAccount("Nam", 1000)
acc.balance = -99999  # Ai cũng có thể gán trực tiếp -> NGUY HIỂM
print(f"Balance: {acc.balance}")  # -99999 (vô lý!)


# ===== 2. _PROTECTED: 1 dấu gạch dưới =====
# QUY ƯỚC: "đây là internal, đừng đụng vào từ bên ngoài"
# Python không ngăn truy cập, chỉ là tín hiệu cho developer
class BetterAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance  # Protected: quy ước "không nên đụng"

    def get_balance(self):
        """Công khai cách đọc balance"""
        return self._balance

    def deposit(self, amount):
        """Công khai cách nạp tiền, có validation"""
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Công khai cách rút tiền, có validation"""
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False


acc = BetterAccount("Nam", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Balance:", acc.get_balance())  # 1300
# acc._balance = -99999  # VẪN LÀM ĐƯỢC, nhưng quy ước là "đừng làm"


# ===== 3. __PRIVATE: 2 dấu gạch dưới =====
# Python dùng NAME MANGLING để "ẩn" attribute
# __attr -> _ClassName__attr (Python tự đổi tên)
class SecureAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private (name mangling)

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


acc = SecureAccount("Nam", 1000)
print("Balance:", acc.get_balance())  # OK - qua method public
# print(acc.__balance)  # AttributeError: 'SecureAccount' has no '__balance'

# Nhưng vẫn truy cập được nếu biết cơ chế name mangling:
print("Truy cập trực tiếp:", acc._SecureAccount__balance)  # Vẫn được! Nhưng đừng làm.


# ===== 4. @property: GETTER / SETTER / DELETER pythonic =====
# Cách Pythonic để kiểm soát truy cập attribute, không cần get_xxx()/set_xxx()
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = None  # Backing field
        self.price = price  # Gọi setter (dòng dưới)

    @property
    def price(self):
        """Getter: product.price (không cần product.get_price())"""
        return self._price

    @price.setter
    def price(self, value):
        """Setter: product.price = X -> tự động gọi"""
        if value < 0:
            raise ValueError("Giá không thể âm!")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter: del product.price -> tự động gọi"""
        print("Đang xóa giá...")
        self._price = None


p = Product("Laptop", 1000)
print("Giá:", p.price)  # 1000 - như đọc attribute bình thường
p.price = 1200  # Như gán bình thường, nhưng chạy qua setter
print("Giá mới:", p.price)  # 1200

# p.price = -500  # ValueError: Giá không thể âm!
del p.price  # Đang xóa giá...
print("Sau khi xóa:", p.price)  # None


# ===== @property chỉ đọc (Read-only) =====
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def area(self):
        """Read-only: tính từ radius, không set được"""
        import math
        return math.pi * self._radius ** 2

    @property
    def diameter(self):
        """Read-only: chỉ get, không có setter"""
        return self._radius * 2


c = Circle(5)
print("Bán kính:", c.radius)
print("Diện tích:", c.area)
print("Đường kính:", c.diameter)
# c.area = 100  # AttributeError: can't set attribute (read-only)


# ===== @property với cache/lazy evaluation =====
class HeavyData:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        """Chỉ load data khi cần (lazy), rồi cache lại"""
        if self._data is None:
            print("Đang load data... (chỉ gọi 1 lần)")
            import time
            time.sleep(0.5)  # Giả lập heavy computation
            self._data = [x ** 2 for x in range(10)]
        return self._data


hd = HeavyData()
print("Truy cập lần 1:")
print(hd.data)  # Load và cache
print("Truy cập lần 2:")
print(hd.data)  # Dùng cache, không load lại


# ===== TÓM TẮT =====
# public:    self.name       - ai cũng dùng được
# protected: self._name      - QUY ƯỚC: nội bộ, đừng đụng
# private:   self.__name     - Name mangling, khó truy cập hơn (nhưng vẫn được)
# property:  dùng @property  - Pythonic getter/setter

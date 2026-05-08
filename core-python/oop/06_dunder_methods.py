# ============================================
# 6. DUNDER METHODS - MAGIC / SPECIAL METHODS
# ============================================
# Dunder = Double UNDERscore: __init__, __str__, __add__, __len__...
# Giúp object của bạn hoạt động như built-in types của Python

# ===== __str__ vs __repr__: biểu diễn object =====
# __str__: cho người dùng (print(), str()) - dễ đọc
# __repr__: cho developer (repr(), debug) - rõ ràng, có thể eval được


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Dành cho người dùng - print()"""
        return f"({self.x}, {self.y})"

    def __repr__(self):
        """Dành cho developer - repr(), debug"""
        return f"Point(x={self.x}, y={self.y})"  # Có thể copy để tạo lại object


p = Point(3, 5)
print(str(p))  # (3, 5) - dùng __str__
print(repr(p))  # Point(x=3, y=5) - dùng __repr__
# Trong list, Python dùng __repr__
print([p])  # [Point(x=3, y=5)]


# ===== __len__, __getitem__, __setitem__: hoạt động như list =====
class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add_song(self, song):
        self._songs.append(song)

    def __len__(self):
        """Cho phép len(playlist)"""
        return len(self._songs)

    def __getitem__(self, index):
        """Cho phép playlist[i]"""
        return self._songs[index]

    def __setitem__(self, index, value):
        """Cho phép playlist[i] = X"""
        self._songs[index] = value

    def __contains__(self, song):
        """Cho phép 'song' in playlist"""
        return song in self._songs

    def __iter__(self):
        """Cho phép for song in playlist"""
        return iter(self._songs)


pl = Playlist("My Favorites")
pl.add_song("Shape of You")
pl.add_song("Blinding Lights")
pl.add_song("Bohemian Rhapsody")

print(f"Số bài hát: {len(pl)}")  # __len__
print(f"Bài đầu tiên: {pl[0]}")  # __getitem__
pl[0] = "Perfect"  # __setitem__
print(f"Sau khi sửa: {pl[0]}")
print("'Perfect' trong list?", "Perfect" in pl)  # __contains__

for song in pl:  # __iter__
    print(f"  - {song}")


# ===== __eq__, __lt__, __gt__: so sánh object =====
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        """== : so sánh bằng"""
        if not isinstance(other, Student):
            return NotImplemented  # Để Python thử cách khác
        return self.score == other.score

    def __lt__(self, other):
        """< : so sánh nhỏ hơn -> hỗ trợ sort()"""
        return self.score < other.score

    def __le__(self, other):
        """<= """
        return self.score <= other.score

    def __repr__(self):
        return f"Student({self.name}, {self.score})"


s1 = Student("Nam", 8.5)
s2 = Student("An", 9.0)
s3 = Student("Linh", 8.5)

print("\nSo sánh:")
print("s1 == s2:", s1 == s2)  # False (8.5 != 9.0)
print("s1 == s3:", s1 == s3)  # True  (8.5 == 8.5)
print("s1 < s2:", s1 < s2)  # True  (8.5 < 9.0)

# sort() dùng __lt__
students = [s2, s1, s3]
students.sort()
print("Sorted:", students)  # Theo score tăng dần
students.sort(reverse=True)
print("Sorted desc:", students)  # Theo score giảm dần


# ===== __add__, __mul__: toán tử số học =====
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """v1 + v2"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """v1 - v2"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """v * 3 (scalar multiplication)"""
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        """3 * v (right multiplication)"""
        return self.__mul__(scalar)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)
print("\nVector math:")
print("v1 + v2:", v1 + v2)  # Vector(4, 6)
print("v1 - v2:", v1 - v2)  # Vector(2, 2)
print("v1 * 3:", v1 * 3)  # Vector(9, 12)
print("3 * v1:", 3 * v1)  # Vector(9, 12) - dùng __rmul__


# ===== __call__: object gọi được như hàm =====
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, x):
        """Cho phép: multiplier_instance(x)"""
        return x * self.factor


double = Multiplier(2)
triple = Multiplier(3)
print("\n__call__:")
print("double(5):", double(5))  # 10
print("triple(5):", triple(5))  # 15


# ===== __enter__ / __exit__: Context Manager =====
# Cho phép dùng "with object as x:"
class Database:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        """Khi vào with block"""
        print(f"  Mở kết nối đến {self.name}")
        return self  # Giá trị gán cho biến sau 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Khi thoát with block (kể cả khi có lỗi)"""
        print(f"  Đóng kết nối đến {self.name}")
        if exc_type:
            print(f"  Lỗi: {exc_val}")
        return False  # True = nuốt lỗi, False = ném tiếp lỗi

    def query(self, sql):
        print(f"  Chạy query: {sql}")


print("\nContext Manager:")
with Database("mydb") as db:
    db.query("SELECT * FROM users")
# Tự động gọi __exit__ khi ra khỏi with

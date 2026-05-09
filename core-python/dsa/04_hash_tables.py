# ============================================
# 4. HASH TABLES - BẢNG BĂM / HASH TABLES
# ============================================
# Hash Table: ánh xạ key -> value qua hash function.
# Python dict và set đều dùng hash table bên trong.
# Trung bình: insert/search/delete O(1). Worst case: O(n).

# --- Hash function đơn giản ---
def simple_hash(key, table_size):
    """Hash function cho integer"""
    return key % table_size

def string_hash(s, table_size):
    """Hash function cho string (djb2 variation)"""
    h = 5381
    for ch in s:
        h = ((h << 5) + h) + ord(ch)  # h * 33 + ord(ch)
    return h % table_size

print("=== Hash Functions ===")
print("simple_hash(42, 10):", simple_hash(42, 10))
print("string_hash('hello', 10):", string_hash('hello', 10))
print("string_hash('world', 10):", string_hash('world', 10))

# Python hash()
print("hash('hello'):", hash('hello'))
print("hash(42):", hash(42))
print("hash((1,2,3)):", hash((1, 2, 3)))  # Tuple hashable
# print(hash([1,2,3]))  # List không hashable! TypeError

# ==============================
# Separate Chaining (Dây chuyền)
# ==============================

class HashTableChaining:
    """Hash table dùng separate chaining (linked list cho mỗi bucket)"""

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        """Hash function: hỗ trợ int và string"""
        if isinstance(key, int):
            return key % self.size
        return string_hash(str(key), self.size)

    def put(self, key, value):
        """Thêm/cập nhật key-value. O(1) avg, O(n) worst"""
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Cập nhật
                return
        bucket.append((key, value))
        self.count += 1
        # Resize nếu load factor > 0.75
        if self.count / self.size > 0.75:
            self._resize(self.size * 2)

    def get(self, key):
        """Lấy value theo key. O(1) avg"""
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Xóa key. O(1) avg"""
        idx = self._hash(key)
        bucket = self.table[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.count -= 1
                return True
        return False

    def contains(self, key):
        return self.get(key) is not None

    def _resize(self, new_size):
        """Resize hash table khi load factor vượt ngưỡng"""
        old_table = self.table
        self.size = new_size
        self.table = [[] for _ in range(new_size)]
        self.count = 0
        for bucket in old_table:
            for k, v in bucket:
                self.put(k, v)

    def __repr__(self):
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                result.append(f"  [{i}]: {bucket}")
        return "\n".join(result) if result else "  Empty"


print("\n=== Separate Chaining Hash Table ===")
ht = HashTableChaining(5)
ht.put("apple", 100)
ht.put("banana", 200)
ht.put("orange", 300)
ht.put("grape", 400)
ht.put("mango", 500)
ht.put("peach", 600)
print("Hash table (size={}):".format(ht.size))
print(ht)
print(f"get('banana'): {ht.get('banana')}")
print(f"get('kiwi'): {ht.get('kiwi')}")  # None
ht.delete("orange")
print(f"Sau delete('orange'):")
print(ht)

# ==============================
# Open Addressing (Địa chỉ mở)
# ==============================

class HashTableOA:
    """Hash table dùng open addressing (linear probing)"""

    DELETED = object()  # Sentinel cho ô đã xóa

    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0

    def _hash(self, key):
        if isinstance(key, int):
            return key % self.size
        return string_hash(str(key), self.size)

    def _probe(self, idx, i):
        """Linear probing: idx + i"""
        return (idx + i) % self.size

    def put(self, key, value):
        """Thêm key-value với linear probing"""
        idx = self._hash(key)
        first_deleted = None
        for i in range(self.size):
            probe_idx = self._probe(idx, i)
            slot = self.table[probe_idx]
            # Tìm thấy key đã tồn tại
            if slot is not None and slot is not self.DELETED and slot[0] == key:
                self.table[probe_idx] = (key, value)
                return
            # Ghi nhớ ô deleted đầu tiên để tái sử dụng
            if slot is self.DELETED and first_deleted is None:
                first_deleted = probe_idx
            # Ô trống
            if slot is None or slot is self.DELETED:
                target = first_deleted if first_deleted is not None else probe_idx
                self.table[target] = (key, value)
                self.count += 1
                if self.count / self.size > 0.7:
                    self._resize(self.size * 2)
                return
        raise Exception("Hash table đầy")

    def get(self, key):
        """Lấy value"""
        idx = self._hash(key)
        for i in range(self.size):
            probe_idx = self._probe(idx, i)
            slot = self.table[probe_idx]
            if slot is None:
                return None
            if slot is not self.DELETED and slot[0] == key:
                return slot[1]
        return None

    def delete(self, key):
        """Xóa key (đánh dấu DELETED)"""
        idx = self._hash(key)
        for i in range(self.size):
            probe_idx = self._probe(idx, i)
            slot = self.table[probe_idx]
            if slot is None:
                return False
            if slot is not self.DELETED and slot[0] == key:
                self.table[probe_idx] = self.DELETED
                self.count -= 1
                return True
        return False

    def _resize(self, new_size):
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        for slot in old_table:
            if slot is not None and slot is not self.DELETED:
                self.put(slot[0], slot[1])

    def __repr__(self):
        result = []
        for i, slot in enumerate(self.table):
            if slot is not None and slot is not self.DELETED:
                result.append(f"  [{i}]: {slot}")
            elif slot is self.DELETED:
                result.append(f"  [{i}]: DELETED")
        return "\n".join(result) if result else "  Empty"


print("\n=== Open Addressing Hash Table (Linear Probing) ===")
ht2 = HashTableOA(7)
ht2.put("one", 1)
ht2.put("two", 2)
ht2.put("three", 3)
print("Hash table:")
print(ht2)
ht2.delete("two")
print("Sau delete('two'):")
print(ht2)
print(f"get('three'): {ht2.get('three')}")
print(f"get('two'): {ht2.get('two')}")  # None

# ==============================
# Python dict & set Internals
# ==============================

print("\n=== Python dict & set ===")
# dict: hash table with open addressing (since Python 3.6+)
# key phải hashable: immutable, implement __hash__ và __eq__
d = {"a": 1, "b": 2, "c": 3}
print("dict:", d)
print("d['a']:", d["a"])
print("'x' in d:", "x" in d)           # O(1)
print("d.get('x', 'default'):", d.get("x", "default"))

# set: hash table chỉ lưu key, không value
s = {1, 2, 3, 3, 3}
print("set:", s)                       # {1, 2, 3}
s.add(4)
s.remove(2)
print("set sau thêm/xóa:", s)
print("3 in s:", 3 in s)               # O(1)

# --- Ứng dụng: Frequency Counter ---
def frequency_counter(arr):
    """Đếm tần suất phần tử - O(n)"""
    freq = {}
    for x in arr:
        freq[x] = freq.get(x, 0) + 1
    return freq

print("\nỨng dụng - Frequency counter:")
data = ["a", "b", "a", "c", "b", "a"]
print(f"  {data} -> {frequency_counter(data)}")

# --- Ứng dụng: Two Sum ---
def two_sum(nums, target):
    """Tìm 2 số có tổng = target - O(n) dùng dict"""
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return (seen[complement], i)
        seen[n] = i
    return None

print("\nỨng dụng - Two Sum:")
nums = [2, 7, 11, 15]
print(f"  nums={nums}, target=9 -> {two_sum(nums, 9)}")

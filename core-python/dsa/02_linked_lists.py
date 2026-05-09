# ============================================
# 2. LINKED LISTS - DANH SÁCH LIÊN KẾT / LINKED LISTS
# ============================================
# LinkedList = chuỗi các Node, mỗi Node chứa data + con trỏ tới Node tiếp theo.
# Khác array: truy cập ngẫu nhiên O(n), nhưng chèn/xóa đầu O(1).

# ==============================
# Singly Linked List
# ==============================

class Node:
    """Node cho singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    """Danh sách liên kết đơn"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Thêm vào cuối - O(n)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def prepend(self, data):
        """Thêm vào đầu - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at(self, index, data):
        """Chèn tại vị trí index - O(n)"""
        if index == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        cur = self.head
        for _ in range(index - 1):
            if cur is None:
                raise IndexError("Index out of range")
            cur = cur.next
        new_node.next = cur.next
        cur.next = new_node

    def delete(self, key):
        """Xóa node đầu tiên có data = key - O(n)"""
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur:
            prev.next = cur.next

    def search(self, key):
        """Tìm kiếm - O(n), trả về bool"""
        cur = self.head
        while cur:
            if cur.data == key:
                return True
            cur = cur.next
        return False

    def reverse(self):
        """Đảo ngược danh sách tại chỗ - O(n)"""
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def find_middle(self):
        """Tìm node giữa bằng kỹ thuật fast/slow pointer - O(n)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data if slow else None

    def has_cycle(self):
        """Kiểm tra chu trình - Floyd's Tortoise & Hare - O(n)"""
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def display(self):
        """In danh sách"""
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        print("  ", " -> ".join(result) if result else "Empty")


print("=== Singly Linked List ===")
sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.prepend(5)
print("Sau append(10,20,30) và prepend(5):")
sll.display()

sll.insert_at(2, 15)
print("Sau insert_at(2, 15):")
sll.display()

sll.delete(20)
print("Sau delete(20):")
sll.display()

print("Search 15:", sll.search(15))
print("Search 99:", sll.search(99))
print("Middle:", sll.find_middle())

sll.reverse()
print("Sau reverse:")
sll.display()

print("Has cycle:", sll.has_cycle())

# ==============================
# Doubly Linked List
# ==============================

class DNode:
    """Node cho doubly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """Danh sách liên kết đôi"""

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Thêm cuối - O(1)"""
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, data):
        """Thêm đầu - O(1)"""
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def delete(self, key):
        """Xóa node đầu tiên có data = key - O(n)"""
        cur = self.head
        while cur and cur.data != key:
            cur = cur.next
        if cur is None:
            return
        if cur.prev:
            cur.prev.next = cur.next
        else:
            self.head = cur.next
        if cur.next:
            cur.next.prev = cur.prev
        else:
            self.tail = cur.prev

    def display_forward(self):
        """In từ đầu đến cuối"""
        cur = self.head
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.next
        print("  Forward:", " <-> ".join(result) if result else "Empty")

    def display_backward(self):
        """In từ cuối lên đầu"""
        cur = self.tail
        result = []
        while cur:
            result.append(str(cur.data))
            cur = cur.prev
        print("  Backward:", " <-> ".join(result) if result else "Empty")


print("\n=== Doubly Linked List ===")
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.prepend(5)
print("Sau append(10,20,30) và prepend(5):")
dll.display_forward()
dll.display_backward()

dll.delete(20)
print("Sau delete(20):")
dll.display_forward()

# ==============================
# Circular Linked List
# ==============================

class CircularLinkedList:
    """Danh sách liên kết vòng"""

    def __init__(self):
        self.head = None

    def append(self, data):
        """Thêm vào cuối - O(n)"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new_node
        new_node.next = self.head

    def display(self, limit=10):
        """In danh sách (có giới hạn vòng)"""
        if self.head is None:
            print("  Empty")
            return
        cur = self.head
        result = []
        count = 0
        while True:
            result.append(str(cur.data))
            cur = cur.next
            count += 1
            if cur == self.head or count >= limit:
                break
        print("  ", " -> ".join(result), "-> (back to head)")


print("\n=== Circular Linked List ===")
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("Circular list:")
cll.display()

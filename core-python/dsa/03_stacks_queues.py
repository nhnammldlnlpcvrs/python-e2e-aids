# ============================================
# 3. STACKS & QUEUES - NGĂN XẾP & HÀNG ĐỢI / STACKS & QUEUES
# ============================================
# Stack: LIFO (Last In First Out) - vào sau ra trước.
# Queue: FIFO (First In First Out) - vào trước ra trước.

from collections import deque

# ==============================
# STACK - NGĂN XẾP
# ==============================

print("=== STACK (Ngăn xếp) ===")

# --- Cách 1: Dùng list (đơn giản nhất) ---
print("\n1. Stack dùng list:")
stack = []
stack.append(1)    # push
stack.append(2)
stack.append(3)
print("  Stack:", stack)
print("  Pop:", stack.pop())  # Lấy ra 3 (cuối cùng)
print("  Pop:", stack.pop())  # Lấy ra 2
print("  Stack sau pop:", stack)

# --- Cách 2: Stack class tự cài ---
class Stack:
    """Ngăn xếp dùng list"""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Thêm vào đỉnh - O(1)"""
        self._items.append(item)

    def pop(self):
        """Lấy đỉnh ra - O(1)"""
        if self.is_empty():
            raise IndexError("Stack rỗng")
        return self._items.pop()

    def peek(self):
        """Xem đỉnh - O(1)"""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return str(self._items)


print("\n2. Stack class:")
s = Stack()
s.push("A")
s.push("B")
s.push("C")
print("  Stack:", s)
print("  Peek:", s.peek())
print("  Pop:", s.pop())
print("  Size:", s.size())

# --- Ứng dụng Stack: Kiểm tra dấu ngoặc ---
def is_balanced(expr):
    """Kiểm tra dấu ngoặc cân bằng: (), [], {}"""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() != pairs[ch]:
                return False
    return len(stack) == 0

print("\n3. Balanced parentheses:")
test_exprs = ["([]){}", "([)]", "(]", "((()))"]
for expr in test_exprs:
    print(f"  '{expr}' -> {is_balanced(expr)}")

# --- Ứng dụng Stack: Đảo chuỗi ---
def reverse_string(s):
    """Đảo chuỗi dùng stack"""
    stack = list(s)
    result = []
    while stack:
        result.append(stack.pop())
    return ''.join(result)

print("\n4. Reverse string dùng stack:")
print(f"  'hello' -> '{reverse_string('hello')}'")

# --- Ứng dụng Stack: Postfix evaluation ---
def evaluate_postfix(expr):
    """Tính biểu thức hậu tố (Reverse Polish Notation)"""
    stack = []
    for token in expr.split():
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/': stack.append(a / b)
        else:
            stack.append(int(token))
    return stack[0]

print("\n5. Postfix evaluation:")
print(f"  '5 3 +' -> {evaluate_postfix('5 3 +')}")
print(f"  '5 1 2 + 4 * + 3 -' -> {evaluate_postfix('5 1 2 + 4 * + 3 -')}")

# ==============================
# QUEUE - HÀNG ĐỢI
# ==============================

print("\n=== QUEUE (Hàng đợi) ===")

# --- Cách 1: Dùng collections.deque (tối ưu) ---
print("\n1. Queue dùng deque:")
queue = deque()
queue.append(1)     # enqueue
queue.append(2)
queue.append(3)
print("  Queue:", list(queue))
print("  Dequeue:", queue.popleft())  # Lấy ra 1 (đầu tiên)
print("  Dequeue:", queue.popleft())  # Lấy ra 2

# --- Cách 2: Queue class tự cài ---
class Queue:
    """Hàng đợi dùng deque"""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        """Thêm vào cuối - O(1)"""
        self._items.append(item)

    def dequeue(self):
        """Lấy đầu ra - O(1)"""
        if self.is_empty():
            raise IndexError("Queue rỗng")
        return self._items.popleft()

    def front(self):
        """Xem đầu - O(1)"""
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

    def __repr__(self):
        return str(list(self._items))


print("\n2. Queue class:")
q = Queue()
q.enqueue("X")
q.enqueue("Y")
q.enqueue("Z")
print("  Queue:", q)
print("  Front:", q.front())
print("  Dequeue:", q.dequeue())
print("  Sau dequeue:", q)

# --- Cách 3: Queue dùng 2 stack ---
class QueueWithStacks:
    """Queue cài bằng 2 stack - amortized O(1)"""

    def __init__(self):
        self.stack_in = []   # Stack để enqueue
        self.stack_out = []  # Stack để dequeue

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            raise IndexError("Queue rỗng")
        return self.stack_out.pop()

    def __repr__(self):
        return f"in={self.stack_in}, out={self.stack_out}"


print("\n3. Queue dùng 2 stack:")
q2 = QueueWithStacks()
q2.enqueue(10)
q2.enqueue(20)
q2.enqueue(30)
print(f"  Sau enqueue(10,20,30): {q2}")
print(f"  Dequeue: {q2.dequeue()}")
print(f"  Dequeue: {q2.dequeue()}")
q2.enqueue(40)
print(f"  Sau enqueue(40): {q2}")
print(f"  Dequeue: {q2.dequeue()}")

# ==============================
# DEQUE - HÀNG ĐỢI HAI ĐẦU
# ==============================

print("\n=== DEQUE (Hàng đợi hai đầu) ===")
dq = deque()
dq.append(1)        # Thêm phải
dq.appendleft(0)    # Thêm trái
dq.append(2)
print("Deque:", list(dq))
print("Pop right:", dq.pop())
print("Pop left:", dq.popleft())

# --- Ứng dụng: Kiểm tra Palindrome ---
def is_palindrome(s):
    """Kiểm tra palindrome dùng deque"""
    dq = deque(s)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

print("\nPalindrome check dùng deque:")
for w in ["radar", "hello", "abba"]:
    print(f"  '{w}' -> {is_palindrome(w)}")

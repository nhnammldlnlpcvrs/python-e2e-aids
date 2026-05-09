# ============================================
# 7. AVL TREES - CÂY AVL / AVL TREES
# ============================================
# AVL = BST tự cân bằng. |chiều_cao_trái - chiều_cao_phải| <= 1 cho mọi node.
# Cân bằng được duy trì qua 4 phép xoay: LL, RR, LR, RL.
# Insert/Delete/Search: O(log n) guaranteed.


class AVLNode:
    """Node của AVL tree"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1  # Chiều cao của node (tính từ node này đến lá)


class AVLTree:
    """Cây AVL tự cân bằng"""

    def __init__(self):
        self.root = None

    # ==========================
    # Tiện ích
    # ==========================

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        """Balance factor = height(left) - height(right)"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # ==========================
    # 4 phép xoay
    # ==========================

    def rotate_right(self, y):
        """Xoay phải (dùng cho LL)"""
        #   y         x
        #  / \       / \
        # x   T3 -> T1  y
        #/ \           / \
        #T1 T2        T2 T3
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        """Xoay trái (dùng cho RR)"""
        #   x           y
        #  / \         / \
        # T1  y  ->   x   T3
        #    / \     / \
        #   T2 T3  T1 T2
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        self.update_height(x)
        self.update_height(y)
        return y

    # ==========================
    # Insert
    # ==========================

    def insert(self, val):
        """Chèn giá trị mới, tự cân bằng - O(log n)"""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        # B1: Chèn như BST thường
        if node is None:
            return AVLNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        else:
            return node  # Trùng, bỏ qua

        # B2: Cập nhật chiều cao
        self.update_height(node)

        # B3: Kiểm tra cân bằng và xoay
        balance = self.get_balance(node)

        # LL: left-left (mất cân bằng trái - trái)
        if balance > 1 and val < node.left.val:
            return self.rotate_right(node)

        # RR: right-right (mất cân bằng phải - phải)
        if balance < -1 and val > node.right.val:
            return self.rotate_left(node)

        # LR: left-right (mất cân bằng trái - phải)
        if balance > 1 and val > node.left.val:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # RL: right-left (mất cân bằng phải - trái)
        if balance < -1 and val < node.right.val:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # ==========================
    # Delete
    # ==========================

    def delete(self, val):
        """Xóa node, tự cân bằng - O(log n)"""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None

        # B1: Xóa như BST
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Node có 0 hoặc 1 con
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Node có 2 con: tìm successor
            succ = self._get_min(node.right)
            node.val = succ.val
            node.right = self._delete(node.right, succ.val)

        if node is None:
            return None

        # B2: Cập nhật chiều cao
        self.update_height(node)

        # B3: Cân bằng
        balance = self.get_balance(node)

        # LL
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)

        # LR
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # RR
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)

        # RL
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _get_min(self, node):
        while node.left:
            node = node.left
        return node

    # ==========================
    # Duyệt cây
    # ==========================

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def print_tree(self):
        """In cây theo mức"""
        from collections import deque
        if self.root is None:
            return
        q = deque([self.root])
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(str(node.val))
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(".")
            print("  ", " ".join(level))


# ==============================
# Demo
# ==============================
print("=== AVL Tree ===")
avl = AVLTree()

# Insert các giá trị gây mất cân bằng
print("\n--- Insert demo ---")
test_data = [30, 20, 40, 10, 5]  # 5 sẽ trigger LL rotation
print("Insert:", test_data)
for v in test_data:
    avl.insert(v)

print("Inorder:", avl.inorder())
print("Preorder:", avl.preorder())
print("Tree structure:")
avl.print_tree()

# Thêm các giá trị trigger RR, LR, RL
print("\nThêm tiếp: 3, 35, 32")
for v in [3, 35, 32]:
    avl.insert(v)

print("Inorder:", avl.inorder())
print("Preorder:", avl.preorder())
print("Tree structure:")
avl.print_tree()

# --- Delete demo ---
print("\n--- Delete demo ---")
avl.delete(32)
print("Sau delete(32) - lá:", avl.inorder())
print("Tree structure:")
avl.print_tree()

avl.delete(30)  # Xóa node có 2 con
print("Sau delete(30):", avl.inorder())
print("Tree structure:")
avl.print_tree()

# --- AVL vs BST không cân bằng ---
print("\n--- So sánh AVL vs BST ---")
# Chèn dãy tăng dần vào BST thường -> cây suy biến thành linked list (height = n)
# Chèn dãy tăng dần vào AVL -> tự cân bằng (height = log n)
avl2 = AVLTree()
for i in range(1, 16):
    avl2.insert(i)
print("AVL với 1..15 (tăng dần):")
print("  Inorder:", avl2.inorder()[:5], "...", avl2.inorder()[-5:])
print("  Cây cân bằng height ~ log2(15) = 4")
avl2.print_tree()

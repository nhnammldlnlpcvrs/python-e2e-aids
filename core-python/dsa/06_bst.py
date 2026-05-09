# ============================================
# 6. BST - CÂY NHỊ PHÂN TÌM KIẾM / BINARY SEARCH TREE
# ============================================
# BST: left < node < right. Mọi node trong cây thỏa mãn.
# Inorder traversal của BST luôn cho dãy đã sắp xếp.

class BSTNode:
    """Node của BST"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    """Binary Search Tree"""

    def __init__(self):
        self.root = None

    # --- Insert (Chèn) ---
    def insert(self, val):
        """Chèn giá trị vào BST - O(h)"""
        self.root = self._insert(self.root, val)

    def _insert(self, node, val):
        if node is None:
            return BSTNode(val)
        if val < node.val:
            node.left = self._insert(node.left, val)
        elif val > node.val:
            node.right = self._insert(node.right, val)
        # val == node.val: bỏ qua (không chèn trùng)
        return node

    def insert_iterative(self, val):
        """Chèn không đệ quy"""
        new_node = BSTNode(val)
        if self.root is None:
            self.root = new_node
            return
        cur = self.root
        while True:
            if val < cur.val:
                if cur.left is None:
                    cur.left = new_node
                    return
                cur = cur.left
            elif val > cur.val:
                if cur.right is None:
                    cur.right = new_node
                    return
                cur = cur.right
            else:
                return  # Trùng, bỏ qua

    # --- Search (Tìm kiếm) ---
    def search(self, val):
        """Tìm kiếm - O(h), trả về bool"""
        return self._search(self.root, val)

    def _search(self, node, val):
        if node is None:
            return False
        if val == node.val:
            return True
        elif val < node.val:
            return self._search(node.left, val)
        else:
            return self._search(node.right, val)

    # --- Min / Max ---
    def find_min(self):
        """Tìm giá trị nhỏ nhất - O(h)"""
        if self.root is None:
            return None
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.val

    def find_max(self):
        """Tìm giá trị lớn nhất - O(h)"""
        if self.root is None:
            return None
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.val

    # --- Delete (Xóa) ---
    def delete(self, val):
        """Xóa node - O(h). 3 trường hợp: lá, 1 con, 2 con"""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Tìm thấy node cần xóa
            # Case 1: Node lá (không có con)
            if node.left is None and node.right is None:
                return None
            # Case 2: Node có 1 con
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Node có 2 con
            # Tìm successor (min của cây con phải)
            successor = self._find_min_node(node.right)
            node.val = successor.val
            node.right = self._delete(node.right, successor.val)
        return node

    def _find_min_node(self, node):
        """Tìm node có giá trị nhỏ nhất"""
        while node.left:
            node = node.left
        return node

    # --- Successor / Predecessor ---
    def successor(self, val):
        """Tìm successor: node nhỏ nhất > val"""
        node = self.root
        succ = None
        while node:
            if val < node.val:
                succ = node.val
                node = node.left
            else:
                node = node.right
        return succ

    def predecessor(self, val):
        """Tìm predecessor: node lớn nhất < val"""
        node = self.root
        pred = None
        while node:
            if val > node.val:
                pred = node.val
                node = node.right
            else:
                node = node.left
        return pred

    # --- Validate BST ---
    def is_valid_bst(self):
        """Kiểm tra cây có phải BST hợp lệ - O(n)"""
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (self._is_valid_bst(node.left, min_val, node.val) and
                self._is_valid_bst(node.right, node.val, max_val))

    # --- Inorder traversal (cho ra dãy đã sắp xếp) ---
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)


# ==============================
# Demo
# ==============================
print("=== Binary Search Tree ===")
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80, 35, 45]
for v in values:
    bst.insert(v)

print("Insert:", values)
print("Inorder (đã sắp xếp):", bst.inorder())
print("Min:", bst.find_min())
print("Max:", bst.find_max())
print("Search 40:", bst.search(40))
print("Search 99:", bst.search(99))
print("Successor of 40:", bst.successor(40))
print("Predecessor of 40:", bst.predecessor(40))
print("Successor of 45:", bst.successor(45))
print("Predecessor of 20:", bst.predecessor(20))  # None
print("Is valid BST:", bst.is_valid_bst())

# --- Xóa node ---
print("\n=== Delete demo ===")
print("Inorder trước delete:", bst.inorder())
bst.delete(20)  # Xóa lá
print("Sau delete(20) - lá:", bst.inorder())
bst.delete(70)  # Xóa node có 1 con
print("Sau delete(70) - 1 con:", bst.inorder())
bst.delete(50)  # Xóa node có 2 con (root)
print("Sau delete(50) - 2 con (root):", bst.inorder())
print("Is valid BST:", bst.is_valid_bst())

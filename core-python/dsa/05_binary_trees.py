# ============================================
# 5. BINARY TREES - CÂY NHỊ PHÂN / BINARY TREES
# ============================================
# Cây nhị phân: mỗi node có tối đa 2 con (left, right).
# Cây là cấu trúc phân cấp, không tuyến tính như array/linked list.

from collections import deque


class TreeNode:
    """Node của cây nhị phân"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# --- Xây dựng cây mẫu ---
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6
#    /
#   7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)

print("=== Cây mẫu ===")
print("        1")
print("       / \\")
print("      2   3")
print("     / \\   \\")
print("    4   5   6")
print("   /")
print("  7")

# ==============================
# DUYỆT CÂY (TREE TRAVERSAL)
# ==============================

# --- Preorder: Node -> Left -> Right (NLR) ---
def preorder_recursive(node):
    """Duyệt tiền thứ tự - đệ quy"""
    if node is None:
        return []
    return [node.val] + preorder_recursive(node.left) + preorder_recursive(node.right)


def preorder_iterative(node):
    """Duyệt tiền thứ tự - dùng stack"""
    if node is None:
        return []
    result, stack = [], [node]
    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.right:   # Đẩy right vào trước
            stack.append(cur.right)
        if cur.left:    # Đẩy left vào sau -> left được pop trước
            stack.append(cur.left)
    return result


# --- Inorder: Left -> Node -> Right (LNR) ---
def inorder_recursive(node):
    """Duyệt trung thứ tự - đệ quy"""
    if node is None:
        return []
    return inorder_recursive(node.left) + [node.val] + inorder_recursive(node.right)


def inorder_iterative(node):
    """Duyệt trung thứ tự - dùng stack"""
    result, stack = [], []
    cur = node
    while cur or stack:
        while cur:           # Đi hết nhánh trái
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()    # Lấy node ra
        result.append(cur.val)
        cur = cur.right      # Qua nhánh phải
    return result


# --- Postorder: Left -> Right -> Node (LRN) ---
def postorder_recursive(node):
    """Duyệt hậu thứ tự - đệ quy"""
    if node is None:
        return []
    return postorder_recursive(node.left) + postorder_recursive(node.right) + [node.val]


def postorder_iterative(node):
    """Duyệt hậu thứ tự - dùng 2 stack"""
    if node is None:
        return []
    result, stack = [], [node]
    while stack:
        cur = stack.pop()
        result.append(cur.val)
        if cur.left:
            stack.append(cur.left)
        if cur.right:
            stack.append(cur.right)
    return result[::-1]  # Đảo ngược kết quả


# --- Level-order: Từng mức từ trên xuống, trái qua phải ---
def level_order(node):
    """Duyệt theo mức (BFS)"""
    if node is None:
        return []
    result, q = [], deque([node])
    while q:
        cur = q.popleft()
        result.append(cur.val)
        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)
    return result


def level_order_by_level(node):
    """Duyệt theo mức, nhóm kết quả theo từng mức"""
    if node is None:
        return []
    result, q = [], deque([node])
    while q:
        level = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        result.append(level)
    return result


print("\n=== Kết quả duyệt cây ===")
print("Preorder  (NLR):", preorder_recursive(root))
print("  Iterative:     ", preorder_iterative(root))
print("Inorder   (LNR):", inorder_recursive(root))
print("  Iterative:     ", inorder_iterative(root))
print("Postorder (LRN):", postorder_recursive(root))
print("  Iterative:     ", postorder_iterative(root))
print("Level-order:     ", level_order(root))
print("Level by level:  ", level_order_by_level(root))

# ==============================
# THUỘC TÍNH CÂY
# ==============================

def tree_height(node):
    """Chiều cao của cây (số cạnh từ gốc đến lá xa nhất)"""
    if node is None:
        return -1  # Cây rỗng: height = -1; 1 node: height = 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node):
    """Số lượng node trong cây"""
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


def count_leaves(node):
    """Đếm số lá (node không có con)"""
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)


def is_full_binary_tree(node):
    """Cây nhị phân đầy đủ: mỗi node có 0 hoặc 2 con"""
    if node is None:
        return True
    if (node.left is None) != (node.right is None):  # Có 1 con -> không đầy đủ
        return False
    return is_full_binary_tree(node.left) and is_full_binary_tree(node.right)


def is_perfect_tree(node):
    """Cây nhị phân hoàn hảo: tất cả lá cùng mức, node trong có 2 con"""
    if node is None:
        return True
    # Đếm số node và chiều cao, kiểm tra 2^h - 1 = size
    # Hoặc kiểm tra chiều cao trái = chiều cao phải
    def check(n):
        if n is None:
            return (0, True)  # (depth, is_perfect)
        left_d, left_p = check(n.left)
        right_d, right_p = check(n.right)
        return (max(left_d, right_d) + 1,
                left_p and right_p and left_d == right_d)
    return check(node)[1]


print("\n=== Thuộc tính cây ===")
print("Chiều cao (height):", tree_height(root))     # 3
print("Số node (size):    ", tree_size(root))       # 7
print("Số lá (leaves):    ", count_leaves(root))    # 3 (5, 6, 7)
print("Full binary?:      ", is_full_binary_tree(root))
print("Perfect?:          ", is_perfect_tree(root))

# ==============================
# CÂY NHỊ PHÂN BIỂU DIỄN BẰNG MẢNG
# ==============================
# Node tại index i:
#   - Con trái:  2*i + 1
#   - Con phải:  2*i + 2
#   - Cha:       (i-1)//2

print("\n=== Biểu diễn cây bằng mảng ===")
# Cây         1
#           /   \
#          2     3
#         / \   /
#        4   5 6
tree_array = [1, 2, 3, 4, 5, 6]
print("Mảng:", tree_array)
print("Con của 2 (index 1):")
print("  left  = tree_array[2*1+1] =", tree_array[2*1+1] if 2*1+1 < len(tree_array) else "none")  # 4
print("  right = tree_array[2*1+2] =", tree_array[2*1+2] if 2*1+2 < len(tree_array) else "none")  # 5
print("Con của 3 (index 2):")
print("  left  = tree_array[2*2+1] =", tree_array[2*2+1] if 2*2+1 < len(tree_array) else "none")  # 6
print("  right = tree_array[2*2+2] =", tree_array[2*2+2] if 2*2+2 < len(tree_array) else "none")  # none

# --- Cây hoàn chỉnh (Complete Binary Tree) ---
# Mọi mức được lấp đầy trừ mức cuối, mức cuối lấp từ trái sang
# CBT luôn có thể biểu diễn gọn bằng mảng (như heap)

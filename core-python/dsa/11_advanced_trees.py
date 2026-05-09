# ============================================
# 11. ADVANCED TREES - CÂY NÂNG CAO / ADVANCED TREES
# ============================================
# Red-Black Tree: BST tự cân bằng, dùng trong std::map, TreeMap.
# B-Tree: cây tổng quát cho database/ filesystem indexing.
# N-ary Tree: mỗi node có nhiều con.
# Huffman Tree: cây mã hóa tối ưu cho nén dữ liệu.

import heapq
from collections import deque


# ==============================
# RED-BLACK TREE (Khái niệm + Demo nhẹ)
# ==============================
# 5 tính chất:
# 1. Mỗi node là ĐỎ hoặc ĐEN
# 2. Gốc luôn ĐEN
# 3. Lá (NIL) luôn ĐEN
# 4. Không có 2 node ĐỎ liền kề (con của node đỏ phải là đen)
# 5. Mọi đường từ gốc đến lá có cùng số node ĐEN (Black Height)

print("=== Red-Black Tree (Overview) ===")
print("""
Tính chất RB Tree:
  1. Node màu ĐỎ hoặc ĐEN
  2. Gốc ĐEN
  3. Lá (NIL) ĐEN
  4. Không 2 ĐỎ liền kề
  5. Mọi đường gốc->lá có cùng số node ĐEN

Insert: O(log n), max 2 rotations
Delete: O(log n), max 3 rotations

Cây RB lỏng hơn AVL (ít rotation hơn khi insert/delete)
  -> Dùng trong: std::map (C++), TreeMap (Java), Linux kernel
""")

# Simplified RB visualization
class RBNode:
    """Node cây Đỏ-Đen (đơn giản)"""
    def __init__(self, val, color="RED"):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.color = color  # "RED" hoặc "BLACK"


def rb_insert_visualization():
    """Minh họa các case insert của Red-Black tree"""
    print("Các case insert trong Red-Black Tree:")
    print("  Case 1: Chú (uncle) ĐỎ -> đổi màu")
    print("  Case 2: Chú ĐEN, node zig-zag -> xoay để thành Case 3")
    print("  Case 3: Chú ĐEN, node thẳng hàng -> xoay + đổi màu")
    print("Sau insert: luôn đảm bảo 5 tính chất trên.")


rb_insert_visualization()

# ==============================
# B-TREE (Khái niệm)
# ==============================
print("\n=== B-Tree (Overview) ===")
print("""
B-Tree bậc m:
  - Mỗi node có tối đa m con
  - Mỗi node (trừ gốc) có ít nhất ceil(m/2) con
  - Tất cả lá cùng độ sâu
  - Node chứa các key đã sắp xếp

B-Tree dùng cho disk-based storage:
  - Mỗi node = 1 disk page
  - Giảm số lần đọc/ghi đĩa

B+ Tree (biến thể phổ biến):
  - Chỉ lá mới chứa data
  - Các lá nối với nhau thành linked list -> range query nhanh
  - Dùng trong: MySQL (InnoDB), PostgreSQL, hầu hết filesystem
""")


class BTreeNode:
    """Node B-Tree bậc m (minh họa)"""
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []        # Danh sách key đã sắp xếp
        self.children = []    # Danh sách con (len = len(keys) + 1)


def btree_split_demo():
    """Minh họa split node trong B-Tree"""
    print("Split node trong B-Tree bậc 3 (2-3 tree):")
    print("  Khi node đầy (2 keys), thêm key thứ 3:")
    print("  [10, 20] + 15 -> [10] [15] [20]")
    print("                          ^key giữa được đẩy lên cha")
    print("                    [10]   [20]")
    print("                    /  \\  /  \\")
    print("                  con1  con2  con3")


btree_split_demo()

# ==============================
# N-ARY TREE (Cây tổng quát)
# ==============================

class NaryNode:
    """Node cho cây N-ary"""
    def __init__(self, val):
        self.val = val
        self.children = []


def nary_preorder(node):
    """Duyệt tiền thứ tự cây N-ary"""
    if node is None:
        return []
    result = [node.val]
    for child in node.children:
        result.extend(nary_preorder(child))
    return result


def nary_level_order(node):
    """Duyệt theo mức cây N-ary"""
    if node is None:
        return []
    result, q = [], deque([node])
    while q:
        cur = q.popleft()
        result.append(cur.val)
        for child in cur.children:
            q.append(child)
    return result


print("\n=== N-ary Tree ===")
# Xây cây N-ary:   1
#                 / | \
#                2  3  4
#               / \    |
#              5   6   7
nary_root = NaryNode(1)
nary_root.children = [NaryNode(2), NaryNode(3), NaryNode(4)]
nary_root.children[0].children = [NaryNode(5), NaryNode(6)]
nary_root.children[2].children = [NaryNode(7)]

print("Cây N-ary:")
print("       1")
print("     / | \\")
print("    2  3  4")
print("   / \\    |")
print("  5   6   7")
print("Preorder:", nary_preorder(nary_root))
print("Level-order:", nary_level_order(nary_root))

# ==============================
# HUFFMAN TREE (Cây mã hóa Huffman)
# ==============================

class HuffmanNode:
    """Node của cây Huffman"""
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    """Xây dựng cây Huffman từ văn bản"""
    # Đếm tần suất
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    # Tạo heap các node
    heap = [HuffmanNode(ch, f) for ch, f in freq.items()]
    heapq.heapify(heap)

    # Ghép 2 node nhỏ nhất đến khi còn 1 node
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0] if heap else None


def generate_huffman_codes(root):
    """Tạo mã Huffman từ cây"""
    codes = {}

    def dfs(node, code):
        if node is None:
            return
        if node.char is not None:  # Lá
            codes[node.char] = code
            return
        dfs(node.left, code + "0")
        dfs(node.right, code + "1")

    dfs(root, "")
    return codes


def huffman_encode(text, codes):
    """Mã hóa văn bản bằng mã Huffman"""
    return "".join(codes[ch] for ch in text)


def huffman_decode(encoded, root):
    """Giải mã chuỗi Huffman"""
    if root is None:
        return ""
    result = []
    node = root
    for bit in encoded:
        node = node.left if bit == "0" else node.right
        if node.char is not None:
            result.append(node.char)
            node = root
    return "".join(result)


print("\n=== Huffman Coding ===")
text = "aababcabcd"
print(f"Văn bản: '{text}' ({len(text)} ký tự)")

root = build_huffman_tree(text)
codes = generate_huffman_codes(root)
print("Bảng mã Huffman:")
for ch, code in sorted(codes.items()):
    print(f"  '{ch}' -> {code}")

encoded = huffman_encode(text, codes)
print(f"Encoded ({len(encoded)} bits): {encoded}")
print(f"Tỉ lệ nén: {len(text)*8} bits -> {len(encoded)} bits ({(1-len(encoded)/(len(text)*8))*100:.1f}%)")

decoded = huffman_decode(encoded, root)
print(f"Decoded: '{decoded}'")
print(f"Khớp: {decoded == text}")

# --- Demo nén với text dài hơn ---
print("\n--- Demo nén text dài ---")
long_text = "this is an example of a huffman tree for data compression"
print(f"Original: '{long_text}'")
huff_root = build_huffman_tree(long_text)
huff_codes = generate_huffman_codes(huff_root)
huff_encoded = huffman_encode(long_text, huff_codes)
original_bits = len(long_text) * 8
compressed_bits = len(huff_encoded)
print(f"Nén: {original_bits} bits -> {compressed_bits} bits (tiết kiệm {(1-compressed_bits/original_bits)*100:.1f}%)")

# ============================================
# 9. TRIE - CÂY TIỀN TỐ / TRIE (PREFIX TREE)
# ============================================
# Trie = cây lưu trữ tập hợp các string.
# Mỗi node là 1 ký tự. Đường đi từ gốc đến node = 1 prefix.
# Dùng cho: autocomplete, spell checker, IP routing, từ điển.


class TrieNode:
    """Node của Trie"""
    def __init__(self):
        self.children = {}           # char -> TrieNode
        self.is_end = False          # Đánh dấu kết thúc từ
        self.count = 0               # Số từ đi qua node này (cho autocomplete)


class Trie:
    """Cây tiền tố (Prefix Tree)"""

    def __init__(self):
        self.root = TrieNode()

    # --- Insert ---
    def insert(self, word):
        """Chèn từ vào trie - O(len(word))"""
        node = self.root
        node.count += 1
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    # --- Search ---
    def search(self, word):
        """Tìm chính xác từ - O(len(word))"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    # --- Starts With (Prefix) ---
    def starts_with(self, prefix):
        """Kiểm tra có từ nào bắt đầu bằng prefix không - O(len(prefix))"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

    def count_prefix(self, prefix):
        """Đếm số từ có prefix này - O(len(prefix))"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.count

    # --- Delete ---
    def delete(self, word):
        """Xóa từ khỏi trie - O(len(word))"""
        if not self.search(word):
            return False
        self._delete(self.root, word, 0)
        return True

    def _delete(self, node, word, depth):
        if depth == len(word):
            node.is_end = False
            node.count -= 1
            return len(node.children) == 0  # Trả về True nếu node không còn con

        ch = word[depth]
        should_delete = self._delete(node.children[ch], word, depth + 1)
        node.count -= 1

        if should_delete:
            del node.children[ch]
            return len(node.children) == 0 and not node.is_end
        return False

    # --- Autocomplete ---
    def autocomplete(self, prefix, limit=10):
        """Gợi ý tất cả từ bắt đầu bằng prefix"""
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        result = []
        self._collect_words(node, prefix, result, limit)
        return result

    def _collect_words(self, node, prefix, result, limit):
        """DFS thu thập tất cả từ từ node hiện tại"""
        if len(result) >= limit:
            return
        if node.is_end:
            result.append(prefix)
        for ch, child in node.children.items():
            self._collect_words(child, prefix + ch, result, limit)

    # --- Lấy tất cả từ trong trie ---
    def get_all_words(self):
        """Trả về tất cả từ trong trie"""
        return self.autocomplete("", limit=float('inf'))


# ==============================
# Demo
# ==============================
print("=== Trie (Prefix Tree) ===")
trie = Trie()
words = ["cat", "car", "card", "care", "dog", "dot", "do", "bat", "ball"]
for w in words:
    trie.insert(w)
print(f"Inserted: {words}")

print("\n--- Search ---")
print("Search 'cat':", trie.search("cat"))
print("Search 'car':", trie.search("car"))
print("Search 'cargo':", trie.search("cargo"))  # False
print("Search 'do':", trie.search("do"))

print("\n--- Prefix ---")
print("Starts with 'ca':", trie.starts_with("ca"))
print("Count prefix 'ca':", trie.count_prefix("ca"))  # cat, car, card, care = 4
print("Count prefix 'do':", trie.count_prefix("do"))  # dog, dot, do = 3
print("Starts with 'xyz':", trie.starts_with("xyz"))  # False

print("\n--- Autocomplete ---")
print("Gợi ý cho 'ca':", trie.autocomplete("ca"))
print("Gợi ý cho 'd':", trie.autocomplete("d"))
print("Gợi ý cho 'b':", trie.autocomplete("b"))

print("\n--- Delete ---")
trie.delete("cat")
print("Sau delete 'cat':")
print("  Search 'cat':", trie.search("cat"))
print("  Search 'car':", trie.search("car"))  # Vẫn còn
print("  Autocomplete 'ca':", trie.autocomplete("ca"))

trie.delete("do")
print("Sau delete 'do':")
print("  Search 'do':", trie.search("do"))    # False
print("  Search 'dog':", trie.search("dog"))  # Vẫn còn
print("  Search 'dot':", trie.search("dot"))  # Vẫn còn

print("\n--- All Words ---")
print("Tất cả từ:", trie.get_all_words())

# ==============================
# Ứng dụng: Từ điển kiểm tra chính tả
# ==============================
print("\n=== Ứng dụng: Spell Checker ===")

dictionary = Trie()
vocab = ["python", "java", "javascript", "ruby", "rust", "golang", "typescript"]
for w in vocab:
    dictionary.insert(w)

print("Từ điển:", vocab)
print("'python' đúng chính tả?", dictionary.search("python"))
print("'pythn' đúng chính tả?", dictionary.search("pythn"))  # Sai chính tả
print("Từ gợi ý cho 'py':", dictionary.autocomplete("py"))
print("Từ gợi ý cho 'j':", dictionary.autocomplete("j"))

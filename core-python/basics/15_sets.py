# Set - tập hợp không trùng lặp, không có thứ tự

s = {1, 2, 3, 3, 2, 1}
print("Set tự loại bỏ trùng:", s)

# Thêm / xóa
s.add(4)
s.remove(1)       # Lỗi nếu không tồn tại
s.discard(10)     # Không lỗi nếu không tồn tại
popped = s.pop()  # Xóa và trả về phần tử ngẫu nhiên
print("Sau thao tác:", s)

# Phép toán tập hợp
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("Hợp (union):", a | b)
print("Giao (intersection):", a & b)
print("Hiệu (difference):", a - b)
print("Khác đối xứng (symmetric diff):", a ^ b)

# Kiểm tra
print(2 in a)     # True
print(5 not in a) # True

# Ứng dụng: loại bỏ trùng lặp trong list
nums = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(nums))
print("List sau khi loại trùng:", unique)

# Tuple - giống list nhưng immutable (không thể thay đổi sau khi tạo)

t = (1, 2, 3, "hello", 3.14)

# Truy cập giống list
print(t[0])
print(t[-1])
print(t[1:4])

# Đếm và tìm
print("Số lần xuất hiện của 2:", t.count(2))
print("Vị trí của 'hello':", t.index("hello"))

# Unpacking
a, b, c, d, e = t
print("Unpacked:", a, b, c, d, e)

# Tuple 1 phần tử - cần dấu phẩy
single = (42,)
print(type(single))  # tuple

# Lý do dùng tuple: nhanh hơn list, bảo vệ dữ liệu không bị sửa đổi

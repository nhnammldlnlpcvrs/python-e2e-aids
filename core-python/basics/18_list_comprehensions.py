# List Comprehension - cách viết ngắn gọn để tạo list

# Cách thông thường
squares = []
for i in range(10):
    squares.append(i ** 2)
print("Cách thường:", squares)

# List comprehension
squares_lc = [i ** 2 for i in range(10)]
print("List comprehension:", squares_lc)

# Có điều kiện
evens = [i for i in range(20) if i % 2 == 0]
print("Số chẵn:", evens)

# Biến đổi có điều kiện
labels = ["chẵn" if i % 2 == 0 else "lẻ" for i in range(6)]
print("Labels:", labels)

# Từ list có sẵn
names = ["Nam", "An", "Bình", "Cường"]
uppers = [name.upper() for name in names]
print("Uppercase:", uppers)

# Lọc và biến đổi
long_names = [name for name in names if len(name) >= 4]
print("Tên dài >= 4:", long_names)

# Dictionary comprehension
square_dict = {i: i ** 2 for i in range(5)}
print("Dict:", square_dict)

# Set comprehension
square_set = {i ** 2 for i in range(-3, 4)}
print("Set (không trùng):", square_set)

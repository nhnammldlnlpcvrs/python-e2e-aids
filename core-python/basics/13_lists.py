# List trong Python - mảng động, chứa được nhiều kiểu dữ liệu

# Tạo list
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty = []

# Truy cập phần tử
print(numbers[0])       # Index 0
print(numbers[-1])      # Index cuối
print(numbers[1:4])     # Slice: [2, 3, 4]

# Thêm phần tử
numbers.append(6)       # Thêm vào cuối
numbers.insert(0, 0)    # Thêm vào vị trí 0
numbers.extend([7, 8])  # Thêm nhiều phần tử
print("Sau khi thêm:", numbers)

# Xóa phần tử
numbers.remove(0)       # Xóa giá trị 0 đầu tiên
popped = numbers.pop()  # Xóa và trả về phần tử cuối
numbers.pop(0)          # Xóa phần tử ở index 0
print("Popped:", popped)
print("Sau khi xóa:", numbers)

# Các thao tác khác
print("Độ dài:", len(numbers))
print("3 ở vị trí:", numbers.index(3))
print("Số lần xuất hiện của 4:", numbers.count(4))
numbers.sort(reverse=True)
print("Sắp xếp giảm dần:", numbers)
numbers.reverse()
print("Đảo ngược:", numbers)

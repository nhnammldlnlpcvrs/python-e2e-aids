# Strings trong Python

s = "  Hello, Python World!  "

# Indexing & slicing
print(s[0])        # Ký tự đầu tiên
print(s[-1])       # Ký tự cuối cùng
print(s[2:7])      # Từ index 2 đến 6
print(s[:5])       # Từ đầu đến index 4
print(s[8:])       # Từ index 8 đến hết
print(s[::-1])     # Đảo ngược chuỗi

# String methods
print(s.strip())          # Xóa khoảng trắng 2 đầu
print(s.lower())          # Chữ thường
print(s.upper())          # Chữ hoa
print(s.replace("Hello", "Xin chào"))  # Thay thế
print(s.split(","))       # Tách chuỗi thành list
print(s.find("Python"))   # Tìm vị trí

# f-string (Python 3.6+)
name = "Nam"
age = 18
print(f"Tên: {name}, Tuổi: {age}")
print(f"5 + 3 = {5 + 3}")

# Kiểm tra nội dung
print("123".isdigit())    # True
print("abc".isalpha())    # True
print("abc123".isalnum()) # True
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True

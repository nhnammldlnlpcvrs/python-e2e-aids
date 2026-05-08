# File I/O - Đọc và ghi file

# Ghi file
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Dòng 1\n")
    f.write("Dòng 2\n")
    f.writelines(["Dòng 3\n", "Dòng 4\n"])

# Đọc toàn bộ file
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print("Toàn bộ file:\n" + content)

# Đọc từng dòng
with open("sample.txt", "r", encoding="utf-8") as f:
    print("Từng dòng:")
    for line in f:
        print(line.strip())

# Đọc thành list các dòng
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print("List các dòng:", lines)

# Append (ghi thêm vào cuối)
with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("Dòng append\n")

# Các mode: r (read), w (write), a (append), r+ (read+write)

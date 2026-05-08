# Dictionary - lưu trữ key-value

person = {
    "name": "Nam",
    "age": 18,
    "city": "Hà Nội"
}

# Truy cập
print(person["name"])
print(person.get("age"))
print(person.get("job", "Không có"))  # Trả về default nếu key không tồn tại

# Thêm / sửa / xóa
person["job"] = "Developer"   # Thêm cặp mới
person["age"] = 19            # Sửa giá trị
del person["city"]            # Xóa key
popped = person.pop("job")    # Xóa và trả về giá trị
print("Popped:", popped)
print(person)

# Duyệt dictionary
for key in person:
    print(key, "->", person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Chỉ lấy keys hoặc values
print("Keys:", list(person.keys()))
print("Values:", list(person.values()))

# Dictionary lồng nhau
students = {
    "SV001": {"name": "Nam", "score": 8.5},
    "SV002": {"name": "An", "score": 9.0},
}
print("Điểm SV001:", students["SV001"]["score"])

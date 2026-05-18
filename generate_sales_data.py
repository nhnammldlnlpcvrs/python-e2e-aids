"""
Script tạo file dữ liệu giả lập 'sales_data.csv' để thực hành Pandas.
Chạy script này trước khi mở notebook 02_learn_pandas.ipynb.
"""

import random
import csv
from datetime import datetime, timedelta

# ── Thiết lập random seed để kết quả có thể tái lập ──────────────────────
random.seed(42)

# ── Dữ liệu mẫu ───────────────────────────────────────────────────────────
CATEGORIES = {
    "Điện tử": ["iPhone 15", "Samsung Galaxy S24", "MacBook Air", "Tai nghe AirPods", "Loa Bluetooth"],
    "Gia dụng": ["Nồi cơm điện", "Máy xay sinh tố", "Quạt điều hòa", "Bếp từ", "Ấm siêu tốc"],
    "Thời trang": ["Áo sơ mi", "Quần jean", "Giày sneaker", "Túi xách da", "Đồng hồ"],
    "Thực phẩm": ["Cà phê hòa tan", "Bánh quy", "Sữa tươi", "Mì gói", "Dầu ô liu"],
    "Văn phòng": ["Bút bi", "Giấy A4", "Sổ tay", "Ghim bấm", "Băng keo"],
}

# Ghép tất cả sản phẩm thành danh sách phẳng kèm danh mục
ALL_PRODUCTS = []
for cat, products in CATEGORIES.items():
    for p in products:
        ALL_PRODUCTS.append((p, cat))

# ── Hàm sinh ngày ngẫu nhiên trong năm 2025 ───────────────────────────────
def random_date():
    start = datetime(2025, 1, 1)
    end = datetime(2025, 12, 31)
    delta = (end - start).days
    random_days = random.randint(0, delta)
    return (start + timedelta(days=random_days)).strftime("%Y-%m-%d")

# ── Sinh 100 dòng dữ liệu ─────────────────────────────────────────────────
rows = []
for _ in range(100):
    product, category = random.choice(ALL_PRODUCTS)
    date = random_date()
    quantity = random.randint(1, 10)
    price = random.choice([150_000, 250_000, 350_000, 500_000, 750_000, 1_200_000, 2_500_000])
    is_vip = random.choice([True, False])

    rows.append([date, product, category, quantity, price, is_vip])

# ── Cố tình chèn Missing Values (NaN) ─────────────────────────────────────
# Khoảng 5 dòng sẽ bị mất giá ở các cột khác nhau
rows[10][2] = ""          # Mất Category
rows[25][3] = ""          # Mất Quantity
rows[40][4] = ""          # Mất Price
rows[60][2] = ""          # Mất Category
rows[75][5] = ""          # Mất Is_VIP
rows[88][1] = ""          # Mất Product
rows[95][3] = ""          # Mất Quantity

# ── Cố tình chèn dữ liệu trùng lặp (Duplicate) ────────────────────────────
# Copy nguyên dòng 5 thành dòng 101, dòng 20 thành dòng 102, dòng 50 thành 103
rows.append(rows[5][:])   # Trùng với dòng 5
rows.append(rows[20][:])  # Trùng với dòng 20
rows.append(rows[50][:])  # Trùng với dòng 50
rows.append(rows[77][:])  # Trùng với dòng 77

# ── Ghi ra file CSV ───────────────────────────────────────────────────────
HEADERS = ["Ngay", "San_Pham", "Danh_Muc", "So_Luong", "Gia_Ban", "Is_VIP"]

with open("sales_data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(HEADERS)
    writer.writerows(rows)

print(f"[OK] Da tao file 'sales_data.csv' voi {len(rows)} dong (gom header).")
print("     - Co ~7 o du lieu bi thieu (NaN).")
print("     - Co 4 dong bi trung lap.")
print("     - Hay mo notebook 02_learn_pandas.ipynb de bat dau thuc hanh!")

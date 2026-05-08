# break, continue, pass

# break: thoát khỏi vòng lặp ngay lập tức
for i in range(10):
    if i == 5:
        break
    print("break loop:", i)

print("---")

# continue: bỏ qua lượt hiện tại, nhảy sang lượt tiếp theo
for i in range(10):
    if i % 2 == 0:
        continue
    print("continue loop (odd):", i)

print("---")

# pass: placeholder - không làm gì cả
for i in range(3):
    if i == 1:
        pass  # chưa biết viết gì, để sau
    print("pass loop:", i)

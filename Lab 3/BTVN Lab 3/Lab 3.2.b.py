tong = 0
for i in range(500,1001):
    if i % 4 == 0 and i % 6 != 0:
        tong += i
print("Tổng các số chia hết cho 4 nhưng không chia hết cho 6 trong khoảng từ 500 đến 1000 là: ", tong)
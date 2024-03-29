tong = 0
for i in range(2000,4001):
    if i % 7 == 0 and i % 5 !=0:
        tong += i
print("Tổng các số chia hết cho 7 nhưng không chia hết cho 5 trong khoảng từ 2000 đến 4000 là: ", tong)
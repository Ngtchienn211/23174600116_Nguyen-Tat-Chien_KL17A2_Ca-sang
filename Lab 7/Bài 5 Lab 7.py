kho = {
    "banana": 6,
    "apple": 5,
    "orange": 32,
    "pear": 15
}

gia_tien = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

hoa_don = {}
tong_tien = 0

mua_hang = {
    "banana": 3,
    "apple": 2,
    "orange": 12,
    "pear": 6
}

print("Hóa đơn mua hàng:")
print("Mặt hàng".ljust(10), "Số lượng".ljust(10), "Đơn giá".ljust(10), "Số tiền".ljust(10))
for mat_hang, so_luong in mua_hang.items():
    don_gia = gia_tien[mat_hang]
    so_tien = don_gia * so_luong
    tong_tien += so_tien
    hoa_don[mat_hang] = {"Số lượng": so_luong, "Đơn giá": don_gia, "Số tiền": so_tien}
    print(mat_hang.ljust(10), str(so_luong).ljust(10), str(don_gia).ljust(10), str(so_tien).ljust(10))

print("\nTổng số tiền của hóa đơn:", tong_tien)

print("\nSố lượng của các mặt hàng trong kho sau khi bán:")
for mat_hang, so_luong in kho.items():
    print(mat_hang + ":", so_luong - mua_hang.get(mat_hang, 0))

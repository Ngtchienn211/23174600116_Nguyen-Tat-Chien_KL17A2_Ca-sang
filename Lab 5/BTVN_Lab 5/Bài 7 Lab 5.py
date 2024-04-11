str = input("Nhập chuỗi cần kiểm tra: ")
chu_thuong = 0
chu_hoa = 0
chu_so = 0
ky_tu_dac_biet = 0

for ky_tu in str:
    if ky_tu.islower():
        chu_thuong += 1
    elif ky_tu.isupper():
        chu_hoa += 1
    elif ky_tu.isdigit():
        chu_so += 1
    else:
        ky_tu_dac_biet += 1

print("Số lượng chữ thường:", chu_thuong)
print("Số lượng chữ hoa:", chu_hoa)
print("Số lượng chữ số:", chu_so)
print("Số lượng ký tự đặc biệt:", ky_tu_dac_biet)

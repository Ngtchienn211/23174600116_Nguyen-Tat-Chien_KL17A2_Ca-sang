chuoi = input("Nhập chuỗi ký tự: ")
chuoi_so = ''
for char in chuoi:
    if char.isdigit():
        chuoi_so += char
if chuoi_so:
    so_nguyen = int(chuoi_so)
    if so_nguyen > 1:
        for i in range(2, int(so_nguyen/2) + 1):
            if so_nguyen % i == 0:
                print("Chuỗi ký tự sau khi loại bỏ ký tự không phải số:", chuoi_so)
                print("Đây không phải là số nguyên tố.")
                break
        else:
            print("Chuỗi ký tự sau khi loại bỏ ký tự không phải số:", chuoi_so)
            print("Đây là số nguyên tố.")
    else:
        print("Chuỗi ký tự sau khi loại bỏ ký tự không phải số:", chuoi_so)
        print("Đây không phải là số nguyên tố.")
else:
    print("Chuỗi không chứa số nguyên.")

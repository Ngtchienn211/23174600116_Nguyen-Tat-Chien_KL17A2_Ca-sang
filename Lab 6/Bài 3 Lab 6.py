str = input("Nhập vào một dãy số, cách nhau bằng dấu phẩy: ")
num = [float(x) for x in str.split(',')]
if not num:
    print("Dãy số không có phần tử.")
else:
    min_num = max_num = num[0]
    for num in num:
        if num < min_num:
            min_num = num
        elif num > max_num:
            max_num = num
    print("Số nhỏ nhất là:", min_num)
    print("Số lớn nhất là:", max_num)

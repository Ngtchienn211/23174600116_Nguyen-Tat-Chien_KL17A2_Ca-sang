so = int(input("Mời nhập số cần kiểm tra: "))
so_lan = 0
while so > 0:
    so //= 10
    so_lan += 1
    if so == 0:
        break
print(f"Số đã nhập có {so_lan} chữ số")
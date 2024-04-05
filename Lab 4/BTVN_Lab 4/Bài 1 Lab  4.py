#Bài 1 
tong = 0
so_lan_nhap = 0
while tong <= 1000:
    so = int(input("Nhập số nguyên dương: "))
    tong += so
    so_lan_nhap += 1
print("\nCác số lẻ đã nhập là: ")
if so % 2 != 0:
    print (so, end = ' ')
print("\nCác số chẵn đã nhập là: ")
if so % 2 == 0:
    print(so, end = ' ')
    
#Bài 1.b
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("Số n phải là số nguyên dương lớn hơn 0. Mời nhập lại: "))
a = 0
for i in range(1, n+1):
    a += 1/i
print("Tổng của dãy S2 là: ", a)
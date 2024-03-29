#Bài 1.c
n = int(input("Nhập số nguyên dương n: "))
if n<4:
    n = int(input("Số n phải là số lớn hơn hoặc bằng 4. Mời nhập lại n: "))
a=0
for i in range(1, n+1):
    a += 1/(2*i)**0.5
print("Tổng của dãy S3 là: ", a)
#Bài 1.a
n = int(input("Nhập số nguyên dương n: "))
if n<=0:
    n = int(input("n phải là số nguyên dương lớn hơn 0. Vui lòng nhập lại n: "))
c = 0
for i in range (1, n+1):
    c += i
print("Tổng của dãy S1 là: ", c)
    

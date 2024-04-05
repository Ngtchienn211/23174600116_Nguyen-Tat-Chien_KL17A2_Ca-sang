n = int(input("Nhập vào số n (n>10): "))
while n <= 10:
    n = int(input("Vui lòng nhập n>10: "))
#a
a = 1
S1 = 0
while a <= n:
    S1 += 6**a 
    a += 1
    if a > n:
        break
print("Giá trị của S1 là", S1)

#b
b = 0
S2 = 0
while a <= n:
    S2 += 1/(3**(2*b+1))
    b += 1
    if b > n:
        break
print("Giá trị của S2 = ", S2)

#c
c = 1
S3 = 0
while True:
    S3 += ((-1) ** c) * (c ** 2)
    c += 1
    if abs(S3) > n:
        break
print("Giá trị của S3 = ", S3)

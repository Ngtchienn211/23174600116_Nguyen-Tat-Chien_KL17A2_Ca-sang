a = 1
b = 0
c = 0
d = 1
#a
print("Các số nguyên tố nhỏ hơn 100 là: ")
while a < 100:
    print(a, end = ' ')
    a += 1  

#b
print("\nCác số chính phương bé hơn 100 là: ")
while b < 100:
    r = int(b ** 0.5)
    if r * r == b:
        print(b, end = ' ')
    b += 1

#c
print("\nCác số Fibonacci nhỏ hơn 1000 là: ")
print(c)
while d < 1000:
    print(d)
    c, d = d, c + d

#1
def cubesum(n):
    return sum(int(digit) ** 3 for digit in str(n))
x = int(input("Nhập vào số nguyên n: "))
print(f"Tổng lập phương của chữ số n là: {cubesum(x)}")

#2.a
def PrintArmstrong():
    Armstrong = []
    for i in range(2000):
        if cubesum(i) == i:
            Armstrong.append((cubesum(i)))
    return Armstrong
print(f"Các số Armstrong dưới 1000 là: {PrintArmstrong()}")


#2.b
def isArmstrong(n):
    if cubesum(n) == n:
        return True
    else:
        return False
n = int(input("Nhập số cần kiểm tra: "))
print(f"Số {n} có phải số Armstrong không? {isArmstrong(n)}")

print("Các số nguyên tố từ 100 đến 1000 là: ")
for num in range(100, 1001):
    if num > 1:
        so = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                so = False
                break
        if so:
            print(num, end="  ")
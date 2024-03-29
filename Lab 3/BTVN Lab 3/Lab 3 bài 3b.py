print("Các số chính phương từ 1 đến 1000 là: ")
for i in range(1, 1001):
    if i ** 0.5 == int(i**0.5):
        print(i, end="  ")
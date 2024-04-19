n = int(input("Nhập số lượng phần tử mong muốn: "))
ls = []
for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i + 1}: "))
    ls.append(num)
odd_num = 0
even_num = 0
for num in ls:
    if num % 2 == 0:
        even_num += num
    if num % 2 != 0:
        odd_num += num
print(f"Tổng các số chẵn trong mảng là: {even_num}")
print(f"Tổng các số lẻ trong mảng là: {odd_num}")

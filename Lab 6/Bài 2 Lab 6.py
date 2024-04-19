so = int(input("Nhập số lượng số nguyên mong muốn: "))
dsach =[]
for i in range(so):
    num = int(input(f"Nhập số nguyên thứ {i + 1}: "))
    dsach.append(num)
    
    
#Số nguyên tố
print("Các số nguyên tố có trong mảng là: ")
for num in dsach:
    if num > 1:
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, end = ' ')


#Số hoàn hảo
print("\nCác số hoàn hảo trong mảng là:")
perfect_num = [n for n in dsach if (n > 1 and sum(i for i in range(1, n) if n % i == 0) == n)]
print(perfect_num if perfect_num else "Không có số hoàn hảo trong mảng.")
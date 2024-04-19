n = int(input("Nhập số n: "))

fibonacci = [0, 1] if n > 1 else [0] if n == 1 else []
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Dãy Fibonacci gồm", n, "số đầu tiên là:", fibonacci)

prime = []
for num in range(2, 100):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(num)
print("Danh sách các số nguyên tố nhỏ hơn 100 là:", prime)


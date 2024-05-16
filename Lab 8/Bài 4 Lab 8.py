def sumPdivisors():
    sum = 0
    for i in range(1, n):
        if n % i == 0:
           sum += i  
    return sum
n = 144
print(f"Tổng các ước chính của số {n} là: {sumPdivisors()}")
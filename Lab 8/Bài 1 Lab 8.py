def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True  
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def find_twin_primes(z):
    primes = []
    for num in range(2, z):
        if is_prime(num):
            primes.append(num)
    
    twin_primes = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            twin_primes.append((primes[i], primes[i + 1]))
    
    return twin_primes

z = 1000
twin_primes = find_twin_primes(z)

print("Các số nguyên tố sinh đôi nhỏ hơn 1000 là:")
for prime1, prime2 in twin_primes:
    print(f"({prime1}, {prime2})")

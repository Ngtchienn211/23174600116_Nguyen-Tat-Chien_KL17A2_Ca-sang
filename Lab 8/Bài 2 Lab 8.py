def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def permutations(n, r):
    if n < r:
        return 0
    return factorial(n) // factorial(n - r)

def combinations(n, r):
    if n < r:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

n = 14
r = 6
print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần: p({n}, {r}) = {permutations(n, r)}")
print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần: c({n}, {r}) = {combinations(n, r)}")

def Amicable(a, b):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
           suma += i  
    
    sumb = 0
    for i in range(1, b):
        if b % i == 0:
            sumb += i
    return suma == b and sumb == a

a = 70
b = 180

if Amicable(a, b):
    print(f"Hai số {a} và {b} là số Amicable.")
else:
    print(f"Hai số {a} và {b} không phải số Amicable.")
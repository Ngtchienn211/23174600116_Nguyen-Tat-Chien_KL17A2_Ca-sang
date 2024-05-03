N = input("Nhập vào một số nguyên N: ")
if N.isdigit():
    N = int(N)
    if N <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        Chien_dict = {}
        for i in range(1, N + 1):
            Chien_dict[i] = i ** 3
        
        print("Từ điển với độ dài bằng", N, ":")
        for key, value in Chien_dict.items():
            print(key, "->", value)
else:
    print("Vui lòng nhập một số nguyên.")

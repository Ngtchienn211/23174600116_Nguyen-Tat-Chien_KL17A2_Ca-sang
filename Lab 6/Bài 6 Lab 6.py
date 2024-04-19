#6.1
m1 = int(input("Nhập số hàng của ma trận: "))
n1 = int(input("Nhập số cột của ma trận: "))
print("Nhập các phần tử của ma trận thứ nhất:")
ma_tran1 = []
for i in range(m1):
    hang = []
    for j in range(n1):
        hang.append(float(input(f"Nhập phần tử ở hàng {i + 1} cột {j + 1}: ")))
    ma_tran1.append(hang)
tong = 0
for hang in ma_tran1:
    tong += sum(hang)
print("Tổng của ma trận:", tong)

m2 = int(input("Nhập số hàng của ma trận thứ hai: "))
n2 = int(input("Nhập số cột của ma trận thứ hai: "))
print("Nhập các phần tử của ma trận thứ hai:")
ma_tran2 = []
for i in range(m2):
    hang = []
    for j in range(n2):
        hang.append(float(input(f"Nhập phần tử ở hàng {i + 1} cột {j + 1}: ")))
    ma_tran2.append(hang)

if n1 != m2:
    print("Không thể tính tích của hai ma trận.")
else:
    k = len(ma_tran2[0])
    tich = [[0] * k for _ in range(m1)]
    for i in range(m1):
        for j in range(k):
            for l in range(len(ma_tran2)):
                tich[i][j] += ma_tran1[i][l] * ma_tran2[l][j]
    print("Tích của hai ma trận:")
    for hang in tich:
        print(hang)

print("Ma trận chuyển vị của ma trận thứ nhất:")
chuyen_vi = [[ma_tran1[j][i] for j in range(len(ma_tran1))] for i in range(len(ma_tran1[0]))]
for hang in chuyen_vi:
    print(hang)





#6.2
n = int(input("Nhập kích thước của ma trận vuông: "))
print("Nhập các phần tử của ma trận vuông:")
ma_tran_vuong = []
for i in range(n):
    hang = []
    for j in range(n):
        hang.append(float(input(f"Nhập phần tử ở hàng {i + 1} cột {j + 1}: ")))
    ma_tran_vuong.append(hang)
    
det = 0
if len(ma_tran_vuong) == 1:
    det = ma_tran_vuong[0][0]
elif len(ma_tran_vuong) == 2:
    det = ma_tran_vuong[0][0] * ma_tran_vuong[1][1] - ma_tran_vuong[0][1] * ma_tran_vuong[1][0]
else:
    for i in range(len(ma_tran_vuong)):
        minor = [hang[:i] + hang[i+1:] for hang in (ma_tran_vuong[1:])]
        det += ((-1) ** i) * ma_tran_vuong[0][i] * (det := sum(minor))
if det == 0:
    print("Ma trận này không có ma trận nghịch đảo.")
else:
    ma_tran_nghich_dao = []
    for i in range(n):
        hang = []
        for j in range(n):
            minor = [hang[:j] + hang[j+1:] for hang in (ma_tran_vuong[:i] + ma_tran_vuong[i+1:])]
            hang.append(((-1) ** (i + j)) * sum(minor) / det)
        ma_tran_nghich_dao.append(hang)

    print("Ma trận nghịch đảo của ma trận vuông:")
    for hang in ma_tran_nghich_dao:
        print(hang)

symmetric = True
for i in range(n):
    for j in range(i + 1, n):
        if ma_tran_vuong[i][j] != ma_tran_vuong[j][i]:
            symmetric = False
            break
if symmetric:
    print("Ma trận vuông này là ma trận đối xứng.")
else:
    print("Ma trận vuông này không phải là ma trận đối xứng.")
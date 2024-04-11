thap_phan = int(input("Nhập vào số thập phân cần chuyển đổi: "))
if thap_phan == 0:
    print("Số nhị phân tương ứng của 0 là: 0")
else:
    nhi_phan = ""
    while thap_phan > 0:
        phan_du = thap_phan % 2
        thap_phan //= 2 
        nhi_phan = str(phan_du) + nhi_phan
    print("Số nhị phân tương ứng của", thap_phan, "là:", nhi_phan)

while True:
    a = float(input("Mời nhập số a: "))
    b = float(input("Mời nhập số b: "))
    print("1. Tính tổng")
    print("2. Tính hiệu")
    print("3. Tính tích")
    print("4. Tính thương")
    print("5. Tính lũy thừa")
    print("6. Tính căn bậc hai")
    choice = int(input("Lựa chọn của bạn (1-6): "))
    
    if choice == 1:
        tong = a + b
        print("Tổng hai số là: ", tong)
    elif choice == 2:
        hieu = a - b
        print("Hiệu hai số là: ", hieu)
    elif choice == 3:
        tich = a * b
        print("Tích của hai số là: ", tich)
    elif choice == 4:
        if b != 0:
            thuong = a / b
            print("Thuương của a chia b là: ", thuong)
        else:
            print("Không thể chia vì b = 0")
    elif choice == 5:
        luy_thua = a**b
        print("Lũy thừa của a và b là: ", luy_thua)
    elif choice == 6:
        can_bac_hai1 = a**0.5
        can_bac_hai2 = b**0.5
        print("Căn bậc hai của số a là: ", can_bac_hai1) 
        print("Căn bậc hai của số b là: ", can_bac_hai2)
    else:
        print("Lựa chọn của bạn không hợp lệ!!")
    
    lap_lai = input("Bạn có muốn tiếp tục chương trình? (Y/N): ").lower()
    if lap_lai != "Y" and lap_lai != "N":
        lap_lai = input("Chỉ được chọn Y/N: ")
    if lap_lai == "N":
        break
    if lap_lai == "Y":
        continue
    


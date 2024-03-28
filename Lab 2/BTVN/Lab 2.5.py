c = int(input("Nhập số người xem phim: "))
n = 120000    #n là giá vé của 1 người
if 2<=c<4:
    gia = (c*n) - (c*n)/100*5
    print("Giá vé là: ", gia)
if 4<=c<10:
    gia = (c*n) - (c*n)/100*15
    print("Giá vé là: ", gia)
if c>=10:
    gia = (c*n) - (c*n)/100*20
    print("Giá vé là: ", gia)
    
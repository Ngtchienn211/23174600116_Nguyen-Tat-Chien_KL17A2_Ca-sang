x = float(input("Nhập điểm số: "))
if x>=0 and x<5:
    print("Điểm kém")
elif x>=5 and x<7:
    print("Điểm trung bình")
elif x>=7 and x<8.5:
    print("Điểm khá")
elif x>=8.5 and x<=10:
    print("Điểm tốt")
else:
    print("Điểm số không hợp lệ!!")

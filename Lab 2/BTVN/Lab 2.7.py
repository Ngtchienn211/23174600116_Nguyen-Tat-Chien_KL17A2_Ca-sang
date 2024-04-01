cao = float(input("Nhập chiều cao (mét): "))
nang = float(input("Nhập cân nặng (kg): "))
bmi = cao/nang**2
if bmi < 18.5:
    print("Gầy")
elif 18.5 <= bmi <= 24.9:
    print("Bình thường")
elif 25 <= bmi <29.9:
    print("Hơi béo")
else:
    print("Béo")
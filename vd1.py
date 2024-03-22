#Bài_1
n = int(input("Nhập vào một năm để kiểm tra: "))
if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("Năm", n, "là năm nhuận!")
else:
    print("Năm", n, "Không là năm nhuận!")


#Bài_2
a,b = map(float, input('Nhập tọa độ tâm I: ').split())
x,y = map(float, input('Nhập tọa độ điểm M: ').split())
r = float(input("Nhập bán kính: "))
import math
d=math.sqrt((x-a)**2 + (y-b)**2)
if d<r:
    print("Điểm M nằm trong đường tròn")
elif d==r:
    print("Điểm M nằm trên đường tròn")
else:
    print("Điểm M nằm ngoài đường tròn")


#Bài_3
a,b,c=map(int,input("Nhập vào số đo của 3 cạch: ").split())
if (a+b>c) and (b+c>a) and (c+a>b):      #Kiểm tra điều kiện tam giác
    if  a==b and b==c and a==c:
    print("Không phải là độ dài 3 canh của tam giác")       #

    
#Bài_4
Viết chương trình tìm ra số lớn nhất trong 3 số bằng Python 
max = a
kiểm tra max có lớn hơn b hay không
kiểm tra max có lớn hơn c hay không
In số lớn nhất trong 3 số
***
print("Nhập các số :", end='')
a,b,c = map(float,input('=').split(','))
max=a


#Bài_5
ky_tu = input("Nhập vào một kí tự:")
if (ky_tu == 'U') or (ky_tu == 'u') or (ky_tu == 'O') or (ky_tu == 'o') or (ky_tu == 'E') or (ky_tu == 'e') or (ky_tu == 'I') or (ky_tu == 'i') or (ky_tu == 'A') or (ky_tu == 'a'):
    print("Ký tự", ky_tu, "là nguyên âm!")
else:
    print("Ký tự", ky_tu, "là phụ âm!")

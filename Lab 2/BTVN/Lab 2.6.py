num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
num3 = int(input("Nhập số thứ ba: "))
if num1 < num2:
     if num2 < num3:
        print("Số", num3, "là số lớn nhất")
     elif num2 == num3:
        print("Số", num2, "là số lớn nhất")    
     else:
        print("Số", num2, "là số lớn nhất")
elif num1 == num2:
     if num1 < num3:
        print("Số", num3, "là số lớn nhất")
     elif num1 == num3:
        print("Số", num1, "là số lớn nhất")    
     else:
        print("Số", num1, "là số lớn nhất")
else:
     if num1 < num3:
        print("Số", num3, "là số lớn nhất")
     elif num1 == num3:
        print("Số", num1, "là số lớn nhất")    
     else:
        print("Số", num1, "là số lớn nhất")
        
        
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

len_str1 = len(str1)
len_str2 = len(str2)
len_min = min(len_str1, len_str2)
chuoi_con_chung = ""

for i in range(len_min):
    if str1[i] == str2[i]:
        chuoi_con_chung += str1[i]
    else:
        break
if chuoi_con_chung:
    print("Chuỗi ký tự con chung ngắn nhất là:", chuoi_con_chung)
else:
    print("Không có chuỗi ký tự con chung ngắn nhất.")

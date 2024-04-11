str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")

str_tron = ''
min_len = min(len(str1), len(str2))

for i in range(min_len):
    str_tron += str1[i] + '-' + str2[i] + '-'
if len(str1) > len(str2):
    str_tron += str1[min_len:]
elif len(str2) > len(str1):
    str_tron += str2[min_len:]
    
if str_tron.endswith('-'):
    str_tron = str_tron[:-1]
print("Chuỗi sau khi trộn:", str_tron)

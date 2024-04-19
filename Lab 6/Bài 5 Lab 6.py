str = input("Nhập vào một dãy các số nguyên, cách nhau bằng dấu phẩy: ")
num = [int(x) for x in str.split(',')]

if len(num) < 2:
    print("Dãy số quá ngắn để tạo thành cấp số cộng.")
else:
    hieu = num[1] - num[0]
    csc = True
    for i in range(2, len(num)):
        if num[i] - num[i-1] != hieu:
            csc = False
            break
    
    if csc:
        print("Dãy số", num, "là một cấp số cộng với công sai là: ",hieu)
    else:
        print("Dãy số", num, "không tạo thành cấp số cộng.")

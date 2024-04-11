chuoi = input("Nhập chuỗi văn bản: ")
tim_kiem = input("Nhập từ cần tìm kiếm: ")

dem = 0
vi_tri_dau_tien = -1
vi_tri = ""
i = 0
while i < len(chuoi):
    if chuoi[i:i+len(tim_kiem)] == tim_kiem:
        dem += 1
        if vi_tri_dau_tien == -1:
            vi_tri_dau_tien = i
        vi_tri += str(i) + ", "
        i += len(tim_kiem) - 1
    i += 1

if dem > 0:
    print("Từ '{}' xuất hiện {} lần.".format(tim_kiem, dem))
    print("Vị trí đầu tiên của từ '{}' là: {}".format(tim_kiem, vi_tri_dau_tien))
    print("Các vị trí của từ '{}' là: {}".format(tim_kiem, vi_tri))
else:
    print("Từ '{}' không xuất hiện trong chuỗi văn bản.".format(tim_kiem))

tu_nhieu_nhat = ""
dem_tu_nhieu_nhat = 0
for word in chuoi.split():
    dem_tu = chuoi.count(word)
    if dem_tu > dem_tu_nhieu_nhat:
        dem_tu_nhieu_nhat = dem_tu
        tu_nhieu_nhat = word
print("Từ xuất hiện nhiều nhất trong chuỗi là: ", tu_nhieu_nhat)

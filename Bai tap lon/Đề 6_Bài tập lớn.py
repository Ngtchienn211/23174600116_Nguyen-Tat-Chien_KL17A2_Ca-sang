import random
import csv

xac_suat_la_bai = {
    '1': 0.1,
    '2': 0.1,
    '3': 0.1,
    '4': 0.1,
    '5': 0.1,
    '6': 0.1,
    '7': 0.1,
    '8': 0.1,
    '9': 0.1,
    '10': 0.1
}

cac_la_bai = []
for la_bai, xac_suat in xac_suat_la_bai.items():
    so_luong = int(xac_suat * 100)  
    cac_la_bai.extend([la_bai] * so_luong)


so_luong_la_bai = 20
random.shuffle(cac_la_bai)
ban_choi = cac_la_bai[:so_luong_la_bai]

cac_cap_la_bai = ban_choi[:]
cac_cap_la_bai.extend(ban_choi)
random.shuffle(cac_cap_la_bai)

vi_tri_lat_bai = set()
diem_so = 0
so_lan_thu = 0
ket_qua_lat_bai = []

def lat_la_bai(vi_tri1, vi_tri2):
    global diem_so, so_lan_thu
    so_lan_thu += 1
    if vi_tri1 in vi_tri_lat_bai or vi_tri2 in vi_tri_lat_bai:
        return False  
    
    vi_tri_lat_bai.add(vi_tri1)
    vi_tri_lat_bai.add(vi_tri2)
    
    if cac_cap_la_bai[vi_tri1] == cac_cap_la_bai[vi_tri2]:
        diem_so += 1
        ket_qua_lat_bai.append((vi_tri1, cac_cap_la_bai[vi_tri1], xac_suat_la_bai[cac_cap_la_bai[vi_tri1]], True))
        ket_qua_lat_bai.append((vi_tri2, cac_cap_la_bai[vi_tri2], xac_suat_la_bai[cac_cap_la_bai[vi_tri2]], True))
        return True  
    else:
        vi_tri_lat_bai.remove(vi_tri1)
        vi_tri_lat_bai.remove(vi_tri2)
        ket_qua_lat_bai.append((vi_tri1, cac_cap_la_bai[vi_tri1], xac_suat_la_bai[cac_cap_la_bai[vi_tri1]], False))
        ket_qua_lat_bai.append((vi_tri2, cac_cap_la_bai[vi_tri2], xac_suat_la_bai[cac_cap_la_bai[vi_tri2]], False))
        return False 

while diem_so < so_luong_la_bai // 2:
    vi_tri1 = random.randint(0, len(cac_cap_la_bai) - 1)
    vi_tri2 = random.randint(0, len(cac_cap_la_bai) - 1)
    while vi_tri1 == vi_tri2:
        vi_tri2 = random.randint(0, len(cac_cap_la_bai) - 1)
    lat_la_bai(vi_tri1, vi_tri2)

with open('ket_qua_choi.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Vị trí lá bài', 'Mã lá bài', 'Xác suất xuất hiện', 'Tìm được cặp (True/False)'])
    for ket_qua in ket_qua_lat_bai:
        writer.writerow(ket_qua)


print(f"Điểm của người chơi: {diem_so}")
print(f"Số lần thử: {so_lan_thu}")

xac_suat_tim_duoc_cap = diem_so / (so_luong_la_bai // 2)
print(f"Xác suất tìm được cặp lá bài giống nhau: {xac_suat_tim_duoc_cap:.2f}")

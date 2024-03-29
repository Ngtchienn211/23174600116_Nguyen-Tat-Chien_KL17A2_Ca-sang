h_tg = 7
w_tg = 13

for i in range(h_tg):
    print(' ' * (w_tg // 2 - i) + '*' * (2 * i + 1))

h_hcn = 3
w_hcn = 3

start_position = (w_tg - w_hcn) // 2 
for _ in range(h_hcn):
    print(' ' * start_position + '*' * w_hcn)

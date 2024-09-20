kode_N = int(input("N = "))
kode_M = int(input("M = "))

arah = 1

for i in range(kode_N):
    if i % 2 == 1:
        arah = -1
    else:
        arah = 1
    
    for j in range(kode_M):
        x = i
        y = j if arah == 1 else kode_M - j - 1
        print(f"MOVE to ({x}, {y})")
N=int(input("Masukkan jumlah baris (N): "))
M=int(input("Masukkan jumlah kolom (M): "))
for baris in range(N):
    if baris%2==0:
        for kolom in range(M):
            print(f"MOVE to ({baris},{kolom})")
    else:
        for kolom in range(M-1,-1,-1):
            print(f"MOVE to ({baris},{kolom})")
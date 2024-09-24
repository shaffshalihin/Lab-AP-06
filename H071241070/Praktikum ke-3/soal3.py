N = int(input("N :")) 
M = int(input("M :"))

for i in range(N): 
    if i % 2 == 0:
        # Jika baris genap, bergerak dari kiri ke kanan
        for j in range(M): 
            print(f"MOVE to ({i},{j})")
    else:
        # Jika baris ganjil, bergerak dari kanan ke kiri
        for j in range(M, 0, -1): 
            print(f"MOVE to ({i},{j-1})")
baris_robot = int(input("N = "))
kolom_robot = int(input("M = "))

for i in range(baris_robot):
    if i % 2 == 0:  #utk mengidentifikasi angka genap dan ganjil
        for j in range(kolom_robot):
            print(f"MOVE to ({i}, {j})")
    else:
        for j in range(kolom_robot - 1, -1, -1):
            print(f"MOVE to ({i}, {j})")
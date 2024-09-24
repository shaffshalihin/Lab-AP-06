# soal 3 prt 3

gridN = int(input("N = "))
gridM = int(input("M = "))

for i in range(gridN):
    if i % 2 == 0:
        for j in range(gridM):
            print(f"Move to ({i}, {j})")
    else:
        for j in range(gridM - 1, -1, -1):
            print(f"Move to ({i}, {j})")
        

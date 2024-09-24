kodeN = int(input("N : "))
kodeM = int(input("M : "))
arah = 1

for i in range(kodeN):
    if i%2 == 1:
        arah = -1
    else:
        arah = 1

    for j in range(kodeM):
        x = i
        y = j if arah == 1 else kodeM - j - 1
        print(f"MOVE to ({x}, {y})")
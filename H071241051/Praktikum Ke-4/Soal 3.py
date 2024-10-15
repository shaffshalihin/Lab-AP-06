def tekateki():
    try:
        n = int(input("Masukan angka = "))
    except ValueError:
        print("Masukan angka yang benar.")
        return  
    langkah = 0  
    while n != 1:  
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        langkah += 1
        print(n)
    print(f"Jumlah langkah yang diperlukan = {langkah}")
tekateki()

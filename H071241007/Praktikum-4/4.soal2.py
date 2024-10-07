def tes_hoki():
    total_langkah = 0
    bahaya = False
    
    while True:
        try:
            langkah = int(input("Masukkan jarak langkah yang ditempuh (meter): "))

            if langkah == 0:
                break


            if langkah > 20:
                print("Langkah terlalu jauh dan berbahaya!")
                bahaya = True

            total_langkah += langkah
            print(f"Total jarak yang telah ditempuh: {total_langkah} meter")

            if total_langkah >= 50:
                break

        except ValueError:
            print("Input tidak valid! Masukkan angka.")

    if bahaya:
        print("Tidak aman untuk menggali harta karun. Coba lagi!")
    elif total_langkah == 50:
        print("Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Tidak menemukan harta karun. Coba lagi!")

tes_hoki()

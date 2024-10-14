def langkah():
    total_distance = 0
    bahaya = False

    while True:
        try:
            langkah = input("Masukkan langkah (meter) atau 0 untuk selesai: ")
            langkah = int(langkah)

            if langkah == 0:
                break

            if langkah < 0:
                print("Input tidak valid. Masukkan bilangan bulat.")
                continue

            if langkah > 20:
                bahaya = True

            total_distance += langkah # total = total + langkah

        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
    
    print(f"Total jarak: {total_distance} meter")
    print(f"Ada bahaya: {'Ya' if bahaya else 'Tidak'}")
    
    if total_distance == 50 and not bahaya:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang!")
    else:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")

langkah()
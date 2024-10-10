def main():
    total_jarak = 0
    bahaya = False

    while True:
        input_user = input("Masukkan langkah (meter) atau 0 untuk selesai: ")

        try:
            langkah = int(input_user)
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue
        
        if langkah == 0:
            break
        elif langkah < 0:
            print("Input tidak valid. Masukkan bilangan bulat.")
            continue
        
        total_jarak += langkah

        # Logika untuk menentukan bahaya
        if langkah > 20:
            bahaya = True

    print(f"Total jarak: {total_jarak} meter")
    print("Ada bahaya :", "Ya" if bahaya else "Tidak")
    
    if bahaya:
        print("Keputusan: Tidak aman untuk menggali harta karun. Coba lagi!")
    else:
        print("Keputusan: Aman! Kamu tepat menemukan harta karun dan menang.")

main()

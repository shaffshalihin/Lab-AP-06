def langkah():
    jarak = 0  
    while True:
        try:
            langkah = int(input("Masukkan jumlah langkah (0 untuk selesai) = "))
        except ValueError:
            print("Input tidak valid, masukkan angka yang benar.")
            continue  
        jarak += langkah
        if langkah > 20 :
            print("Ada bahaya")   
        if langkah == 0:
            print("Permainan selesai.")
            if jarak == 50:
                print("Aman! Kamu dapat menggali.")    
            elif jarak > 50:
                print("Tidak aman untuk menggali harta karun, coba lagi!.")
            break  
    print(f"Total jarak yang telah ditempuh: {jarak} meter.")      
langkah()

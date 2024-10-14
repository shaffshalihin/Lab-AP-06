huruf = input("masukkan huruf yang mau ta cari: ")
kalimat = input("kalimatnya apa bosku?: ")

pesan = (huruf in kalimat and f"huruf {huruf} ada di kalimat {kalimat}") or (f"huruf {huruf} tidak ditemukan di kalimat {kalimat}")

print(pesan)
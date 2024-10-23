import os
import random

# Membersihkan layar
os.system("cls")

print("Selamat datang di Blackjack!")

def buat_deck():
    """Membuat deck kartu yang diacak."""
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"] * 4
    random.shuffle(deck)
    return deck

def hitung_nilai(kartu):
    """Menghitung nilai total dari sebuah list kartu dengan penanganan kartu As."""
    nilai = 0
    jumlah_as = 0
    for kartu_ini in kartu:
        if kartu_ini in ["J", "Q", "K"]:
            nilai += 10
        elif kartu_ini == "A":
            nilai += 11
            jumlah_as += 1
        else:
            nilai += kartu_ini
    
    # Jika nilai kartu melebihi 21 dan ada As, ubah nilai As jadi 1
    while nilai > 21 and jumlah_as:
        nilai -= 10
        jumlah_as -= 1
    
    return nilai

def permainan_Blackjack():
    """Fungsi utama permainan Blackjack."""
    deck = buat_deck()
    pemain_kartu = [deck.pop(), deck.pop()]
    dealer_kartu = [deck.pop(), deck.pop()]
    
    print(f"Kartu Anda sekarang adalah: {pemain_kartu} (Total nilai: {hitung_nilai(pemain_kartu)})")

    # Pemain mengambil kartu tambahan
    while True:
        pilihan = input("Apakah Anda ingin mengambil kartu lagi? (y/n): ")
        if pilihan.lower() == 'y':
            pemain_kartu.append(deck.pop())
            print(f"Kartu Anda sekarang adalah: {pemain_kartu} (Total nilai: {hitung_nilai(pemain_kartu)})")
            if hitung_nilai(pemain_kartu) > 21:
                print("Anda kalah! Nilai kartu Anda melebihi 21.")
                return
        else:
            break

    # Dealer mengambil kartu hingga mencapai 17 atau lebih
    print(f"Kartu dealer adalah: {dealer_kartu[0]} dan satu kartu tersembunyi.")
    while hitung_nilai(dealer_kartu) < 17:
        dealer_kartu.append(deck.pop())

    # Hitung nilai akhir dan tentukan pemenang
    nilai_pemain = hitung_nilai(pemain_kartu)
    nilai_dealer = hitung_nilai(dealer_kartu)

    print(f"Kartu dealer sekarang adalah: {dealer_kartu} (Total nilai: {nilai_dealer})")

    if nilai_pemain > 21:
        print("Anda kalah!")
    elif nilai_dealer > 21:
        print("Anda menang! Dealer melebihi 21.")
    elif nilai_pemain > nilai_dealer:
        print("Anda menang!")
    elif nilai_pemain < nilai_dealer:
        print("Dealer menang!")
    else:
        print("Seri!")

permainan_Blackjack()

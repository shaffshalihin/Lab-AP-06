import random

def kartu_random():
    """Mengambil kartu acak dengan nilai antara 1 sampai 11 (untuk Ace, King, Queen, Jack dianggap sebagai 10)."""
    return random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])

def perlihatkan_kartu(kartu_pemain, kartu_dealer):
    print(f"Kartu Anda sekarang adalah: {kartu_pemain}")
    print(f"Kartu dealer adalah: {kartu_dealer[0]}")

def calculate_total(cards):
    """Menghitung total nilai kartu, memperhitungkan Ace bisa bernilai 1 atau 11."""
    total = sum(cards)

    return total

def blackjack():
    print("Welcome to Blackjack!")
    
    kartu_pemain = [kartu_random()]
    kartu_dealer = [kartu_random()]
    
    perlihatkan_kartu(kartu_pemain, kartu_dealer)

    # Pemain terus mengambil kartu sampai memilih berhenti atau nilainya melebihi 21
    while True:
        player_total = calculate_total(kartu_pemain)
        if player_total > 21:
            print("Anda kalah, kartu anda melebihi 21.")
            return
        
        choice = input("Apakah masih akan mengambil kartu? (y/n): ")
        
        if choice == 'y':
            kartu_pemain.append(kartu_random())
            kartu_pemain[0] = kartu_pemain[0] + kartu_pemain[1]
            del kartu_pemain[1]
            print(f"Kartu Anda sekarang adalah: {kartu_pemain}")
        else:
            break

    # Giliran dealer mengambil kartu
    dealer_total = calculate_total(kartu_dealer)
    print(f"Kartu dealer sekarang adalah: {kartu_dealer}")
    
    while dealer_total < 17:
        kartu_dealer.append(kartu_random())
        kartu_dealer[0] = kartu_dealer[0] + kartu_dealer[1]
        del kartu_dealer[1]
        dealer_total = calculate_total(kartu_dealer)
        print(f"Kartu dealer sekarang adalah: {kartu_dealer}")

    # Menentukan pemenang
    player_total = calculate_total(kartu_pemain)
    dealer_total = calculate_total(kartu_dealer)
    
    if dealer_total > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_total > dealer_total:
        print("Anda menang!")
    elif player_total == dealer_total:
        print("Seri!")
    else:
        print("Dealer menang!")

# Memulai permainan Blackjack
blackjack()
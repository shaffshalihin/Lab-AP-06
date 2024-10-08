import random
def card():
    """Fungsi untuk mengambil kartu acak 1-11."""
    return random.randint(1, 11)

def dealer_turn(dealer_total):
    """Fungsi untuk menentukan apakah dealer akan mengambil kartu tambahan."""
    while dealer_total < 17:
        dealer_total += card() # dealer = dealer + card()
        print(f"Kartu dealer sekarang adalah: {dealer_total}")
    return dealer_total

def blackjack():
    print("Welcome to Blackjack!")
    
    player_total = card()
    dealer_total = card()

    print(f"Kartu anda sekarang adalah: {player_total}")
    
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
        
        if choice == 'y':
            player_total += card() # player = player + card()
            print(f"Kartu anda sekarang adalah: {player_total}")
            
            if player_total > 21:
                print("Anda kalah, kartu anda melebihi 21.")
                return
        elif choice == 'n':
            break
        else:
            print("Input tidak valid, silakan masukkan 'y' atau 'n'.")

    print(f"Kartu dealer adalah: {dealer_total}")
    dealer_total = dealer_turn(dealer_total)
    
    if dealer_total > 21:
        print("Anda menang, dealer melebihi 21.")
    elif player_total > dealer_total:
        print("Anda menang!")
    elif player_total == dealer_total:
        print("Seri!")
    else:
        print("Dealer menang!")

blackjack()
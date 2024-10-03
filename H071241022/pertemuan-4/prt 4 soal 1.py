import random

def draw_card():
    return random.randint(1, 11)

def blackjack():
    print("Welcome to Blackjack!")
    
    # Pemain
    player_cards = []
    player_cards.append(draw_card())
    player_cards.append(draw_card())
    player_total = sum(player_cards)
    
    # Cetak kartu awal pemain
    print(f"Kartu anda sekarang adalah: {player_total}")
    
    while True:
        choice = input("Apakah masih akan mengambil kartu? (y/n) ").lower()
        
        if choice == 'y':
            new_card = draw_card()
            player_cards.append(new_card)
            player_total = sum(player_cards)
            print(f"Kartu anda sekarang adalah: {player_total}")
            if player_total > 21:
                print("Kartu anda melebihi 21, anda kalah!")
                return
        elif choice == 'n':
            break
        else:
            print("Input tidak valid. Harap masukkan 'y' atau 'n'.")
    
    # Dealer
    dealer_cards = [draw_card()]
    dealer_total = sum(dealer_cards)
    print(f"Kartu dealer adalah: {dealer_total}")
    
    while dealer_total < 17:
        dealer_cards.append(draw_card())
        dealer_total = sum(dealer_cards)
        print(f"Kartu dealer sekarang adalah: {dealer_total}")
        
        if dealer_total > 21:
            print("Kartu dealer melebihi 21, anda menang!")
            return
    
    # Menentukan hasil akhir
    if player_total > dealer_total:
        print("Anda menang!")
    elif player_total < dealer_total:
        print("Anda kalah!")
    else:
        print("Seri!")

blackjack()

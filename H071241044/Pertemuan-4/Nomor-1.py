import random

def hit(deck): # pengambilan kartu
	"""Menarik kartu dari dek."""
	print(deck)
	return deck.pop()

def calculate_hand_value(hand): # hitung jumlah nilai kartu
	"""Menghitung nilai total kartu di tangan."""
	value = 0
	ace_count = 0
	for card in hand:
		if card in ['J', 'Q', 'K']:
			value += 10
		elif card == 'A':
			ace_count += 1
			value += 11  # Asumsi Ace sebagai 11 terlebih dahulu
		else:
			value += int(card)

	while value > 21 and ace_count: # Mengurangi nilai Ace dari 11 menjadi 1 jika total > 21
		value -= 10
		ace_count -= 1

	return value

def display_hands(player_hand, dealer_hand, dealer_reveal = False):
	"""Menampilkan tangan pemain dan dealer."""
	if dealer_reveal:
		print(f"Kartu dealer adalah: {dealer_hand} (nilai: {calculate_hand_value(dealer_hand)})")
	else:
		print(f"Kartu dealer adalah: [{dealer_hand[0]}, ?]")

	print(f"Kartu anda sekarang adalah: {player_hand} (nilai: {calculate_hand_value(player_hand)})")

## Awal Program :)
print("Welcome to Blackjack!")

deck = [str(num) for num in range(2, 11)] + ['J', 'Q', 'K', 'A'] * 4 # Membuat dek kartu

random.shuffle(deck)

# Inisialisasi tangan pemain dan dealer
player_hand = [hit(deck)]
dealer_hand = [hit(deck)]

display_hands(player_hand, dealer_hand) # Tampilkan kartu awal

while True: # Pemain mengambil kartu
	choice = input("Apakah masih akan mengambil kartu? (y/n): ").lower()
	if choice == 'y':
		player_hand.append(hit(deck))
		if calculate_hand_value(player_hand) > 21:
			print("Anda kalah!")
			break
		display_hands(player_hand, dealer_hand)
	elif choice == 'n':
		break
	else:
		print("Pilihan tidak valid. Silakan masukkan 'y' atau 'n'.")

if calculate_hand_value(player_hand) <= 21: # Dealer mengambil kartu jika pemain tidak kalah
	while calculate_hand_value(dealer_hand) < 17:
		dealer_hand.append(hit(deck))

	display_hands(player_hand, dealer_hand, dealer_reveal=True)

	# Menentukan hasil permainan
	player_value = calculate_hand_value(player_hand)
	dealer_value = calculate_hand_value(dealer_hand)

	if dealer_value > 21:
		print("Anda menang, dealer melebihi 21.")
	elif player_value > dealer_value:
		print("Anda menang!")
	elif player_value < dealer_value:
		print("Dealer menang!")
	else:
		print("Seri!")
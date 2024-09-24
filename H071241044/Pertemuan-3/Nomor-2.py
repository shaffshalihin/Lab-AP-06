import random as rd

varAngka		= rd.randint(1, 100)
percobaan		= 0
max_percobaan	= 5

print("Ayo tebak angka!")
print("Angaknya diantara 1 hingga 100.")
print("Kamu punya 5 kesempatan untuk menebak.")
print("Masukkan '0' untuk menyerah.")

while percobaan < max_percobaan:
	try:
		tebakan = int(input("Masukkan tebakan Anda: "))

		if tebakan == 0:
			print("Anda telah berhenti bermain.")
			break

		percobaan += 1

		if tebakan == varAngka:
			print(f"Selamat! Anda menebak angka yang benar yaitu {varAngka}.")
			break
		elif tebakan > varAngka:
			print("Angka terlalu besar.")
		else:
			print("Angka terlalu kecil.")

		if percobaan == max_percobaan:
			print(f"Maaf, Anda kehabisan percobaan. Angka yang benar adalah {varAngka}.")

	except ValueError:
		print("Masukkan angka yang valid.")
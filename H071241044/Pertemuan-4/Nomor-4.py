def kalkulator_sederhana():
	"""Fungsi untuk melakukan perhitungan sederhana."""

	while True:
		try:
			a		= int(input("Masukkan angka pertama: "))
			b		= int(input("Masukkan angka kedua: "))
			op		= input("Masukkan operasi (+, -, *, /): ")
			hasil	= a + b if op == '+' else a - b if op == '-' else a * b if op == '*' else a / b if op == '/' and b != 0 else "Pembagian dengan nol tidak diperbolehkan." if b == 0 else False
			hasil	= hasil if hasil != False else "Operasi tidak valid. Gunakan +, -, *, atau /."
			print(hasil)

		except ValueError as e:
			print(f"Input tidak valid: {e}")

kalkulator_sederhana()
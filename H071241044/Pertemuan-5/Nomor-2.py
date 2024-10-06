inp     = input('Masukkan kata-kata: ')
words	= inp.split()
akronim	= ''.join([word[0].upper() for word in words])
print(f"Dari '{inp}' yang telah diimput dihasilkan akronim yaitu {akronim}")
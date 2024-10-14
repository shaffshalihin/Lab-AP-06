inp			= input('Masukkan string: ')
string		= inp.replace(',', '').split(' ')
string		= ''.join(string).lower()
keterangan	= 'palindrom' if string == string[::-1] else 'not palindrom'
print(keterangan)
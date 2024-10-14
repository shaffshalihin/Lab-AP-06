z = input("Masukkan kata: ")
x = 1
while x < len(z)+1:
	for i in range(0, len(z)+1):
		print(z[i:i+x]) if i+x < len(z)+1 else ''
	x+=1
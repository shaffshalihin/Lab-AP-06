inp			= int(input('masukkan tinggi: '))
tinggiAtas	= inp//2 + 1 if inp % 2 == 0 else inp//2 + 2

for i in range(1, tinggiAtas):
	print(' ' * ( inp - (2 * i) + 1),'* ' * (i + (i - 1)))

for i in range(inp//2, 0, -1):
	print(' ' * ( inp - (2 * i) + 1),'* ' * (i + (i - 1)))
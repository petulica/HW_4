a = int(input('Zadej délku strany: ')
	
for radek in range(a):
	if radek == 0 or radek == a-1:
		for strana in range(a):
			print ("X", end=' ')
		print()
	else:
		print('X', ' '*a+1, 'X')
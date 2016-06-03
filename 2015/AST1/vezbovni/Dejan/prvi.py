broj = 528
initial = -1

while initial!=broj:
	initial = int(input('unesite broj: '))
	if initial < broj:
		print('broj je manji')
	elif initial > broj:
		print('broj je veći')
	else: 
		print('bravo')

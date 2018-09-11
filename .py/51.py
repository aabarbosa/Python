palavra = raw_input()
list_a = []
list_e = []
list_i = [] 
list_o = []
list_u = []

for car in palavra:
	if car=='a' or car=='A':
		list_a.append(car)
		
	elif car=='e' or car=='E':
		list_e.append(car)
		
	elif car=='i' or car=='I':
		list_i.append(car)
		
	elif car=='o' or car=='O':
		list_o.append(car)
		
	elif car=='u' or car=='U':
		list_u.append(car)
		
print 'A -', len(list_a)
print 'E -', len(list_e)
print 'I -', len(list_i)
print 'O -', len(list_o)
print 'U -', len(list_u)
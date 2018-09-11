n = int(raw_input('n? '))
c = raw_input('c? ')

for sequencia in range(n):
	nome = raw_input('palavra? ')
	
	if nome[0].lower() == c.lower():
		print nome, "comeca com", c
	else:
		print nome, 'nao comeca com', c

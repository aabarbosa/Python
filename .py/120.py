# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 120

def cria_login(nome):
	nome_dividido = nome.split()
	
	# remove 'de','da','do', se existirem.
	remover = []
	for i in range(len(nome_dividido)):
		if nome_dividido[i] in ['de','da','do']:
			remover.append(nome_dividido[i])
	
	if len(remover) >= 1:
		for str in remover:
			nome_dividido.remove(str)
			
	login = nome_dividido[0].lower()
	for i in range(1,len(nome_dividido)):
		login += nome_dividido[i][0:1].lower()

	return login

print cria_login("Matheus de da do Gaudencio do Rego Do") 
print cria_login("Eliane da de do Araujo") 
print cria_login("da de do Dalton Serey Do de Guerrero do")
	
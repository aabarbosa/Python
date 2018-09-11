# coding: utf-8
# Aluno: Alekssandro Assis Barbosa. Matrícula: 21211001. Exercício: 88

while True:
	contador = 0
	
	word = raw_input()
	
	if word == 'fim': break
	
	for car in word:
		if car in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			contador +=1
			
	print contador
	

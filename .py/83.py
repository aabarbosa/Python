# coding: utf-8
# Aluno: Alekssandro Assis Barbosa. Matr�cula: 21211001. Exerc�cio: 83

while True:
	word = raw_input()
	
	if word == 'fim': break
	
	for car in word:
		if car in 'aeiouAEIOU':
			print car
			break
		
	if car not in 'aeiouAEIOU':
		print '-'
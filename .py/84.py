# coding: utf-8
# Aluno: Alekssandro Assis Barbosa. Matrícula: 21211001. Exercício: 84

word = raw_input()
	
for car in word:
	if car in 'aeiouAEIOU':
		print car
		break
		
if car not in 'aeiouAEIOU':
	print '-'
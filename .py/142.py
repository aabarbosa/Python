# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 142



def movimentos_possiveis(labirinto):
	for i in range(len(labirinto)):
		for j in range(len(labirinto[0])):
			if labirinto[i][j] == "*":
				indice_i = i
				indice_j = j
				
	conta = 0
	if indice_j+1 in range(len(labirinto[0])):
		if labirinto[indice_i][indice_j+1] == " ":
			conta += 1
	if indice_j-1 in range(len(labirinto[0])):
		if labirinto[indice_i][indice_j-1] == " ":
			conta += 1
	if indice_i+1 in range(len(labirinto)):
		if labirinto[indice_i+1][indice_j] == " ":
			conta += 1
	if indice_i-1 in range(len(labirinto)):
		if labirinto[indice_i-1][indice_j] == " ":
			conta += 1
			
	return conta

labirinto1 = [
  ['P', ' ', ' ', ' '],
  ['P', '*', 'P', ' '],
  ['P', 'P', 'P', ' '],
]
print movimentos_possiveis(labirinto1)



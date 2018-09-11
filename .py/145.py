# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 145

def acima_media(tabela_notas):
	indices = []
	for j in range(len(tabela_notas[0])):
		soma = 0
		for i in range(len(tabela_notas)):
			soma += tabela_notas[i][j]
		media = float(soma)/len(tabela_notas)
		if media >= 7:
			indices.append(j)
			
	return indices

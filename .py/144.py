# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 144

def calcula_media(tabela_notas):
	medias = []
	for i in range(len(tabela_notas)):
		soma = 0
		for j in range(len(tabela_notas[0])):
			soma += tabela_notas[i][j]
		medias.append("%.1f" % (float(soma)/len(tabela_notas[0])))
	
	return medias

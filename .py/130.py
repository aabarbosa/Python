# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 130

def soma_mats(M1,M2):
	assert len(M1) == len(M2)
	
	matriz_soma = []
	for i in range(len(M1)):
		linha = []
		for j in range(len(M1[0])):
			linha.append(M1[i][j] + M2[i][j])
		matriz_soma.append(linha)
		
	return matriz_soma
		
m1 = [[0, 0, 0],
      [0, 0, 0]]
m2 = [[0, 0, 0],
      [ 0,-1,0]]
print soma_mats(m1, m2)

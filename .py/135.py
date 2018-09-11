# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 135

def somacols(M):
	matriz = []
	for j in range(len(M[0])):
		soma_da_col = 0
		for i in range(len(M)):
			soma_da_col += M[i][j]
		matriz.append(soma_da_col)
	return matriz
		
m = [[0, 20, -7],
     [ 5, 14,  3],
     [ 6,  7, 0]]
print somacols(m)

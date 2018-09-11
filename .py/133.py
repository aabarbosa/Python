# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 133

def transposta(M):
	transposta = []
	for j in range(len(M[0])):
		linha_transposta = []
		for i in range(len(M)):
			linha_transposta.append(M[i][j])
		transposta.append(linha_transposta)
	return transposta
		
m = [[10, 20, -7],
     [ 5, 14,  3],
     [ 6,  7, -2]]
print transposta(m)

# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 165

def colunas_com_zero(M):
	'''	Retorna uma lista com os indices das colunas de M que
	possuem o elemento zero '''
	
	indices = []
	for j in range(len(M[0])):
		for i in range(len(M)):
			if M[i][j] == 0:
				if j not in indices:
					indices.append(j)
	return indices

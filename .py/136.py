# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 136

def eh_triangular_sup(M):
	
	""" Verifica se a matriz M eh triangular superior """
	
	j_da_diag = 0
	for i in range(len(M)):
		for j in range(len(M[0])):
			if j < j_da_diag:
				print M[i][j]
				if M[i][j] != 0:
					return False
		j_da_diag += 1
	return True


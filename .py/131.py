# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 131

def diag_principal(M):
	n = 0 # equilibra os indices da diagonal
	values_diag = []
	for i in range(len(M)):
		values_diag.append(M[i][0+n])
		n += 1
	return values_diag
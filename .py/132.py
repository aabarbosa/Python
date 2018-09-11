# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 132

def diag_secundaria(M):
	n = -1 # equilibra os indices da diagonal
	values_diag = []
	for i in range(len(M)):
		values_diag.append(M[i][len(M[0])+n])
		n += -1
	return values_diag
	
m = [[0, 20, -7348],
     [ 5, 1,  3],
     [100,  7, -2]]
print diag_secundaria(m)


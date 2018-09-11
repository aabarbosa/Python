# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 160

def soma_linha(escalar, nlin1, nlin2, M):
	if nlin1 in range(len(M)) and nlin2 in range(len(M)):
		
		for j in range(len(M[0])):
			M[nlin1][j] * escalar
		return True
	
	return False
		
M = [[1,2], [3,4]]
assert soma_linha(2.0, 0, 1, M) == True
print M



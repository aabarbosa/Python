# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 159

def mult_linha(nlin1, escalar, M):
	if nlin1 in range(len(M)):
		for j in range(len(M[0])):
			M[nlin1][j] = M[nlin1][j] * escalar
		return True
		
	else:
		return False



M = [[1,2], [3,4]]
print mult_linha(0, 2.0, M) == True
print M == [[2.0, 4.0], [3, 4]]


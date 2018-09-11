# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 158


def troca_linhas(lin1,lin2,M):
	'''
	A lin1 é substituida por lin2 e vice-versa, na matriz M.
	Retorna True se a substituição é possível, caso contrário False.
	'''
	
	if lin1 in range(len(M)) and lin2 in range(len(M)):
		linha1,linha2 = [],[]
		for j in range(len(M[0])):
			linha1.append(M[lin1][j])
			linha2.append(M[lin2][j])

		for j in range(len(M[0])):
			M[lin1][j] = linha2[j]
			M[lin2][j] = linha1[j]
		return True
		
	else:
		return False


M = [[1,2], [3,4]]
print troca_linhas(0, 1, M)
print M == [[3,4], [1,2]]


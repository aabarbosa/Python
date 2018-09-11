# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 158

def eh_escalonada(M):
	nlin,ncol,maior = len(M),len(M[0]),0
	if nlin > ncol:
		menor = ncol
	else:
		menor = nlin
		
	for i in range(menor):
		for j in range(menor):
			if i == j:
				if M[i][i] != 1: return False
			if i != j:
				if M[i][j] != 0: return False		
	return True
	
		
assert eh_escalonada([[1,2,3], [3,4,5]]) == False
assert eh_escalonada([[1,0,3], [0,1,6]]) == True

assert eh_escalonada([  [1,0,0,1],
						[0,1,0,1],
						[0,0,1,1]]) == True


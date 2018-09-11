# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 162


def matriz_coincidencia(M1, M2):
	'''Retorna uma matriz modelo de M1 e M2 com zeros nas posições de
	elementos que não se repetem em M1 e M2, caso contrário o elemento
	é repetido na matriz retornada'''	
	
	assert len(M1) == len(M2) and len(M1[0]) == len(M2[0])
	
	M = [[0]*len(M1[0]) for i in range(len(M1))]
	
	for i in range(len(M1)):
		for j in range(len(M1[0])):
			if M1[i][j] == M2[i][j]:
				M[i][j] = M1[i][j]
				
	return M
	
	
M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M2= [[10, 11, 12],
     [13, 14, 15],
     [ 7,  8,  9]]

M3= [[ 1,  2,  3],
     [13, 14, 15],
     [16, 17, 18]]
  

assert matriz_coincidencia(M1, M2) == [[0,0,0],[0,0,0],[7,8,9]]
assert matriz_coincidencia(M1, M3) == [[1,2,3],[0,0,0],[0,0,0]]


	

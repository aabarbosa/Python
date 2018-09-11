# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 134

def coluna(M,col_i):
	col = []
	for i in range(len(M)):
		col.append(M[i][col_i])
	return col
	
m = [[10, 20, -0],
     [ 5, 14,  1],
     [ 6,  7, 2]]
print coluna(m,2)

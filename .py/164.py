# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 164


def constroi_matriz(lin, col, list_values):
	'''
	Constrói e retorna uma matriz de dimensões 'lin' por 'col'
	através dos valores fornecidos.
	
	'''
	
	assert len(list_values) == lin * col, 'Dados inválidos'
	
	M_model = [col*[0] for i in range(lin)]
	
	indice = 0
	for i in range(len(M_model)):
		for j in range(len(M_model[0])):
			M_model[i][j] = list_values[indice]
			indice += 1
	
	return M_model


valores = [1,2,3,4,1,5,6,7,8,1,1,2,3,4,1]
assert constroi_matriz(3, 5, valores) == [[1,2,3,4,1], [5,6,7,8,1],[1,2,3,4,1]]
assert valores == [1,2,3,4,1,5,6,7,8,1,1,2,3,4,1]


# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 167


def quadrada_e_nao_repete(quad):
	'''	  Verifica se Matriz quad eh quadrada e nao possui elementos
	repetidos, se sim retorna True, caso contrário False   '''
	
	while True:
		lin,col = 0,0
		for i in range(len(quad)):
			for j in range(len(quad[0])):
				if quad[i][j] == quad[lin][col]: 			# se há elemento repetido
					return False
		
		if quad[lin][col] == quad[len(quad)-1][len(quad[0])-1]: break
		
		if col < len(quad[0])-1:
			col += 1
		elif lin < len(quad)-1:
			lin += 1
			if col == len(quad[0]-1):
				col = 0		




def eh_quadrado_magico(quad):
	'''	  Verifica se os valores da Matriz quad formam um quadrado
	 mágico, se sim retorna True, caso contrário False   '''
	 
	if len(quad) != len(quad[0]):    						# se nao for quadrada
		return False
		
	somas = []
	diagP,diagS = 0,0
	for i in range(len(quad)):
		vlin,vcol = 0,0
		for j in range(len(quad[0])):
			vlin += quad[i][j]
			vcol += quad[j][i]
		somas.append(vlin)				       		# soma para cada linha
		somas.append(vcol)				       		# soma para cada coluna
		
		diagP += quad[i][i]
		diagS += quad[i][len(quad[0])-1-i]             
	somas.append(diagP) 				       		# soma diagonal principal
	somas.append(diagS)					       		# soma diagonal secundária
	
	for i in range(len(somas)-1):
		if somas[i] != somas[i+1]:   						# se há soma diferente
			return False
			
	return True
	
	
quadrado1 = [[2,7,6],[9,5,1],[4,3,8]]
quadrado2 = [[1,2,3],[4,5,6]]

print eh_quadrado_magico(quadrado1) == True
print eh_quadrado_magico(quadrado2) == False


	
		
	
	

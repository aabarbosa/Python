# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 140

def move_direita(M):
	for i in range(len(M)):	
		for j in range(len(M[0])):
			if M[i][j] == "*":
				idc_i = i
				idc_j = j
	
	if idc_j+1 in range(len(M[0])):
		if M[idc_i][idc_j+1] == " ":
			M[idc_i][idc_j+1] = "*"
			M[idc_i][idc_j] = " "
			
			return idc_i, idc_j+1
		
	return idc_i, idc_j


labirinto1 = [ ['P', ' ', '*', ' '],  ['P', ' ', 'P', ' '], ['P', 'P', 'P', ' ']]
assert move_direita(labirinto1) == (0, 3)

assert labirinto1 ==  [ ['P', ' ', ' ', '*'], ['P', ' ', 'P', ' '], ['P', 'P', 'P', ' ']]

labirinto2 = [ ['P', 'P', ' ', ' '], ['P', ' ', ' ', '*'], ['P', 'P', 'P', ' ']]
assert move_direita(labirinto2) == (1, 3)


			
				

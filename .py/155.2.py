# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 155

def jogo_da_velha(tab):
	"""
	Verifica se houve ganhadores através de tab preenchido.
	
	"""
	
	# Itera por linhas e diagonais verificando se houve ganhadores.
	Os_diagS,Xs_diagS = 0,0
	for i in range(len(tab)):
		Os_linha,Xs_linha = 0,0
		Os_diagP,Xs_diagP = 0,0
		for j in range(len(tab[0])): # linhas
			if tab[i][j] == "O":
				Os_linha += 1
			else:
				Xs_linha += 1
			
			if i == j:  # diagonal principal
				if tab[i][j] == "O":
					Os_diagP += 1
				else:
					Xs_diagP += 1
					
			if i+j == len(tab)-1: # diagonal secundaria
				if tab[i][j] == "O":
					Os_diagS += 1
				else:
					Xs_diagS += 1
					
			if Os_linha == 3 or Os_diagP == 3 or Os_diagS == 3:
				return "O ganhou"
			elif Xs_linha == 3 or Xs_diagP == 3 or Xs_diagS == 3:
				return "X ganhou"
		
	for j in range(len(tab[0])):  # colunas
		Os_coluna,Xs_coluna = 0,0
		for i in range(len(tab)):
			if tab[i][j] == "O":
				Os_coluna += 1
			else:
				Xs_coluna += 1
				
		if Os_coluna == 3:
			return "O ganhou"
		elif Xs_coluna == 3:
			return "X ganhou"
		
	return "Ninguem ganhou"
	

tabuleiro1 = [	['O', 'O', 'X'],
				['X', 'O', 'O'],
				['O', 'O', 'X'] 	]
			  
tabuleiro2 = [	['O', 'X', 'X'],
				['X', 'X', 'O'],
				['O', 'O', 'X'] 	]
print jogo_da_velha(tabuleiro1)
print jogo_da_velha(tabuleiro2)


	

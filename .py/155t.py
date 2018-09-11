# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 155

def jogo_da_velha(t):
	if t[0][0] == t[1][1] == t[2][2] and t[0][0] == 'X' or t[0][0] == t[1][1] == t[2][2] and t[0][0] == 'O':
		return t[0][0] + ' ganhou'
		
	if t[0][2] == t[1][1] == t[2][0] and t[0][2] == 'X' or t[0][2] == t[1][1] == t[2][0] and t[0][2] == 'O':
		return t[0][2] + ' ganhou'
	
	for i in range(3):
		list,list2 = [],[]
		for j in range(3):
			list.append(t[i][j])
			list2.append(t[j][i])
			
		if len(set(list )) == 1 and list[0] == 'X' or len(set(list )) == 1 and list[0] == 'O': 
			return list [0] +  ' ganhou'
		if len(set(list2)) == 1 and list2[0] == 'X' or len(set(list2)) == 1 and list2[0] == 'O': 
			return list2[0] +  ' ganhou'
		
	return 'Ninguem ganhou'




tabuleiro1 = [  ['-','-','-'],
				['X','X','X'],
				['O','O','-'], 	]
				
print jogo_da_velha(tabuleiro1)
				
				
				
tabuleiro1 = [	['O', 'X', 'O'],
				['O', 'X', 'X'],
				['X', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'X', 'O'],
				['O', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)	

tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'O', 'X'],
				['O', 'X', 'O'] ]			  
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['O', 'X', 'O'],
				['O', 'O', 'X'],
				['X', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'X', 'O'],
				['O', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'X', 'O'],
				['X', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)				
						
						
		
tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'X', 'X'],
				['X', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'X', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'X', 'X'],
				['O', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)

tabuleiro1 = [	['X', 'O', 'O'],
				['X', 'X', 'X'],
				['X', 'X', 'O'] ]			  
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'O', 'X'],
				['X', 'X', 'X'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['X', 'O', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'X', 'O'],
				['O', 'X', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'X', 'X'],
				['X', 'O', 'X'] ]
print jogo_da_velha(tabuleiro1)



tabuleiro1 = [	['O', 'O', 'X'],
				['O', 'O', 'X'],
				['X', 'O', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'O', 'X'],
				['O', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['O', 'O', 'O'],
				['O', 'X', 'X'],
				['X', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)

tabuleiro1 = [	['X', 'O', 'X'],
				['O', 'O', 'O'],
				['X', 'X', 'O'] ]			  
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'X', 'X'],
				['O', 'O', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['O', 'X', 'O'],
				['O', 'O', 'X'],
				['O', 'X', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'O', 'X'],
				['X', 'O', 'O'] ]
print jogo_da_velha(tabuleiro1)


tabuleiro1 = [	['X', 'O', 'O'],
				['O', 'X', 'O'],
				['X', 'O', 'O'] ]
print jogo_da_velha(tabuleiro1)





tabuleiro1 = [  ['O','O','O'],
				['X','X','x'],
				['O','O','X'], 	]
				
print jogo_da_velha(tabuleiro1)


# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 119

def eh_vencedor_linea(tabuleiro):
	j = tabuleiro[0]
	for i in range(len(tabuleiro)):
		if j >= len(tabuleiro) or j < 0:
			return False
		if j == 0:
			return True
		j = tabuleiro[j]
	return False
	
assert eh_vencedor_linea([2,0,1])
assert not eh_vencedor_linea([1,2,3])
assert eh_vencedor_linea([1,2,3,4,5,0])



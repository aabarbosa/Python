# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 119

def eh_vencedor_linea(tabuleiro):
	tabuleiro.sort()
	for i in range(len(tabuleiro)-1):
		if tabuleiro[i] == tabuleiro[i+1]:
			return False
	if tabuleiro.count(0) == 1:
		return True
	return False

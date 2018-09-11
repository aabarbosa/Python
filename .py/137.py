# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 137

def zera_diagonal(M):
	n = 0
	for i in range(len(M)):
			M[i][n] = 0
			n += 1

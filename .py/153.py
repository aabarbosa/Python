# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 153

def turma_pratica(alocacao, t):
	count = 0
	for v in alocacao.values():
		if v == t:
			count += 1
	return count
	
alocacao = {"Franco": 2, "Joabson": 2, "Monalisa": 4, "Rafael": 3, "Feliciano": 4}

assert turma_pratica(alocacao, 4) == 2
assert turma_pratica(alocacao, 1) == 0
assert turma_pratica(alocacao, 3) == 1




# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 150


def turma_pratica(alocacao, t):
	contador = 0
	for v in alocacao.values():
		if v[1] == t:
			contador += 1
	return contador
	
alocacao = {"Nathan": (2, 4),
          "Isis": (1, 3),
          "Melissa": (3, 5),
          "Davi": (2, 2),
          "Aristofanes": (2, 4)}

assert turma_pratica(alocacao, 4) == 2
assert turma_pratica(alocacao, 1) == 0
assert turma_pratica(alocacao, 5) == 1


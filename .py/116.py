# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 116

def altera_vetor_por_escalar(vetor,escalar):
	for i in range(len(vetor)):
		vetor[i] = vetor[i]*escalar
		
vetor_1 = [1, 2, 3]
altera_vetor_por_escalar(vetor_1, -1)
assert vetor_1 == [-1, -2, -3]
altera_vetor_por_escalar(vetor_1, 2)
assert vetor_1 == [-2, -4, -6]


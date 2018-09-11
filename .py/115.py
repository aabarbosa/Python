# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 115

def vetor_por_escalar(vetor, escalar):
	vetor_resultante = []
	for coord in vetor:
		vetor_resultante.append(coord*escalar)
	return vetor_resultante
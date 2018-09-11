# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 127

def indices_de_idosos(fila):
	indices_idosos = []
	for i in range(len(fila)):
		if fila[i] >= 60:
			indices_idosos.append(i)
	return indices_idosos

# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 118

def filtra_lista(num,lista):
	assert num > 0 and len(lista) >= 1
	indices = []
	for i in range(len(lista)):
		if i%num == 0:
			indices.append(lista[i])
	return indices
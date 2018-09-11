# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 124

def menores(N,lista):
	menores = [] 
	for v in lista:
		if v < N:
			menores.append(v)
	return menores
	
lista = [1, 2, 3, 4, 5]
assert menores(3, lista) == [1, 2]
print menores(3, lista)
print lista

# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 125

def remove_menores(N,lista):
	menores = [] 
	for v in lista:
		if v < N:
			menores.append(v)
	for menor in menores:
		lista.remove(menor)
	return len(menores)
	
lista = [1, 2, 3, 4, 5]
assert remove_menores(3, lista) == 2
assert lista == [3, 4, 5]
 

# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 117

def filtra_altera_lista(num,lista):
	# Busca linear de índices não divisíveis por num
	indices = [] 
	for i in range(len(lista)):
		if i%num != 0:
			indices.append(i)
	
	# Remove de lista os elementos nas posições listadas em Indices
	equilibra = 0
	for i in indices:
		lista.pop(i+equilibra)
		equilibra += -1


lista1 = [0,1,2,3,4,5,6]
lista2 = [2,3,5,7,11,13,17]

filtra_altera_lista(2, lista1)
assert lista1 == [0,2,4,6]
filtra_altera_lista(3, lista1)
assert lista1 == [0,6]

filtra_altera_lista(3, lista2)
filtra_altera_lista(2, lista2)
assert lista2 == [2, 17]



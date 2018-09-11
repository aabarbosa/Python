# coding: utf-8
# Alekssandro Assis Barbosa
# 21211001
# 147


def ausentes(books):
	contador = 0
	for v in books.values():
		if v == 0:
			contador += 1
	return contador
	

livros = { "Metamorfose":0, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
assert ausentes(livros) == 3


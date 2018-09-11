# coding: utf-8

receitas = []
despesas = []

# For varia para adicionar valores de receitas e despesas nas respectivas listas.
for i in range(12):
	valor = map(float, raw_input().split())
	receitas.append(valor[0])
	despesas.append(valor[1])

# Formatação e impressão da lista de Lucro
for i in range(len(receitas)):
	lucro = receitas[i] - despesas[i]
	print '%4.1f' % lucro
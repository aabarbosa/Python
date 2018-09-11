# coding: utf-8

# Receitas e despesas nas respectivas listas.
receitas = map(float, raw_input().split())
despesas = map(float, raw_input().split())
month = ['jan', 'fev' ,'mar', 'abr', 'mai', 'jun', 'jul', 'ago' , 'set' , 'out', 'nov', 'dez']

# Formata��o e impress�o da lista de Lucro por m�s
for i in range(len(receitas)):
	lucro = receitas[i] - despesas[i]
	if lucro < 0:
		print '%s %4.1f' % (month[i], lucro)
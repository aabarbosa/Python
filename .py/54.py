# coding: utf-8

list_valores = []
valor = 0

while valor >= 0:
	valor = float(raw_input('valor? '))
	list_valores.append(valor)

list_valores.pop()
print '---'
print 'Quantidade de valores:', len(list_valores)
print 'Soma dos valores: %.1f' % sum(list_valores)

if len(list_valores) > 0:
	print 'Média: %.1f' % (sum(list_valores)/len(list_valores))
else:
	print 'Média: 0.0'
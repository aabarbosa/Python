x = float(raw_input('Valor? '))
x = x**2

print 'Sem arredondamento:', x

if x != int(x):
	print 'Com arredondamento para cima:', float(int(x)+1)
else:
	print 'Com arredondamento para cima:', float(x)

print 'Com arredondamento para baixo:', float(int(x))
print 'Valor truncado:', int(x)
comp = float(raw_input('Comprimento? '))
larg = float(raw_input('Largura? '))
alt = float(raw_input('Altura? '))
assert comp != larg or larg != alt or alt != comp

lateral = 2*(comp*alt)/1.5
frente = 2*(larg*alt)/1.5
caixas = lateral + frente

if caixas != int(caixas):
	print 'Quantidade de caixas:', int(caixas+1)
else:
	print 'Quantidade de caixas:', int(caixas)

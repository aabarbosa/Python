kmi = float(raw_input('Km inicial? '))
kmf = float(raw_input('Km final? '))
litros = float(raw_input('Litros? '))
recebido = float(raw_input('Total recebido? '))

consumo = int((kmf - kmi)/litros)
lucro = recebido - litros*2.55

print 'Consumo em Km/L:', consumo
print 'Lucro liquido:', lucro
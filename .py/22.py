
inicial = float(raw_input('Valor atual? '))
final = float(raw_input('Novo valor? '))

print 'Reajuste de %.1f' % (((final - inicial )/inicial) * 100) + '%'
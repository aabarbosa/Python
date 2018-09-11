
valor = float(raw_input('Valor de venda? '))

impostos = 0.4 * valor/1.4

print 'ICMS:', 0.18 * (valor - impostos)
print 'IPI:', 0.13 * (valor - impostos)
print 'PIS:', 0.014 * (valor - impostos)
print 'Cofins:', 0.076 * (valor - impostos)
print 'Valor sem impostos:', valor - 0.4*valor/1.4